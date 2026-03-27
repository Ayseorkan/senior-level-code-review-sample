from typing import Any, Dict, List

def calculate_average_order_value(orders: List[Dict[str, Any]]) -> float:
    """
    Calculates the average order value from a list of orders, excluding cancelled orders
    and ignoring invalid amount entries.

    Args:
        orders (List[Dict[str, Any]]): List of order dictionaries. Each should have 
            a 'status' key and an 'amount' key.

    Returns:
        float: Average amount of valid, non-cancelled orders. Returns 0.0 if no valid orders.

    Notes:
        - Safely handles missing or non-numeric 'amount' values.
        - Ignores orders with status 'cancelled'.
    """
    total = 0.0
    count = 0

    for order in orders:
        if order.get("status") != "cancelled":
            try:
                total += float(order.get("amount", 0))
                count += 1
            except (TypeError, ValueError):
                continue

    return total / count if count > 0 else 0.0