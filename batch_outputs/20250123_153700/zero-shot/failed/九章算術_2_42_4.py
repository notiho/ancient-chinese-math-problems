"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit of weight for the silk. The total cost is 13,970 (錢), and the total weight is 1石 2鈞 28斤 3兩 5銖. We will compute the price per 石 (a), per 鈞 (c), and their respective 錢 (b and d).

### Step-by-step breakdown:
1. Convert the total weight into a single unit (銖) for easier calculations:
   - 1石 = 4鈞
   - 1鈞 = 30斤
   - 1斤 = 16兩
   - 1兩 = 24銖

   Total weight in 銖:
   ```
   total_weight_銖 = (1石 * 4鈞/石 * 30斤/鈞 * 16兩/斤 * 24銖/兩) +
                     (2鈞 * 30斤/鈞 * 16兩/斤 * 24銖/兩) +
                     (28斤 * 16兩/斤 * 24銖/兩) +
                     (3兩 * 24銖/兩) +
                     5銖
   ```

2. Compute the price per 銖:
   ```
   price_per_銖 = total_cost / total_weight_銖
   ```

3. Convert the price per 銖 back to the desired units:
   - Price per 石 (a, b): Multiply price_per_銖 by the number of 銖 in 1石, then separate into 錢 and 銖.
   - Price per 鈞 (c, d): Multiply price_per_銖 by the number of 銖 in 1鈞, then separate into 錢 and 銖.

### Python Code:

"""


from fractions import Fraction

# Given data
total_cost = 13970  # in 錢

# Conversion factors
銖_per_兩 = 24
兩_per_斤 = 16
斤_per_鈞 = 30
鈞_per_石 = 4

# Total weight in 銖
total_weight_銖 = (
    (1 * 鈞_per_石 * 斤_per_鈞 * 兩_per_斤 * 銖_per_兩) +  # 1石
    (2 * 斤_per_鈞 * 兩_per_斤 * 銖_per_兩) +              # 2鈞
    (28 * 兩_per_斤 * 銖_per_兩) +                        # 28斤
    (3 * 銖_per_兩) +                                    # 3兩
    5                                                   # 5銖
)

# Price per 銖
price_per_銖 = Fraction(total_cost, total_weight_銖)

# Price per 石 (a, b)
銖_per_石 = 鈞_per_石 * 斤_per_鈞 * 兩_per_斤 * 銖_per_兩
price_per_石 = price_per_銖 * 銖_per_石
a = price_per_石.numerator // price_per_石.denominator  # 錢
b = price_per_石 - a  # Remaining 銖

# Price per 鈞 (c, d)
銖_per_鈞 = 斤_per_鈞 * 兩_per_斤 * 銖_per_兩
price_per_鈞 = price_per_銖 * 銖_per_鈞
c = price_per_鈞.numerator // price_per_鈞.denominator  # 錢
d = price_per_鈞 - c  # Remaining 銖

# Results
a, b, c, d


"""


### Explanation of Variables:
- `a`: Price per 石 in 錢
- `b`: Remaining 銖 for price per 石
- `c`: Price per 鈞 in 錢
- `d`: Remaining 銖 for price per 鈞

This code calculates the values of `a`, `b`, `c`, and `d` based on the given problem.
"""


"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 8051
Variable 'b' has wrong value. Expected: 4, Actual: 68201/79949
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 2012
Variable 'd' has wrong value. Expected: 5, Actual: 77012/79949"""
