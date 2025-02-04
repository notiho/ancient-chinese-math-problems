"""
今有善田一畝價三百惡田七畝價五百今并買一頃價錢一萬問善惡田各幾何
術曰假令善田二十畝惡田八十畝多一千七百一十四錢七分錢之二令之善田一十畝惡田九十畝不足五百七十一錢七分錢之三
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰善田 a畝 惡田 b畝 
"""

#----- content starts here -----
"""
Suppose there is good farmland, 1 mu of which is worth 300 qian, and poor farmland, 7 mu of which is worth 500 qian.
Now, buying 1 qing (100 mu) of land together costs 10,000 qian.
Question: how many mu of good farmland and poor farmland are there respectively?

The procedure says: Suppose there are 20 mu of good farmland and 80 mu of poor farmland. This exceeds the total by 1714 qian and 2/7 of a qian.
Suppose there are 10 mu of good farmland and 90 mu of poor farmland. This falls short of the total by 571 qian and 3/7 of a qian.

The "Excess and Deficit" procedure says: Place the rates of output corresponding to the excess and deficit below them.
Multiply the rates of output by the excess and deficit, and sum them to form the dividend.
Sum the excess and deficit to form the divisor.
Divide the dividend by the divisor. If there is a fraction, simplify it.
The excess and deficit are then used to determine the quantities of the items being purchased.
Place the rates of output, subtract the smaller from the larger, and reduce the divisor and dividend accordingly.
The resulting dividend is the price of the items, and the divisor is the total number of items.

Answer: *a* mu of good farmland, *b* mu of poor farmland.
"""

from fractions import Fraction

# Rates and values
善田價 = 300  # Good farmland price per mu
惡田價 = Fraction(500, 7)  # Poor farmland price per mu
總價 = 10000  # Total price for 1 qing (100 mu)

# Hypothetical scenarios
善田_假1 = 20  # Good farmland in first scenario
惡田_假1 = 80  # Poor farmland in first scenario
超過_假1 = Fraction(1714, 1) + Fraction(2, 7)  # Excess in first scenario

善田_假2 = 10  # Good farmland in second scenario
惡田_假2 = 90  # Poor farmland in second scenario
不足_假2 = Fraction(571, 1) + Fraction(3, 7)  # Deficit in second scenario

# 盈不足術
# Step 1: Multiply rates of output by excess and deficit, and sum them
實 = (善田_假1 * 超過_假1) + (善田_假2 * 不足_假2)

# Step 2: Sum the excess and deficit to form the divisor
法 = 超過_假1 + 不足_假2

# Step 3: Divide the dividend by the divisor to find the amount of good farmland
善田 = Fraction(實, 法)

# Step 4: Calculate the amount of poor farmland
惡田 = 100 - 善田

# Final answer
a = 善田
b = 惡田#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 35/2
Variable 'b' has wrong value. Expected: 175/2, Actual: 165/2"""
