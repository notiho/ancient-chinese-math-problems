"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
術曰：假令善田二十畝，惡田八十畝，多一千七百一十四錢、七分錢之二。令之善田一十畝，惡田九十畝，不足五百七十一錢、七分錢之三。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
This is a classic "excess and deficiency" (盈不足) problem in ancient Chinese mathematics. Let's translate the problem and the procedure into Python code step by step.

### Problem:
We have:
- Good land (善田): 1 mu costs 300 qian.
- Poor land (惡田): 7 mu costs 500 qian.
- Total land to buy: 1 qing (100 mu).
- Total cost: 10,000 qian.

Question: How many mu of good land and poor land are bought?

### Procedure:
The "excess and deficiency" method (盈不足術) is used:
1. Assume two different distributions of good and poor land.
2. Calculate the total cost for each assumption.
3. Determine the excess or deficiency of each assumption compared to the target cost.
4. Use the excess and deficiency method to find the correct distribution.

### Python Code:

"""


from fractions import Fraction

# Known values
善田價 = 300  # Good land price per mu
惡田價 = Fraction(500, 7)  # Poor land price per mu
總地 = 100  # Total land in mu
總價 = 10000  # Total price in qian

# Assumptions
# 假令善田二十畝，惡田八十畝
善田_假1 = 20
惡田_假1 = 總地 - 善田_假1
價值_假1 = 善田_假1 * 善田價 + 惡田_假1 * 惡田價
盈1 = 價值_假1 - 總價  # 多一千七百一十四錢、七分錢之二
盈1 = Fraction(1714, 1) + Fraction(2, 7)

# 令之善田一十畝，惡田九十畝
善田_假2 = 10
惡田_假2 = 總地 - 善田_假2
價值_假2 = 善田_假2 * 善田價 + 惡田_假2 * 惡田價
不足2 = 總價 - 價值_假2  # 不足五百七十一錢、七分錢之三
不足2 = Fraction(571, 1) + Fraction(3, 7)

# 盈不足術
# 置所出率，盈、不足各居其下
所出率1 = 善田_假1 - 善田_假2  # Difference in good land between assumptions
所出率2 = 善田_假2 - 善田_假1  # Negative of the above

# 令維乘所出率，并以為實
實 = 盈1 * 所出率2 + 不足2 * 所出率1

# 并盈、不足為法
法 = 盈1 + 不足2

# 實如法而一
善田 = 實 / 法

# 惡田
惡田 = 總地 - 善田

# Output
a = 善田
b = 惡田

print(f"善田: {a} 畝")
print(f"惡田: {b} 畝")


"""


### Explanation of the Code:
1. **Assumptions**: We assume two different distributions of good and poor land (20 mu good, 80 mu poor; and 10 mu good, 90 mu poor).
2. **Calculate Excess and Deficiency**: For each assumption, calculate the total cost and determine how much it exceeds or falls short of the target cost.
3. **Excess and Deficiency Method**: Use the differences in assumptions and the corresponding excess/deficiency values to calculate the correct distribution of good and poor land.
4. **Output**: The result gives the number of mu of good land (`a`) and poor land (`b`).

### Final Answer:
The values of `a` (善田) and `b` (惡田) will be calculated and printed as fractions or decimals.
"""


"""
Variable 'a' has wrong value. Expected: 25/2, Actual: -5
Variable 'b' has wrong value. Expected: 175/2, Actual: 105"""
