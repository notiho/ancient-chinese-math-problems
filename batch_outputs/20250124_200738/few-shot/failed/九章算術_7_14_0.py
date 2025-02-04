"""
今有漆三得油四，油四和漆五。今有漆三斗，欲令分以易油，還自和餘漆。問︰出漆、得油、和漆各幾何？
術曰：假令出漆九升，不足六升。令之出漆一斗二升，有餘二升。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：出漆 a斗 ，得油 b斗 ，和漆 c斗 ， d升 。
"""

"""
This problem involves a mixture of proportional exchange and reconciliation of surplus and deficit. Let's break it down step by step and encode the procedure in Python.

### Problem Breakdown:
1. **Given Ratios:**
   - 3 dou of lacquer yields 4 dou of oil.
   - 4 dou of oil mixes with 5 dou of lacquer.

2. **Task:**
   - Start with 3 dou of lacquer.
   - Exchange lacquer for oil according to the given ratio.
   - Reconcile the remaining lacquer with the oil to form a mixture.

3. **Procedure:**
   - Use the "盈不足術" (Surplus and Deficit Method) to calculate the amounts exchanged and reconciled.

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# 漆三得油四，油四和漆五
漆出率 = Fraction(3)  # 3 dou of lacquer
油得率 = Fraction(4)  # yields 4 dou of oil
油和率 = Fraction(4)  # 4 dou of oil
漆和率 = Fraction(5)  # mixes with 5 dou of lacquer

# 今有漆三斗
漆初始 = Fraction(3)  # 3 dou of lacquer initially

# Step 1: Calculate the amount of oil obtained by exchanging lacquer
# 漆三得油四 -> 漆初始 * (油得率 / 漆出率)
得油 = 漆初始 * (油得率 / 漆出率)

# Step 2: Calculate the amount of lacquer used for mixing with the obtained oil
# 油四和漆五 -> 得油 * (漆和率 / 油和率)
和漆 = 得油 * (漆和率 / 油和率)

# Step 3: Calculate the remaining lacquer after mixing
# 漆初始 - 和漆
餘漆 = 漆初始 - 和漆

# Step 4: Combine the remaining lacquer with the mixture
# 和漆 + 餘漆
總和漆 = 和漆 + 餘漆

# Convert results to dou and sheng (1 dou = 10 sheng)
a = 漆初始  # 出漆 (initial lacquer used for exchange)
b = 得油  # 得油 (oil obtained)
c = 總和漆.numerator // 總和漆.denominator  # 和漆 in dou
d = (總和漆 - c) * 10  # 和漆 in sheng

# Output results
a斗 = a
b斗 = b
c斗 = c
d升 = d

print(f"出漆 {a斗}斗 ，得油 {b斗}斗 ，和漆 {c斗}斗 ， {d升}升 。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Ratios and Initial Values:**
   - The ratios for lacquer-to-oil exchange and oil-to-lacquer mixing are represented as fractions for precise calculations.
   - The initial amount of lacquer is set to 3 dou.

2. **Step-by-Step Calculations:**
   - The amount of oil obtained (`得油`) is calculated using the lacquer-to-oil exchange ratio.
   - The amount of lacquer used for mixing (`和漆`) is calculated using the oil-to-lacquer mixing ratio.
   - The remaining lacquer (`餘漆`) is the difference between the initial lacquer and the lacquer used for mixing.
   - The total lacquer in the mixture (`總和漆`) is the sum of the lacquer used for mixing and the remaining lacquer.

3. **Conversion to Dou and Sheng:**
   - The results are converted to dou and sheng for proper representation, as 1 dou = 10 sheng.

### Final Answer:
The output will provide the amounts of lacquer exchanged, oil obtained, and the final mixture in dou and sheng.
"""


"""
Variable 'a' has wrong value. Expected: 9/8, Actual: 3
Variable 'b' has wrong value. Expected: 3/2, Actual: 4
Variable 'c' has wrong value. Expected: 9/5, Actual: 3
Variable 'd' has wrong value. Expected: 3/4, Actual: 0"""
