"""
今有出錢五百七十六，買竹七十八箇。欲其大小率之，問︰各幾何？
荅曰：其 a箇 ，箇 b錢 。其 c箇 ，箇 d錢 。
"""

"""
Suppose there is a total of 576 qian (coins) used to buy 78 bamboo pieces. 
The bamboo pieces are of two types: large and small. 
The price per piece for the large and small bamboo pieces is different. 
Question: How many pieces of each type, and what is the price per piece for each type?

Answer: There are *a* pieces, each costing *b* qian, and *c* pieces, each costing *d* qian.
"""

# Total money and total bamboo pieces
total_money = 576
total_bamboo = 78

# Assume the price of the large bamboo is 9 qian per piece, and the price of the small bamboo is 7 qian per piece.
price_large = 9
price_small = 7

# Let the number of large bamboo pieces be `a`, and the number of small bamboo pieces be `c`.
# Solve the system of equations:
# a + c = total_bamboo
# a * price_large + c * price_small = total_money

# Using substitution:
# c = total_bamboo - a
# a * price_large + (total_bamboo - a) * price_small = total_money

# Simplify:
# a * price_large + total_bamboo * price_small - a * price_small = total_money
# a * (price_large - price_small) = total_money - total_bamboo * price_small
# a = (total_money - total_bamboo * price_small) / (price_large - price_small)

a = (total_money - total_bamboo * price_small) // (price_large - price_small)
c = total_bamboo - a

# Calculate the price per piece for each type
b = price_large
d = price_small

# Output the results
a, b, c, d
"""
Variable 'a' has wrong value. Expected: 48, Actual: 15
Variable 'b' has wrong value. Expected: 7, Actual: 9
Variable 'c' has wrong value. Expected: 30, Actual: 63
Variable 'd' has wrong value. Expected: 8, Actual: 7"""
