GT-300 — Top 10 Takeaways plan

Problem
- Produce the single most important "Top 10 takeaways" summary from the GT-300 course that helps learners quickly internalize core concepts and apply them.

Approach
1. Gather course materials (syllabus, slides, readings, recorded lectures).
2. Map materials to learning objectives and modules.
3. Extract candidate takeaways per module (concise principle + why it matters).
4. Distill and prioritize into the Top 10 based on frequency, centrality to objectives, and practical impact.
5. Add one-line actionables or examples for each takeaway.
6. Review and refine for clarity and brevity.

Deliverables
- Top 10 takeaways list (one sentence each) with a one-line actionable example.
- Optional flashcard set (Q/A) derived from each takeaway.
- Short revision script (5–10 minutes) for quick review.

Todos (high-level)
- gather-materials: Collect GT-300 syllabus, slides, readings, and lecture recordings.
- map-objectives: Create a module -> learning objectives map.
- extract-candidates: Extract candidate takeaways from each module.
- distill-top10: Prioritize and distill the Top 10 takeaways.
- write-examples: Write one-line actionable examples for each takeaway.
- create-flashcards: (Optional) Draft flashcards from each takeaway.
- review-refine: Peer-review and refine the final Top 10 list.

Notes
- If the user wants the list tailored to exam prep, project application, or interviews, request that context before distillation.
- Default scope: produce a general-purpose Top 10 suitable for both study and practical application.

Progress: Multi-agent starter created
- Created a minimal multi-agent prototype in session-state: docker-compose.yml, Dockerfile, requirements.txt, orchestrator.py, coder.py, tester.py, prompts.md, README-starter.md.
- Prototype uses Redis queue; coder.ai_synthesize() is a placeholder for LLM calls.
- Next steps: replace ai_synthesize() with an LLM client, add secrets management (.env or secrets manager), create per-service Dockerfiles, add RBAC/sandboxing, and add test harness.

