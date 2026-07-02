APPROVAL_REQUIRED_PATTERNS = [
    "new assumption",
    "new estimand",
    "interpretive claim",
    "literature claim",
    "delete",
    "remove file",
    "expensive job",
    "slurm",
    "submit job",
    "journal submission",
]

def requires_approval(text: str) -> bool:
    lowered = text.lower()
    return any(pattern in lowered for pattern in APPROVAL_REQUIRED_PATTERNS)
