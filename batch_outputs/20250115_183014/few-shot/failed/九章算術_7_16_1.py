"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
This is a classic "Excess and Deficiency" (盈不足) problem, where we solve for the amounts of two types of fields (善田 and 惡田) based on their prices and the total cost of a combined purchase. Here's the solution in Python:


"""


"""
Suppose there is good land (善田) worth 300 per mu and poor land (惡田) worth 500 for 7 mu.
Now, buying 1 qing (100 mu) together costs 10,000.
Question: how many mu of good land and poor land are there?

The procedure says:
Assume 20 mu of good land and 80 mu of poor land, resulting in an excess of 1714 and 2/7 qian.
Assume 10 mu of good land and 90 mu of poor land, resulting in a deficit of 571 and 3/7 qian.

The Excess and Deficiency procedure says:
Place the rates of output (所出率), with excess and deficiency each below them.
Multiply the rates by their respective assumptions, summing them to form the dividend (實).
Sum the excess and deficiency to form the divisor (法).
Divide the dividend by the divisor to find the unit amount.
If there are fractions, handle them accordingly.
For the amounts of good and poor land, use the rates of output, subtract the smaller from the larger, and reduce the divisor and dividend proportionally.
The dividend becomes the price of the goods, and the divisor becomes the total number of units.

Answer: *a* mu of good land, *b* mu of poor land.
"""

from fractions import Fraction

# Prices and total cost
善田價 = 300  # per mu
惡田價 = Fraction(500, 7)  # per mu
總價 = 10000  # total cost for 1 qing (100 mu)

# Assumptions and results
善田假設1 = 20  # mu
惡田假設1 = 80  # mu
盈1 = Fraction(1714, 1) + Fraction(2, 7)  # excess

善田假設2 = 10  # mu
惡田假設2 = 90  # mu
不足2 = Fraction(571, 1) + Fraction(3, 7)  # deficiency

# 盈不足術 calculations
# Rates of output (所出率)
所出率1 = 善田假設1 * 善田價 + 惡田假設1 * 惡田價
所出率2 = 善田假設2 * 善田價 + 惡田假設2 * 惡田價

# Dividend (實)
實 = 盈1 * 所出率2 + 不足2 * 所出率1

# Divisor (法)
法 = 盈1 + 不足2

# Unit amount (善田數量)
善田數量 = 實 / 法

# Calculate 善田 and 惡田
a = 善田數量
b = 100 - a  # Total mu is 100 (1 qing)

# Output the results
a, b


"""


### Explanation of the Code:
1. **Input Data**: The prices of good and poor land, the total cost, and the assumptions for the two scenarios (善田假設1, 惡田假設1, etc.).
2. **Excess and Deficiency**: The excess (盈1) and deficiency (不足2) are calculated based on the assumptions.
3. **Rates of Output**: The total cost for each assumption is calculated using the prices and assumptions.
4. **盈不足術**: The procedure is applied to calculate the unit amount (善田數量).
5. **善田 and 惡田**: Using the unit amount, the number of mu for good and poor land is calculated.

### Final Answer:
The values of `a` (善田) and `b` (惡田) will give the number of mu for good and poor land, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 10000
Variable 'b' has wrong value. Expected: 175/2, Actual: -9900"""
