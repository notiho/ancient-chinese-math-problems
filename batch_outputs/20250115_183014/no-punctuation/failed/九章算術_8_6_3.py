"""
今有牛五羊二直金十兩牛二羊五直金八兩問牛羊各直金幾何
術曰如方程
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰牛 a 直金 b兩 羊 c 直金 d兩 
"""

"""
This problem involves solving a system of linear equations to determine the value of a cow and a sheep in terms of gold (金). The ancient Chinese method described here is equivalent to solving simultaneous equations using elimination or substitution. Let's translate this into Python code.

The problem is as follows:
- 5 cows and 2 sheep are worth 10 taels of gold.
- 2 cows and 5 sheep are worth 8 taels of gold.
- Find the value of a cow and a sheep.

The procedure ("方程術") describes a method for solving simultaneous equations step by step.


"""


from fractions import Fraction

# 牛五羊二直金十兩
牛1 = 5
羊1 = 2
金1 = 10

# 牛二羊五直金八兩
牛2 = 2
羊2 = 5
金2 = 8

# Step 1: Eliminate one variable (羊) by aligning coefficients and subtracting equations
# Multiply the first equation by 5 (羊2) and the second equation by 2 (羊1)
eq1_multiplier = 羊2
eq2_multiplier = 羊1

牛1_new = eq1_multiplier * 牛1
羊1_new = eq1_multiplier * 羊1
金1_new = eq1_multiplier * 金1

牛2_new = eq2_multiplier * 牛2
羊2_new = eq2_multiplier * 羊2
金2_new = eq2_multiplier * 金2

# Subtract the second equation from the first to eliminate 羊
牛_diff = 牛1_new - 牛2_new
金_diff = 金1_new - 金2_new

# Step 2: Solve for the value of a cow (牛)
牛_value = Fraction(金_diff, 牛_diff)

# Step 3: Substitute the value of 牛 into one of the original equations to solve for 羊
# Using the first equation: 5牛 + 2羊 = 10
羊_value = Fraction(金1 - (牛1 * 牛_value), 羊1)

# Final results
a = 牛_value  # Value of a cow in taels of gold
b = 羊_value  # Value of a sheep in taels of gold

# Output the results
print(f"牛直金 {a} 兩")
print(f"羊直金 {b} 兩")


"""


### Explanation of the Code:
1. **Input the equations**: The coefficients of cows, sheep, and gold are input as variables.
2. **Eliminate one variable**: The coefficients of sheep are aligned by multiplying the equations by appropriate factors, and then one equation is subtracted from the other to eliminate sheep.
3. **Solve for the remaining variable**: The value of a cow is calculated by dividing the difference in gold by the difference in cow coefficients.
4. **Substitute back**: The value of a cow is substituted into one of the original equations to solve for the value of a sheep.
5. **Output the results**: The values of a cow and a sheep are displayed as fractions for precision.

### Answer:
The value of a cow is `a` taels of gold, and the value of a sheep is `b` taels of gold.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 34/21
Variable 'b' has wrong value. Expected: 34/21, Actual: 20/21
Missing variable in output: 'c'
Missing variable in output: 'd'"""
