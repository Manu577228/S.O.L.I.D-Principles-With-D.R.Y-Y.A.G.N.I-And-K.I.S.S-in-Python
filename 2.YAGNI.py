# YAGNI - You Aren’t Gonna Need It

# YAGNI means don’t build features you don’t need right now.
# Implement only what is required for current requirements, not hypothetical future ones.

# Adding features “just in case” makes code harder to maintain and increases bugs. 
# You may never use them, and by the time you need them, the requirements might have changed.
# YAGNI helps keep code focused, small, and easy to change when real needs arise.


# Bad Way
def compute_total_with_points(qty, unit_price, loyalty_points=False):
    sub = qty * unit_price
    tax = sub * 0.18
    total = sub + tax
    if loyalty_points:
        points = int(total // 10) # This is not needed now. This just adds complexity
        print(f"Loyalty points: {points}")
    return total


# Good Way
def compute_total(qty, unit_price):
    sub = qty * unit_price
    tax = sub * 0.18
    return sub + tax

t1 = compute_total(3, 100)
t2 = compute_total(15, 100)
print(f"Order1 Total: {t1}")
print(f"Order2 total: {t2}")





