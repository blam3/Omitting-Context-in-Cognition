from dataclasses import dataclass
import os

@dataclass
class LoopConfig:
    model: str = os.getenv("OPENAI_MODEL", "gpt-5.5")
    reasoning_effort: str = os.getenv("OPENAI_REASONING_EFFORT", "high")
    max_autofix_attempts: int = int(os.getenv("MAX_AUTOFIX_ATTEMPTS", "10"))
    max_local_replications_without_approval: int = int(os.getenv("MAX_LOCAL_REPLICATIONS_WITHOUT_APPROVAL", "25"))
    expensive_job_replication_threshold: int = int(os.getenv("EXPENSIVE_JOB_REPLICATION_THRESHOLD", "250"))
    expensive_job_core_threshold: int = int(os.getenv("EXPENSIVE_JOB_CORE_THRESHOLD", "32"))
