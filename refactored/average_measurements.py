from typing import List, Union


def average_valid_measurements(values: List[Union[float, int, None]]) -> float:
    """
    Computes the average of valid numeric measurements.

    Args:
        values (List[Union[float, int, None]]): List of numeric values or None.

    Returns:
        float: Average of valid numeric values. Returns 0.0 if no valid entries.

    Notes:
        - Ignores None or non-numeric values.
        - Safe against TypeError or ValueError from invalid entries.
    """
    total = 0.0
    count = 0

    for v in values:
        if v is None:
            continue
        try:
            total += float(v)
            count += 1
        except (TypeError, ValueError):
            continue

    return total / count if count > 0 else 0.0
