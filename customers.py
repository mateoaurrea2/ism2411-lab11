# Reflection
# 1. I'd use .get() any time a key might not be there, like optional fields
#    or customer data that isn't complete, since it gives a default instead of
#    crashing. Bracket notation is better when the key should always exist,
#    because if it's missing, I want the error so I know something's wrong.
#    My rule of thumb: .get() if missing is normal, brackets if missing is a bug.
#
# 2. This is basically SUMIF or a pivot table in Excel, adding up totals by
#    category. The Python version is more useful for big datasets because it can
#    handle way more rows without slowing down, and once it's written I can
#    rerun it on new data without rebuilding anything by hand.
# Exercise 1: one customer
customer = {
    "name": "Jordan Lee",
    "email": "jordan@example.com",
    "tier": "gold",
    "ytd_spend": 1250.75,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2: update and add
customer["phone"] = "813-555-0142"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# Exercise 3: safe lookup
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as e:
    print("KeyError:", e)
    for key, value in customer.items():
     print(f"{key}: {value}")

for key in customer:
    print(key)
# Without .items(), looping over a dict only gives you the keys.
# To get the value you'd have to look it up yourself with customer[key].
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
final_price = 200 * (1 - discount)

print(f"Tier: {tier}")
print(f"Discount: {discount:.0%}")
print(f"Final price: ${final_price:.2f}")
customers = [
    customer,
    {"name": "Ava Patel", "tier": "silver"},
    {"name": "Sam Chen", "tier": "bronze"},
]

for c in customers:
    discount_amount = 300 * tier_discounts.get(c["tier"], 0)
    print(f"{c['name']} | {c['tier']} | ${discount_amount:.2f} off")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} ({info['stock']} left)")
