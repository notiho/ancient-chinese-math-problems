"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，斤 b錢 。其 c石 ，斤 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (斤) for silk. The total weight is given as 1石2鈞18斤, and the total cost is 1120錢. The problem asks us to compute the price per 斤 for two different units: 鈞 and 石.

Here is the Python code to compute the values of the unknowns `a`, `b`, `c`, and `d`:


"""

#----- content starts here -----

from fractions import Fraction

# Total cost in 錢
total_cost = 1120

# Conversion factors
斤_per_鈞 = 30  # 1 鈞 = 30 斤
斤_per_石 = 120  # 1 石 = 120 斤

# Total weight in 斤
total_weight_石 = 1 * 斤_per_石  # 1 石
total_weight_鈞 = 2 * 斤_per_鈞  # 2 鈞
total_weight_斤 = 18  # 18 斤
total_weight = total_weight_石 + total_weight_鈞 + total_weight_斤

# Price per 斤
price_per_斤 = Fraction(total_cost, total_weight)

# Price per 鈞 (a 鈞, b 錢)
price_per_鈞 = price_per_斤 * 斤_per_鈞
a = price_per_鈞.numerator
b = price_per_鈞.denominator

# Price per 石 (c 石, d 錢)
price_per_石 = price_per_斤 * 斤_per_石
c = price_per_石.numerator
d = price_per_石.denominator

# Results
a, b, c, d
#----- content ends here -----


"""


### Explanation:
1. **Conversion Factors**:
   - 1 鈞 = 30 斤
   - 1 石 = 120 斤

2. **Total Weight**:
   - The total weight is calculated by converting 石, 鈞, and 斤 into 斤 and summing them up.

3. **Price per 斤**:
   - The price per 斤 is calculated by dividing the total cost by the total weight.

4. **Price per 鈞 and 石**:
   - The price per 鈞 is obtained by multiplying the price per 斤 by the number of 斤 in a 鈞.
   - Similarly, the price per 石 is obtained by multiplying the price per 斤 by the number of 斤 in a 石.

5. **Output**:
   - The results are stored in variables `a`, `b`, `c`, and `d`, representing the numerator and denominator of the prices per 鈞 and 石, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 5600
Variable 'b' has wrong value. Expected: 5, Actual: 33
Variable 'c' has wrong value. Expected: 13/12, Actual: 22400
Variable 'd' has wrong value. Expected: 6, Actual: 33"""
