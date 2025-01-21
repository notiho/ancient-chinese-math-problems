"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛 a(=1) ，直金 b(=34/21)兩 ，羊 c(=1) ，直金 d(=20/21)兩 。
"""

"""
To solve this problem, we need to determine the value of a cow and a sheep in terms of gold (liang). The problem is essentially a system of linear equations, which can be solved using the method described in the "方程術" (method of solving simultaneous equations). Below is the Python implementation of the solution:


"""


from fractions import Fraction

# 牛五、羊二，直金十兩
牛1 = 5
羊1 = 2
金1 = 10

# 牛二、羊五，直金八兩
牛2 = 2
羊2 = 5
金2 = 8

# 方程術解法
# Step 1: Eliminate one variable (羊) by aligning coefficients and subtracting equations
# Multiply the first equation by 5 (coefficient of 羊 in the second equation)
# Multiply the second equation by 2 (coefficient of 羊 in the first equation)
eq1_multiplied = (牛1 * 5, 羊1 * 5, 金1 * 5)  # (25牛, 10羊, 50金)
eq2_multiplied = (牛2 * 2, 羊2 * 2, 金2 * 2)  # (4牛, 10羊, 16金)

# Subtract the second equation from the first to eliminate 羊
牛_diff = eq1_multiplied[0] - eq2_multiplied[0]  # 25牛 - 4牛 = 21牛
金_diff = eq1_multiplied[2] - eq2_multiplied[2]  # 50金 - 16金 = 34金

# Step 2: Solve for 牛
牛_value = Fraction(金_diff, 牛_diff)  # 牛 = 34/21 金

# Step 3: Substitute 牛's value into one of the original equations to solve for 羊
# Using the first equation: 5牛 + 2羊 = 10金
羊_value = Fraction(金1 - 牛1 * 牛_value, 羊1)  # 羊 = (10 - 5 * (34/21)) / 2 = 20/21 金

# Final results
a = 1  # 牛 count
b = 牛_value  # 牛 value in 金
c = 1  # 羊 count
d = 羊_value  # 羊 value in 金

# Output the results
print(f"牛 a(={a}), 直金 b(={b})兩, 羊 c(={c}), 直金 d(={d})兩.")


"""


### Explanation of the Code:
1. **Input the equations**: The problem gives us two equations:
   - \( 5 \text{牛} + 2 \text{羊} = 10 \text{金} \)
   - \( 2 \text{牛} + 5 \text{羊} = 8 \text{金} \)

2. **Eliminate one variable**: To eliminate the variable \( \text{羊} \), we align the coefficients of \( \text{羊} \) in both equations by multiplying the first equation by 5 and the second equation by 2. Then, we subtract the second equation from the first.

3. **Solve for \( \text{牛} \)**: After eliminating \( \text{羊} \), we solve for \( \text{牛} \) in terms of \( \text{金} \).

4. **Substitute \( \text{牛} \)'s value**: Using the value of \( \text{牛} \), we substitute it back into one of the original equations to solve for \( \text{羊} \).

5. **Output the results**: The values of \( \text{牛} \) and \( \text{羊} \) in terms of \( \text{金} \) are printed.

### Final Answer:
- 牛 \( a = 1 \), 直金 \( b = \frac{34}{21} \) 兩
- 羊 \( c = 1 \), 直金 \( d = \frac{20}{21} \) 兩
"""


"""
"""
