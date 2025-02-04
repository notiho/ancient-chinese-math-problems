"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：本 a錢 。利 b錢 。
"""

"""
This is a classic "excess and deficiency" (盈不足) problem in ancient Chinese mathematics. The problem involves determining the principal (本) and interest (利) based on the returns from multiple transactions with a fixed profit rate. Let's solve it step by step using Python.

---

### Problem Breakdown:
1. The profit rate is 13%.
2. The returns from five transactions are:
   - First return: 14,000
   - Second return: 13,000
   - Third return: 12,000
   - Fourth return: 11,000
   - Fifth return: 10,000
3. The total principal and interest are exhausted after these five returns.
4. We need to find the original principal (本) and the total interest (利).

---

### Solution Procedure:
The "excess and deficiency" method (盈不足術) is used here. It involves:
1. Assuming two different values for the principal (本錢).
2. Calculating the total returns for each assumption.
3. Using the differences (盈 for excess, 不足 for deficiency) to find the correct principal.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
profit_rate = Fraction(13, 100)  # Profit rate is 13%
returns = [14000, 13000, 12000, 11000, 10000]  # Returns from five transactions

# Step 1: Assume two different values for the principal
assumed_principal_1 = 30000  # First assumption
assumed_principal_2 = 40000  # Second assumption

# Step 2: Calculate the total returns for each assumption
def calculate_total_returns(principal, profit_rate, returns):
    total = 0
    for r in returns:
        total += r / (1 + profit_rate)
    return total - principal

excess = calculate_total_returns(assumed_principal_2, profit_rate, returns)  # Excess (盈)
deficiency = calculate_total_returns(assumed_principal_1, profit_rate, returns)  # Deficiency (不足)

# Step 3: Use the excess and deficiency method to find the correct principal
# Formula: (excess * assumed_principal_1 + deficiency * assumed_principal_2) / (excess + deficiency)
principal = (excess * assumed_principal_1 + deficiency * assumed_principal_2) / (excess + deficiency)

# Step 4: Calculate the total interest
total_returns = sum(returns)
interest = total_returns - principal

# Output the results
a = principal
b = interest

print(f"本 (Principal): {a} 錢")
print(f"利 (Interest): {b} 錢")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Profit Rate**: The profit rate is converted into a fraction for precise calculations.
2. **Assumptions**: Two different values for the principal are assumed (30,000 and 40,000).
3. **Total Returns**: For each assumption, the total returns are calculated by dividing each return by `(1 + profit_rate)` and subtracting the assumed principal.
4. **Excess and Deficiency**: The differences between the calculated returns and the actual returns are used to find the correct principal using the formula from the "excess and deficiency" method.
5. **Interest**: The total interest is calculated as the difference between the total returns and the principal.

---

### Final Answer:
The code will output the values of `a` (principal) and `b` (interest) in terms of 錢.
"""


"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 14880000/409
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 9660000/409"""
