"""
今有人持錢之蜀賈利十三初返歸一萬四千次返歸一萬三千次返歸一萬二千次返歸一萬一千後返歸一萬凡五返歸錢本利俱盡問本持錢及利各幾何
術曰假令本錢三萬不足一千七百三十八錢半令之四萬多三萬五千三百九十錢八分
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰本 a錢 利 b錢 
"""

"""
This is a complex problem involving the "盈不足術" (Excess and Deficit Method), which is an ancient Chinese algorithm for solving linear equations. Let's carefully translate the procedure into Python step by step.

### Problem Breakdown:
- A person holds an unknown amount of money (本金, principal) and earns a profit (利, interest) of 13% on each trade.
- After five trades, the person returns with decreasing amounts of money: 14,000, 13,000, 12,000, 11,000, and finally 10,000, at which point the principal and interest are fully consumed.
- The goal is to find the original principal (本金) and the total profit (利).

### Procedure:
The "盈不足術" involves:
1. Assuming two trial values for the principal (本金) and calculating the resulting excess or deficit after the transactions.
2. Using the excess and deficit to compute the correct principal using a proportion.

### Python Code Implementation:


"""


from fractions import Fraction

# 利率 (profit rate per trade)
利率 = Fraction(13, 100)

# 假令本錢三萬 (Assume the first trial principal is 30,000)
本金1 = 30000

# 計算第一次假設的盈不足 (Calculate the excess/deficit for the first trial)
盈1 = 本金1 * (1 + 利率)**5 - 10000 - 11000 - 12000 - 13000 - 14000

# 假令本錢四萬 (Assume the second trial principal is 40,000)
本金2 = 40000

# 計算第二次假設的盈不足 (Calculate the excess/deficit for the second trial)
盈2 = 本金2 * (1 + 利率)**5 - 10000 - 11000 - 12000 - 13000 - 14000

# 盈不足術計算本金 (Use the excess and deficit to calculate the correct principal)
本金 = 本金1 + (本金2 - 本金1) * (-盈1) / (盈2 - 盈1)

# 計算利 (Calculate the total profit)
利 = 本金 * 利率 * 5

# Output the results
a = 本金
b = 利

# Print the results
print(f"本 a錢: {a}")
print(f"利 b錢: {b}")


"""


### Explanation of the Code:
1. **利率**: The profit rate per trade is given as 13%, which is represented as a fraction (`Fraction(13, 100)`).
2. **Trial Values**: Two trial values for the principal are assumed (`本金1` and `本金2`), and the resulting excess or deficit is calculated for each.
3. **盈不足術**: The formula for the "盈不足術" is applied to compute the correct principal based on the two trial values and their corresponding excess/deficit.
4. **Profit Calculation**: Once the principal is determined, the total profit is calculated as the product of the principal, the profit rate, and the number of trades (5).

### Final Answer:
The variables `a` and `b` will contain the original principal and total profit, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 600000000000000/18424351793
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 390000000000000/18424351793"""
