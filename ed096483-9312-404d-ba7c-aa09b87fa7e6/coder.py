import os, json, time, re
import redis

# Optional OpenAI integration — coder will call OpenAI when OPENAI_API_KEY is set
try:
    import openai
except Exception:
    openai = None

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

if OPENAI_KEY and openai:
    openai.api_key = OPENAI_KEY

print("Coder agent started, waiting for tasks...")

SYSTEM_MSG = (
    "You are the Coder LLM. Input: task.payload.summary and files. "
    "Return a JSON object with keys: code (string) and explanation (string). "
    "Do not wrap code in markdown fences; return raw code in the 'code' field."
)


def call_llm_for_code(summary):
    if not (OPENAI_KEY and openai):
        # fallback stub when no key or client
        return {"code": f"# Stub for {summary}\nprint('hello from stub')\n", "explanation": "No LLM key configured; returned a stub."}

    messages = [
        {"role": "system", "content": SYSTEM_MSG},
        {"role": "user", "content": f"Task: {summary}\nRespond with a JSON object as described."}
    ]

    resp = openai.ChatCompletion.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=messages,
        temperature=0.2,
        max_tokens=1200,
    )
    text = resp["choices"][0]["message"]["content"]

    # Try to parse JSON from the model output
    try:
        return json.loads(text)
    except Exception:
        m = re.search(r"\{.*\}", text, re.S)
        if m:
            try:
                return json.loads(m.group(0))
            except Exception:
                pass
        # If parsing fails, return the raw text as code
        return {"code": text, "explanation": "Model output was not valid JSON; returned raw content as code."}


while True:
    _, raw = r.blpop('tasks')  # block until a task arrives
    task = json.loads(raw)
    task_id = task.get('id')
    print('Processing', task_id)
    summary = task.get('payload', {}).get('summary', '')

    payload = call_llm_for_code(summary)
    result = {"id": task_id, "status": "done", "result": payload}
    r.rpush('results', json.dumps(result))
    print('Pushed result', result['id'])
    time.sleep(0.1)
