import os, json
import redis
import time

r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, decode_responses=True)

print("Tester agent started, waiting for results to test...")

while True:
    _, raw = r.blpop('results')
    res = json.loads(raw)
    # Placeholder for running tests; integrate your test runner here
    print(f"Running tests for {res['id']}: OK (placeholder)")
    time.sleep(0.1)
