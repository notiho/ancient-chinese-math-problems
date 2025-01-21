"""
今有善田一畝價三百惡田七畝價五百今并買一頃價錢一萬問善惡田各幾何
術曰假令善田二十畝惡田八十畝多一千七百一十四錢七分錢之二令之善田一十畝惡田九十畝不足五百七十一錢七分錢之三
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰善田 a畝 惡田 b畝 
"""

"""
Suppose there is good farmland, 1 mu of which costs 300 qian, and poor farmland, 7 mu of which costs 500 qian.
Now, buying 1 qing of land (100 mu) costs 10,000 qian.
Question: how many mu of good farmland and poor farmland are there respectively?

The procedure for the "Excess and Deficit" method says:
1. Assume 20 mu of good farmland and 80 mu of poor farmland. This exceeds the cost by 1714 qian and 2/7 of a qian.
2. Assume 10 mu of good farmland and 90 mu of poor farmland. This falls short by 571 qian and 3/7 of a qian.
3. Place the rates of excess and deficit below their respective assumptions.
4. Multiply the assumptions by their respective rates, then add these to form the dividend.
5. Add the excess and deficit rates to form the divisor.
6. Divide the dividend by the divisor to find the result. If there is a fraction, convert it.
7. Subtract the smaller assumption from the larger, and use this difference to simplify the divisor and dividend.
8. The result gives the number of good farmland mu. Subtract this from the total mu to find the number of poor farmland mu.

Answer: *a* mu of good farmland, *b* mu of poor farmland.
"""

from fractions import Fraction

# Step 1: Initial assumptions and their outcomes
善田_假設1 = 20  # First assumption: 20 mu of good farmland
惡田_假設1 = 80  # First assumption: 80 mu of poor farmland
盈1 = Fraction(1714, 7)  # Excess by 1714 qian and 2/7 qian

善田_假設2 = 10  # Second assumption: 10 mu of good farmland
惡田_假設2 = 90  # Second assumption: 90 mu of poor farmland
不足2 = Fraction(571, 7)  # Deficit by 571 qian and 3/7 qian

# Step 2: Calculate the rates (盈 and 不足)
盈率 = 盈1
不足率 = 不足2

# Step 3: Multiply assumptions by their respective rates and sum them
實 = (善田_假設1 * 盈率) + (善田_假設2 * 不足率)

# Step 4: Add the rates to form the divisor
法 = 盈率 + 不足率

# Step 5: Divide the dividend by the divisor to find the number of good farmland mu
善田 = 實 / 法

# Step 6: Subtract the number of good farmland mu from the total to find poor farmland mu
惡田 = 100 - 善田

# Final Answer
a = 善田
b = 惡田
"""
Variable 'a' has wrong value. Expected: 25/2, Actual: 7998/457
Variable 'b' has wrong value. Expected: 175/2, Actual: 37702/457"""
