Multi-agent starter (minimal)

Files created:
- docker-compose.yml (redis + orchestrator + coder + tester)
- Dockerfile, requirements.txt
- orchestrator.py, coder.py, tester.py
- prompts.md

Quick run (Docker):
1. docker build -t ma-starter .
2. docker-compose up --build

Quick run (local):
1. python -m venv .venv && .venv\Scripts\activate
2. pip install -r requirements.txt
3. Run redis locally, then in separate terminals: python orchestrator.py, python coder.py, python tester.py

Next: replace ai_synthesize() with your LLM client, add authentication, sandboxing, and human checkpoints.
