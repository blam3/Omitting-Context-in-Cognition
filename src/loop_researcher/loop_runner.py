"""
Minimal API-based loop runner.

This is intentionally conservative. It does not execute arbitrary shell commands
and it treats approval-gated actions as stop conditions.

Before using:
  pip install openai python-dotenv
  cp .env.example .env
  edit .env
"""

from pathlib import Path
import json
import os

try:
    from dotenv import load_dotenv
    from openai import OpenAI
except ImportError as exc:
    raise SystemExit("Install dependencies first: pip install openai python-dotenv") from exc

from loop_researcher.config import LoopConfig
from loop_researcher.policy import requires_approval
from loop_researcher.local_tools import run_safe_command

ROOT = Path(__file__).resolve().parents[2]

def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")

def load_agent(agent_file: str) -> str:
    return read_text(f"agents/{agent_file}")

def build_context() -> str:
    files = [
        "docs/research_spec.md",
        "docs/approval_policy.md",
        "docs/claim_registry.md",
        "docs/assumption_registry.md",
    ]
    chunks = []
    for f in files:
        chunks.append(f"\n\n--- FILE: {f} ---\n{read_text(f)}")
    return "\n".join(chunks)

def run_agent_task(agent_file: str, objective: str) -> dict:
    load_dotenv(ROOT / ".env")
    cfg = LoopConfig()
    client = OpenAI()

    agent_spec = load_agent(agent_file)
    context = build_context()

    instructions = f"""
You are operating as a bounded-autonomy research agent.

Agent specification:
{agent_spec}

Project context:
{context}

Return JSON only with these keys:
task_id, status, summary, files_changed, approval_needed, approval_request, risks, next_actions.

Do not invent citations.
Do not introduce new assumptions without setting approval_needed=true.
Do not make interpretive or literature claims without setting approval_needed=true.
Do not request deletion or expensive jobs without approval_needed=true.
"""

    response = client.responses.create(
        model=cfg.model,
        input=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": objective},
        ],
        reasoning={"effort": cfg.reasoning_effort},
    )

    text = response.output_text
    if requires_approval(text):
        return {
            "task_id": "manual-review",
            "status": "needs_approval",
            "summary": "The proposed output appears to require human approval.",
            "files_changed": [],
            "approval_needed": True,
            "approval_request": text,
            "risks": ["Approval policy triggered."],
            "next_actions": ["Review manually before applying changes."],
        }

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {
            "task_id": "parse-failure",
            "status": "failed",
            "summary": "Agent output was not valid JSON.",
            "files_changed": [],
            "approval_needed": True,
            "approval_request": text,
            "risks": ["Structured output parsing failed."],
            "next_actions": ["Retry with stricter schema or inspect output manually."],
        }

if __name__ == "__main__":
    result = run_agent_task(
        agent_file="principal_investigator.md",
        objective="Create the first three GitHub issues needed to make this repository publishable."
    )
    print(json.dumps(result, indent=2))
