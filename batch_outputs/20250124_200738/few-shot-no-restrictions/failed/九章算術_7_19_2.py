"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：本 a錢 。利 b錢 。
"""

"""
This is a classic "盈不足術" (Excess and Deficiency Method) problem from ancient Chinese mathematics. Let's break it down and solve it step by step using Python.

### Problem Description:
A person holds an unknown amount of money (本金, principal) and earns a profit rate of 13%. Over five transactions, they return decreasing amounts of money: 14,000, 13,000, 12,000, 11,000, and 10,000. By the end of the five transactions, both the principal and the profit are fully returned. The question is: What are the original principal (本金) and the total profit (利)?

The solution involves the "盈不足術" (Excess and Deficiency Method), which is a systematic way to solve problems involving proportional relationships.

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# 利率 (profit rate)
profit_rate = Fraction(13, 100)  # 13%

# 假設本金 (assume initial principal)
假本1 = 30000  # First assumption: 30,000
假本2 = 40000  # Second assumption: 40,000

# 計算盈不足 (calculate excess and deficiency)
# 假本1: 不足 1738.5
不足 = 1738 + Fraction(1, 2)

# 假本2: 盈 35390.8
盈 = 35390 + Fraction(8, 10)

# 盈不足術計算
# 盈不足術公式:
# 本金 = 假本1 + (不足 / (盈 + 不足)) * (假本2 - 假本1)

本金 = 假本1 + (不足 / (盈 + 不足)) * (假本2 - 假本1)

# 計算利 (profit)
# 利 = 本金 * 利率
利 = 本金 * profit_rate

# 結果
a = 本金
b = 利

print(f"本金 (Principal): {a} 錢")
print(f"利 (Profit): {b} 錢")
#----- content ends here -----


"""


---

### Explanation of the Code:

1. **Profit Rate**: The profit rate is given as 13%, which is represented as a fraction (`Fraction(13, 100)`).

2. **Assumptions**: Two initial guesses for the principal are made: 30,000 and 40,000.

3. **Excess and Deficiency**: Based on the problem, the first assumption (30,000) results in a deficiency of 1,738.5, and the second assumption (40,000) results in an excess of 35,390.8.

4. **Excess and Deficiency Method**: The formula for the principal is derived from the excess and deficiency method:
   \[
   本金 = 假本1 + \frac{不足}{盈 + 不足} \times (假本2 - 假本1)
   \]

5. **Profit Calculation**: Once the principal is calculated, the profit is determined by multiplying the principal by the profit rate.

---

### Final Answer:
The program will output the values of the principal (`a`) and the profit (`b`) in terms of ancient Chinese currency units (錢).
"""


"""
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 113126400/28561"""
