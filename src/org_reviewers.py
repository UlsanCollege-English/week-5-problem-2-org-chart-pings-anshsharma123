def count_senior(root, min_level):
    """
    Return how many people in the org tree have level >= min_level.
    Node format: {"name": str, "level": int, "reports": [nodes]}
    """
    # Handle None or invalid input
    if root is None or not isinstance(root, dict):
        return 0

    # Extract level; default to 0 if missing
    level = root.get("level", 0)

    # Count 1 if level meets or exceeds the minimum
    count = 1 if level >= min_level else 0

    # Get list of reports (default to [])
    reports = root.get("reports", [])

    # Recursively count in each report
    for r in reports:
        count += count_senior(r, min_level)

    return count
