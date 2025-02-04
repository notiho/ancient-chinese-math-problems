"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：本 a錢 。利 b錢 。
"""

"""
This is a classic "盈不足術" (Excess and Deficiency Method) problem from ancient Chinese mathematics. The problem involves determining the principal amount of money (本金) and the total profit (利) based on the returns from multiple transactions.

Let's break it down and solve it step by step using Python:

---

### Problem:
A person holds an unknown amount of principal money and earns a profit rate of 13%. They return money in five installments:
- First return: 14,000
- Second return: 13,000
- Third return: 12,000
- Fourth return: 11,000
- Fifth return: 10,000

The total of these five returns equals the principal plus the profit. The goal is to find the principal (本金) and the profit (利).

The procedure uses the "盈不足術" (Excess and Deficiency Method). Here's how it works:
1. Assume two trial values for the principal.
2. Calculate the excess or deficiency for each trial value.
3. Use the excess and deficiency to calculate the true value of the principal.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
profit_rate = Fraction(13, 100)  # 13% profit rate
returns = [14000, 13000, 12000, 11000, 10000]  # Five returns
total_returns = sum(returns)  # Total money returned

# Step 1: Assume two trial values for the principal
trial_1 = 30000  # First trial value
trial_2 = 40000  # Second trial value

# Step 2: Calculate the total amount (principal + profit) for each trial
total_1 = trial_1 + trial_1 * profit_rate  # Total for trial 1
total_2 = trial_2 + trial_2 * profit_rate  # Total for trial 2

# Step 3: Calculate the excess or deficiency for each trial
excess_1 = total_1 - total_returns  # Excess for trial 1
excess_2 = total_2 - total_returns  # Excess for trial 2

# Step 4: Use the "盈不足術" formula to calculate the true principal
# Formula: (trial_1 * excess_2 - trial_2 * excess_1) / (excess_2 - excess_1)
principal = (trial_1 * excess_2 - trial_2 * excess_1) / (excess_2 - excess_1)

# Step 5: Calculate the profit
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
2. **Returns**: The five returns are summed to get the total amount of money returned.
3. **Trial Values**: Two trial values for the principal are assumed (30,000 and 40,000).
4. **Excess/Deficiency**: For each trial value, the total amount (principal + profit) is calculated and compared to the total returns to find the excess or deficiency.
5. **盈不足術 Formula**: The formula is applied to calculate the true principal based on the trial values and their respective excess/deficiency.
6. **Profit Calculation**: The profit is calculated as the principal multiplied by the profit rate.

---

### Output:
The program will output the principal (`a`) and the profit (`b`) in terms of money (`錢`).
"""


"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 6000000/113
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 780000/113"""
