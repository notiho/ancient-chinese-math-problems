"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit (石, 鈞, 斤, 兩) for the given amount of money and silk. Here's the step-by-step breakdown:

### Problem:
- Total money: 13,970 (錢)
- Total silk: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
- We need to calculate the price per 石 and per 鈞.

### Procedure:
1. **Convert all units of silk into 銖 (the smallest unit):**
   - 1 石 = 4 鈞
   - 1 鈞 = 30 斤
   - 1 斤 = 16 兩
   - 1 兩 = 24 銖

   Total silk in 銖:
   ```
   Total 銖 = (1 石 × 4 鈞 × 30 斤 × 16 兩 × 24 銖) 
           + (2 鈞 × 30 斤 × 16 兩 × 24 銖)
           + (28 斤 × 16 兩 × 24 銖)
           + (3 兩 × 24 銖)
           + 5 銖
   ```

2. **Calculate the price per 銖:**
   ```
   Price per 銖 = Total money ÷ Total 銖
   ```

3. **Convert the price per 銖 back to the desired units (石 and 鈞):**
   - Price per 石 = Price per 銖 × (4 鈞 × 30 斤 × 16 兩 × 24 銖)
   - Price per 鈞 = Price per 銖 × (30 斤 × 16 兩 × 24 銖)

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money
錢 = 13970

# Conversion factors
石_to_鈞 = 4
鈞_to_斤 = 30
斤_to_兩 = 16
兩_to_銖 = 24

# Total silk in 銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

total_銖 = (
    石 * 石_to_鈞 * 鈞_to_斤 * 斤_to_兩 * 兩_to_銖 +
    鈞 * 鈞_to_斤 * 斤_to_兩 * 兩_to_銖 +
    斤 * 斤_to_兩 * 兩_to_銖 +
    兩 * 兩_to_銖 +
    銖
)

# Price per 銖
price_per_銖 = Fraction(錢, total_銖)

# Price per 石
price_per_石 = price_per_銖 * (石_to_鈞 * 鈞_to_斤 * 斤_to_兩 * 兩_to_銖)

# Price per 鈞
price_per_鈞 = price_per_銖 * (鈞_to_斤 * 斤_to_兩 * 兩_to_銖)

# Results
a = price_per_石.numerator
b = price_per_石.denominator
c = price_per_鈞.numerator
d = price_per_鈞.denominator

print(f"其 {a} 石 ，兩 {b} 錢 。其 {c} 鈞 ，兩 {d} 錢 。")
#----- content ends here -----


"""


### Explanation of Results:
- `a` and `b` represent the price per 石 in the form of a fraction (a/b).
- `c` and `d` represent the price per 鈞 in the form of a fraction (c/d).
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 643737600
Variable 'b' has wrong value. Expected: 4, Actual: 79949
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 160934400
Variable 'd' has wrong value. Expected: 5, Actual: 79949"""
