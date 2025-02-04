"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a翭 ， b翭 一錢 其 c翭 ， d翭 一錢
"""

"""
This problem involves determining the price per unit for two types of goods (in this case, feathers) when the total cost and total quantity are known, but the rates for the two types differ. Let's break it down and encode the solution in Python.

### Problem Breakdown:
- Total money spent: 610 (錢)
- Total feathers purchased: 2100 (翭)
- The goal is to determine the price per unit (貴賤率) for two types of feathers.

The procedure involves reversing the rates (反其率術):
1. Use the total money as the divisor (法).
2. Use the total quantity (2100) as the dividend (實).
3. Divide the dividend by the divisor to determine the rates.
4. If the result is not an integer, adjust the rates by subtracting the remainder from the divisor and increasing the dividend proportionally.

Finally, calculate the number of feathers corresponding to each rate.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Total money and total feathers
total_money = 610  # 錢
total_feathers = 2100  # 翭

# Step 1: Reverse the rate
法 = total_money  # Use total money as the divisor
實 = total_feathers  # Use total feathers as the dividend

# Calculate the base rate (實如法而一)
base_rate = Fraction(實, 法)

# If the base rate is not an integer, adjust
if base_rate.denominator != 1:
    remainder = base_rate.denominator - base_rate.numerator % base_rate.denominator
    法_adjusted = 法 - remainder
    實_adjusted = 實 + remainder
else:
    法_adjusted = 法
    實_adjusted = 實

# Step 2: Calculate the rates for the two types of feathers
貴_rate = Fraction(實_adjusted, 法_adjusted)  # Higher rate
賤_rate = 貴_rate - 1  # Lower rate (1 less than the higher rate)

# Step 3: Calculate the number of feathers for each rate
貴_feathers = 貴_rate * 法_adjusted
賤_feathers = 賤_rate * 法_adjusted

# Output the results
a = 貴_feathers.numerator
b = 貴_feathers.denominator
c = 賤_feathers.numerator
d = 賤_feathers.denominator

print(f"其 {a}翭 ， {b}翭 一錢 其 {c}翭 ， {d}翭 一錢")
#----- content ends here -----


"""


---

### Explanation of Variables:
- `法` (divisor): Total money spent.
- `實` (dividend): Total feathers purchased.
- `貴_rate`: The higher price per feather.
- `賤_rate`: The lower price per feather.
- `貴_feathers`: The number of feathers purchased at the higher rate.
- `賤_feathers`: The number of feathers purchased at the lower rate.

### Output:
The program will output the number of feathers corresponding to each rate and the rate itself in terms of feathers per money unit.
"""


"""
Variable 'a' has wrong value. Expected: 1140, Actual: 2134
Variable 'b' has wrong value. Expected: 3, Actual: 1
Variable 'c' has wrong value. Expected: 960, Actual: 1558
Variable 'd' has wrong value. Expected: 4, Actual: 1"""
