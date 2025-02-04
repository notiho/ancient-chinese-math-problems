"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，斤 b錢 。其 c斤 ，斤 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (斤, "jin") of silk based on the total cost and the total weight. The total weight is given in a combination of units: 石 (shi), 鈞 (jun), 斤 (jin), 兩 (liang), and 銖 (zhu). We need to convert all these units into a single unit (斤) and then compute the price per 斤.

Here is the Python code to compute the values of the unknowns `a`, `b`, `c`, and `d`:


"""

#----- content starts here -----

from fractions import Fraction

# Conversion factors
shi_to_jin = 120  # 1 石 = 120 斤
jun_to_jin = 30   # 1 鈞 = 30 斤
liang_to_jin = Fraction(1, 16)  # 1 兩 = 1/16 斤
zhu_to_jin = Fraction(1, 16 * 24)  # 1 銖 = 1/(16*24) 斤

# Total cost in 錢
total_cost = 13970  # 1 萬三千九百七十 錢

# Total weight in 石, 鈞, 斤, 兩, 銖
total_weight_shi = 1
total_weight_jun = 2
total_weight_jin = 28
total_weight_liang = 3
total_weight_zhu = 5

# Convert total weight to 斤
total_weight_in_jin = (
    total_weight_shi * shi_to_jin +
    total_weight_jun * jun_to_jin +
    total_weight_jin +
    total_weight_liang * liang_to_jin +
    total_weight_zhu * zhu_to_jin
)

# Calculate price per 斤 in 錢
price_per_jin = Fraction(total_cost, total_weight_in_jin)

# Extract integer part (a) and fractional part (b) of the price per 斤
a = price_per_jin.numerator // price_per_jin.denominator  # Integer part
b = price_per_jin - a  # Fractional part

# Convert fractional part to 錢
b = b * price_per_jin.denominator

# Assign c and d (same as a and b for this problem)
c = a
d = b

# Results
a = Fraction(a)
b = Fraction(b)
c = Fraction(c)
d = Fraction(d)

# Output the results
a, b, c, d
#----- content ends here -----


"""


### Explanation:
1. **Unit Conversion**: Convert all weight units to 斤 using the given conversion factors.
2. **Price Calculation**: Divide the total cost by the total weight in 斤 to get the price per 斤.
3. **Integer and Fractional Parts**: Extract the integer part (`a`) and fractional part (`b`) of the price per 斤. The fractional part is converted into 錢.
4. **Assign Variables**: Assign the same values to `c` and `d` as `a` and `b` since the problem states they are the same.

This code computes the values of `a`, `b`, `c`, and `d` as fractions, ensuring accuracy for non-integer results.
"""


"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 67
Variable 'b' has wrong value. Expected: 67, Actual: 7897
Variable 'c' has wrong value. Expected: 7897/384, Actual: 67
Variable 'd' has wrong value. Expected: 68, Actual: 7897"""
