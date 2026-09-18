# Build: 35bd2ba7a1398d5f6eb65e0a4111dac6

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
