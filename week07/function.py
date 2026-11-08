
# --- Self-Assessment ---

# 1. The first bug I noticed was that the total wasn't
# adding up correctly. I did not add everthing up first, but instea i replaced the prvious number.when i slowed down to actually read the code i realized,
#I need to use += instead of =. This showed me that code may seem complicated but i when i actually read each line
# recognize some errors simply.

# 2. It takes the original price and the customer's membership tier,. It also does a price that then returns the new
# price after the discount.

# 3. AI Disclosure:
# I used ChatGPT to help explain the errors in Exercise 5. It helped me understand how the functions work and
# why certain changes were needed.


# --- Exercise 1 Calculate tax---

def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2  Apply discount based on membership tier---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(200, tier):.2f}")


# --- Exercise 3 Combine discount and tax---

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
total = discounted + tax

print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${total:.2f}")

def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax_amount = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax_amount

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# --- Exercise 4 Loop through orders and print a sales report---

orders = [(200, "gold"), (150, "silver"),
          (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5  Debug broken_sales.py---

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    # Changed = to += so the sales add together.
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    # Added the missing colon to fix the syntax error.
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    # Changed <= to < so the loop stays within the list.
    print(sales[i])
    i += 1


# --- Exercise 6 Scope experiment---

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)

# The first and last print statements show 100
# because x is a global variable and hasn't changed.
# The local variable doesn't change the global one.
