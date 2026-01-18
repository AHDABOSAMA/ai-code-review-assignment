# Write your corrected implementation for Task 1 here.
def calculate_average_order_value(orders):
    total = 0.0
    count = 0

    for order in orders:
        if not isinstance(order, dict):
            continue

        if order.get("status") != "cancelled":
            amount = order.get("amount", 0)
            try:
                amount = float(amount)
            except (TypeError, ValueError):
                continue

            total += amount
            count += 1

    if count == 0:
        return 0.0

    return total / count

# Do not modify `task1.py`.
