# DRY means avoid duplicating code or logic.
# Each piece of knowledge or rule should exist in one place in the system so that if you need to change it, 
# you change it only once.

# When you copy-paste logic, you create multiple “versions” of the same rule. 
# Later, if the rule changes, you must fix it in all places — and missing even one causes bugs.
# DRY centralizes logic into one function, class, or module. 
# This makes maintenance easier, reduces bugs, and keeps code cleaner.

# Bad way
def price_small_order(qty, unit_price):
    sub = qty * unit_price
    tax = sub * 0.18
    return sub + tax

def price_bulk_order(qty, unit_price):
    sub = qty * unit_price
    disc = sub * 0.05 if qty >= 10 else 0
    tax = (sub - disc) * 0.18
    return sub - disc + tax

# DRY -> Good Way
def compute_total(qty, unit_price):
    sub = qty * unit_price
    disc = sub * 0.05 if qty >= 10 else 0
    tax = (sub - disc) * 0.18
    return sub, disc, tax, sub - disc + tax

o1 = compute_total(3, 100)
o2 = compute_total(15, 100)

for sub, disc, tax, total in (o1, o2):
    print(f"Subtotal={sub:.2f}, Discount={disc:.2f}, Tax={tax:.2f}, Total={total:.2f}")
