"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：本 a錢 。利 b錢 。
"""

"""
To solve this problem, we will follow the "盈不足術" (Excess and Deficiency Method) as described in the procedure. Let's translate it step by step into Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
返歸 = [14000, 13000, 12000, 11000, 10000]  # Five returns
賈利 = 13  # Profit rate (13%)

# Step 1: 假令本錢三萬，不足一千七百三十八錢半
假本1 = 30000
不足1 = Fraction(1738, 2)

# Step 2: 令之四萬，多三萬五千三百九十錢八分
假本2 = 40000
盈2 = Fraction(35390, 8)

# Step 3: 置所出率，盈、不足各居其下
盈 = 盈2
不足 = 不足1

# Step 4: 令維乘所出率，并以為實
實 = (盈 * 假本1) + (不足 * 假本2)

# Step 5: 并盈、不足為法
法 = 盈 + 不足

# Step 6: 實如法而一
本錢 = Fraction(實, 法)

# Step 7: 有分者，通之 (Simplify the fraction)
本錢 = 本錢.limit_denominator()

# Step 8: 利 = 本錢 * 賈利 / 100
利 = 本錢 * Fraction(賈利, 100)

# Final results
a = 本錢  # 本錢
b = 利    # 利
#----- content ends here -----


"""


### Explanation of the Code:
1. **Initial Assumptions**: We assume two hypothetical principal amounts (`假本1` and `假本2`) and calculate their respective deficiencies (`不足1`) and excesses (`盈2`).
2. **盈不足術**: Using the "Excess and Deficiency Method," we calculate the true principal (`本錢`) by combining the excess and deficiency values proportionally.
3. **利 Calculation**: Once the principal is determined, the profit (`利`) is calculated as 13% of the principal.

### Final Answer:
- 本錢 (`a`) = The true principal amount in 錢.
- 利 (`b`) = The profit amount in 錢.
"""


"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 669890000/21171
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 87085700/21171"""
