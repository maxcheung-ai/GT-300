import os, time, json
import redis

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

def enqueue_task(task):
    r.rpush("tasks", json.dumps(task))

def listen_results():
    print("Orchestrator listening for results...")
    while True:
        item = r.blpop("results", timeout=5)
        if item:
            _, raw = item
            data = json.loads(raw)
            print("Result:", json.dumps(data, indent=2))
        else:
            time.sleep(1)

if __name__ == '__main__':
    sample = {"id":"task-1","type":"code","payload":{"summary":"Implement /hello endpoint","files":["app.py"]}}
    enqueue_task(sample)
    print("Enqueued sample task", sample["id"])
    listen_results()
