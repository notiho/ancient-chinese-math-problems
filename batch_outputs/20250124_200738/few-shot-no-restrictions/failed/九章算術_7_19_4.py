"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：本 a錢 。利 b錢 。
"""

"""
This is a classic "盈不足" (Excess and Deficit) problem, which is a method used in ancient Chinese mathematics to solve problems involving proportional relationships. Let's translate the problem and solution into Python step by step.

---

### Problem:
A person holds an unknown amount of money as capital and earns a profit rate of 13%. They return money in five installments:
- First return: 14,000
- Second return: 13,000
- Third return: 12,000
- Fourth return: 11,000
- Fifth return: 10,000

After these five returns, the total capital and profit are fully repaid. The question is: What is the original capital (本金) and the total profit (利)?

---

### Solution:
The method involves assuming two different initial capital amounts and calculating the excess or deficit for each assumption. Then, the "盈不足術" (Excess and Deficit Method) is used to find the true initial capital.

---

### Python Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# 利率 (profit rate)
profit_rate = Fraction(13, 100)

# 假設本錢 (Assume initial capital)
# 假設1: 本錢 = 30,000
assumed_capital_1 = 30000
returns = [14000, 13000, 12000, 11000, 10000]
total_repaid = sum(returns)

# 計算盈不足 (Excess and Deficit)
# 假設1計算 (Assumption 1 calculation)
profit_1 = assumed_capital_1 * profit_rate
total_1 = assumed_capital_1 + profit_1
deficit_1 = total_1 - total_repaid  # 不足

# 假設2: 本錢 = 40,000
assumed_capital_2 = 40000

# 假設2計算 (Assumption 2 calculation)
profit_2 = assumed_capital_2 * profit_rate
total_2 = assumed_capital_2 + profit_2
excess_2 = total_2 - total_repaid  # 盈

# 盈不足術計算 (Excess and Deficit Method)
# 盈 = 35390.8, 不足 = 1738.5
excess = Fraction(35390, 8)  # Convert to fraction for precision
deficit = Fraction(17385, 10)  # Convert to fraction for precision

# 盈不足術公式
# 本錢 = (假設1 * 盈 + 假設2 * 不足) / (盈 + 不足)
capital = (assumed_capital_1 * excess + assumed_capital_2 * deficit) / (excess + deficit)

# 利 = 本錢 * 利率
profit = capital * profit_rate

# 結果
a = capital
b = profit

print(f"本錢 (Initial Capital): {a} 錢")
print(f"利 (Profit): {b} 錢")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Assumptions**: We assume two different initial capital amounts (30,000 and 40,000) and calculate the total repayment including profit for each assumption.
2. **Excess and Deficit**: For each assumption, calculate the excess or deficit compared to the actual total repayment.
3. **Excess and Deficit Method**: Use the formula to calculate the true initial capital:
   \[
   本錢 = \frac{(假設1 \times 盈) + (假設2 \times 不足)}{盈 + 不足}
   \]
4. **Profit Calculation**: Once the initial capital is determined, calculate the profit using the given profit rate.

---

### Final Answer:
The program will output the initial capital \( a \) and the profit \( b \) in terms of money (錢).
"""


"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 809010000/24649
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 105171300/24649"""
