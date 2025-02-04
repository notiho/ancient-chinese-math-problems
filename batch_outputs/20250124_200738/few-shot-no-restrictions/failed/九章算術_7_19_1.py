"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：本 a錢 。利 b錢 。
"""

"""
This is a classic "盈不足" (Excess and Deficiency) problem from ancient Chinese mathematics. The problem involves determining the principal amount of money (本金) and the profit (利) based on multiple returns and a fixed profit rate.

Let's break it down and solve it step by step in Python:

---

### Problem Breakdown:
1. A person invests money with a profit rate of 13%.
2. The returns are as follows:
   - First return: 14,000
   - Second return: 13,000
   - Third return: 12,000
   - Fourth return: 11,000
   - Fifth return: 10,000
3. The total principal and profit are exhausted after these five returns.
4. We are tasked to find:
   - The principal amount (本金)
   - The total profit (利)

The **盈不足術** (Excess and Deficiency method) is used to solve this problem.

---

### Procedure:
1. Assume an initial principal amount (e.g., 30,000).
2. Calculate the total return based on the profit rate (13%).
3. Compare the calculated total return with the actual total return (sum of the five returns).
   - If the calculated return is less than the actual return, record the deficiency (不足).
   - If the calculated return is more than the actual return, record the excess (盈).
4. Adjust the principal amount and repeat until the correct principal is found.
5. Use the formula from the **盈不足術** to calculate the exact principal and profit.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
profit_rate = Fraction(13, 100)  # 13% profit rate
returns = [14000, 13000, 12000, 11000, 10000]  # Five returns
total_return = sum(returns)  # Total return

# Assumed principals and their results
assumed_principal_1 = 30000  # First assumption
assumed_principal_2 = 40000  # Second assumption

# Calculate the total return for the first assumption
calculated_return_1 = assumed_principal_1 * (1 + profit_rate)

# Calculate the total return for the second assumption
calculated_return_2 = assumed_principal_2 * (1 + profit_rate)

# Calculate the deficiency (不足) and excess (盈)
不足 = total_return - calculated_return_1
盈 = calculated_return_2 - total_return

# Use the 盈不足術 formula to calculate the exact principal
法 = 盈 + 不足
實 = 盈 * assumed_principal_1 + 不足 * assumed_principal_2
principal = 實 / 法

# Calculate the profit
profit = principal * profit_rate

# Output the results
a = principal
b = profit

print(f"本 (Principal): {a} 錢")
print(f"利 (Profit): {b} 錢")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Profit Rate**: The profit rate is given as 13%, which is represented as a fraction (`Fraction(13, 100)`).
2. **Returns**: The five returns are summed up to get the total return.
3. **Assumed Principals**: Two initial guesses for the principal are made (30,000 and 40,000).
4. **盈不足術 Formula**:
   - `法 = 盈 + 不足`
   - `實 = 盈 * assumed_principal_1 + 不足 * assumed_principal_2`
   - `principal = 實 / 法`
5. **Profit Calculation**: Once the principal is found, the profit is calculated using the profit rate.

---

### Output:
The program will output the principal (`a`) and the profit (`b`) in terms of 錢.
"""


"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 6000000/113
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 780000/113"""
