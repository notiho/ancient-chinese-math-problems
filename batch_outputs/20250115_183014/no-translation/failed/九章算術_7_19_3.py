"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：本 a錢 。利 b錢 。
"""

"""
To solve this problem, we will follow the "盈不足術" (Excess and Deficiency Method) as described. Here's the step-by-step Python implementation:


"""


from fractions import Fraction

# 假令本錢三萬，不足一千七百三十八錢半
假本1 = 30000
不足1 = Fraction(1738, 2)

# 令之四萬，多三萬五千三百九十錢八分
假本2 = 40000
多2 = Fraction(35390, 8)

# 置所出率，盈、不足各居其下
盈 = 多2
不足 = 不足1

# 令維乘所出率，并以為實
實 = 假本1 * 盈 + 假本2 * 不足

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
本錢 = Fraction(實, 法)

# 利 = 五次返歸總和 - 本錢
五次返歸總和 = 14000 + 13000 + 12000 + 11000 + 10000
利 = 五次返歸總和 - 本錢

# 答案
a = 本錢
b = 利

# Output results
a, b


"""


### Explanation of the Code:
1. **假本 and 盈不足**:
   - We assume two hypothetical principal amounts (`假本1` and `假本2`) and calculate the deficiency (`不足1`) and excess (`多2`) based on the problem's description.

2. **盈不足術**:
   - Following the method, we calculate the "實" (numerator) by multiplying the hypothetical principals by their respective excess or deficiency and summing them.
   - The "法" (denominator) is the sum of the excess and deficiency.

3. **Calculate 本錢**:
   - The true principal (`本錢`) is obtained by dividing the numerator (`實`) by the denominator (`法`).

4. **Calculate 利**:
   - The total profit (`利`) is the difference between the total amount returned over five trips and the principal.

### Final Answer:
- `a` is the principal (`本錢`).
- `b` is the profit (`利`).
"""


"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 669890000/21171
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 600370000/21171"""
