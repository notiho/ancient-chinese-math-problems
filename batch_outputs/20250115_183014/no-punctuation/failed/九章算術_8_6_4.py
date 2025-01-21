"""
今有牛五羊二直金十兩牛二羊五直金八兩問牛羊各直金幾何
術曰如方程
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰牛 a 直金 b兩 羊 c 直金 d兩 
"""

"""
To solve this problem, we need to determine the value of a cow and a sheep in terms of gold. This is a system of linear equations, and the ancient Chinese method described here corresponds to solving it using a procedure similar to Gaussian elimination. Let's translate the procedure into Python code:

### Problem Setup:
- 5 cows and 2 sheep are worth 10 taels of gold.
- 2 cows and 5 sheep are worth 8 taels of gold.
- We need to find the value of one cow (*a* taels of gold) and one sheep (*c* taels of gold).

### Procedure:
The procedure described in the text is the ancient Chinese "fangcheng" (方程) method, which is essentially a systematic elimination process to solve simultaneous linear equations.


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

# Step 1: Eliminate one variable (羊) by aligning coefficients
# Multiply the first equation by 5 (coefficient of 羊 in the second equation)
# Multiply the second equation by 2 (coefficient of 羊 in the first equation)
牛1, 羊1, 金1 = 5 * 牛1, 5 * 羊1, 5 * 金1
牛2, 羊2, 金2 = 2 * 牛2, 2 * 羊2, 2 * 金2

# Step 2: Subtract the second equation from the first to eliminate 羊
牛_diff = 牛1 - 牛2
金_diff = 金1 - 金2

# Step 3: Solve for the value of one cow (a)
a = Fraction(金_diff, 牛_diff)

# Step 4: Substitute the value of a (one cow) back into one of the original equations to solve for one sheep (c)
金_for_sheep = 金1 - (牛1 * a)
c = Fraction(金_for_sheep, 羊1)

# Final Answer
print(f"牛 a 直金 {a} 兩 羊 c 直金 {c} 兩")


"""


### Explanation of the Code:
1. **Align Coefficients**: The coefficients of sheep in both equations are made equal by multiplying the equations by appropriate factors.
2. **Eliminate Sheep**: By subtracting one equation from the other, the sheep variable is eliminated, leaving an equation with only cows.
3. **Solve for Cows**: The value of one cow is calculated by dividing the difference in gold by the difference in cow coefficients.
4. **Solve for Sheep**: The value of one sheep is calculated by substituting the value of a cow back into one of the original equations.

### Output:
The output will give the value of one cow (*a* taels of gold) and one sheep (*c* taels of gold).
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 34/21
Missing variable in output: 'b'
Variable 'c' has wrong value. Expected: 1, Actual: 20/21
Missing variable in output: 'd'"""
