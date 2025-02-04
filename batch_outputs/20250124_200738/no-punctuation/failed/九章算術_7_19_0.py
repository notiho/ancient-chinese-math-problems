"""
今有人持錢之蜀賈利十三初返歸一萬四千次返歸一萬三千次返歸一萬二千次返歸一萬一千後返歸一萬凡五返歸錢本利俱盡問本持錢及利各幾何
術曰假令本錢三萬不足一千七百三十八錢半令之四萬多三萬五千三百九十錢八分
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰本 a錢 利 b錢 
"""

"""
This problem involves a complex calculation using the "盈不足術" (Excess and Deficiency Method), which is an ancient Chinese algorithm for solving linear equations. Let's break it down step by step and translate it into Python code.

### Problem Description:
A person holds an unknown amount of money (本金, "principal") and goes to Shu to trade. The profit rate is 13%. After five returns, the money (principal + profit) is completely exhausted. The amounts returned are as follows:
- First return: 14,000
- Second return: 13,000
- Third return: 12,000
- Fourth return: 11,000
- Fifth return: 10,000

We are tasked with finding the original principal (*a* 錢) and the total profit (*b* 錢).

### Procedure:
The "盈不足術" (Excess and Deficiency Method) is used to solve this problem. The steps are as follows:
1. Assume two trial values for the principal (本金).
2. Calculate the total returns for each trial value based on the profit rate.
3. Compare the calculated returns with the actual total returns (sum of the five returns).
4. Use the excess and deficiency method to find the correct principal.

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# 利率 (profit rate)
profit_rate = Fraction(13, 100)

# 五次返歸的總和 (sum of the five returns)
total_returns = 14000 + 13000 + 12000 + 11000 + 10000

# 假設兩個本金試值 (assume two trial values for the principal)
trial1 = 30000  # 假令本錢三萬
trial2 = 40000  # 假令本錢四萬

# 計算每個試值的總返歸金額 (calculate total returns for each trial value)
# 總返歸金額 = 本金 * (1 + 利率)^5
def calculate_total_returns(principal, rate, times):
    total = 0
    for _ in range(times):
        total += principal * rate
        principal *= (1 + rate)
    return total

# 計算盈不足 (calculate excess and deficiency)
excess = calculate_total_returns(trial1, profit_rate, 5) - total_returns
deficiency = total_returns - calculate_total_returns(trial2, profit_rate, 5)

# 盈不足術求解本金 (use excess and deficiency method to find the principal)
principal = (trial1 * deficiency + trial2 * excess) / (excess + deficiency)

# 計算利潤 (calculate profit)
profit = principal * profit_rate * 5

# 答案
a = principal
b = profit

print(f"本錢: {a} 錢, 利潤: {b} 錢")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Profit Rate**: The profit rate is given as 13%, which is represented as a fraction (`Fraction(13, 100)`).
2. **Total Returns**: The sum of the five returns is calculated as `14000 + 13000 + 12000 + 11000 + 10000`.
3. **Trial Values**: Two trial values for the principal are assumed (`30000` and `40000`).
4. **Excess and Deficiency**: The total returns for each trial value are calculated, and the differences (excess and deficiency) are used to find the correct principal using the formula:
   \[
   本金 = \frac{{試值1 \times 不足 + 試值2 \times 盈}}{{盈 + 不足}}
   \]
5. **Profit**: The total profit is calculated as the product of the principal, the profit rate, and the number of returns (5).

### Final Answer:
The variables `a` and `b` represent the original principal and the total profit, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 600000000000000/8424351793
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 30000000000000/648027061"""
