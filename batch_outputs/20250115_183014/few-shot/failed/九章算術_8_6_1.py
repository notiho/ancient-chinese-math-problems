"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛 a ，直金 b兩 ，羊 c ，直金 d兩 。
"""

"""
This problem involves solving a system of linear equations to determine the value of a cow and a sheep in terms of gold taels. The ancient Chinese method described here is essentially a form of Gaussian elimination, referred to as "方程術" (method of solving equations). Below is the Python implementation of the solution:


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

# Step 1: Normalize the first equation by dividing through by 牛1
# This makes the coefficient of 牛 in the first equation equal to 1
牛1_coeff = Fraction(1, 牛1)
牛1 = 牛1 * 牛1_coeff
羊1 = 羊1 * 牛1_coeff
金1 = 金1 * 牛1_coeff

# Step 2: Eliminate the 牛 term from the second equation
牛2_coeff = 牛2
牛2 = 牛2 - (牛1 * 牛2_coeff)
羊2 = 羊2 - (羊1 * 牛2_coeff)
金2 = 金2 - (金1 * 牛2_coeff)

# Step 3: Solve for 羊 (sheep) in the second equation
羊_value = Fraction(金2, 羊2)

# Step 4: Substitute 羊_value back into the first equation to solve for 牛 (cow)
牛_value = 金1 - (羊1 * 羊_value)

# Assign results
a = "牛"
b = 牛_value
c = "羊"
d = 羊_value

# Output results
print(f"{a}直金 {b} 兩")
print(f"{c}直金 {d} 兩")


"""


### Explanation of the Code:
1. **Step 1**: Normalize the first equation so that the coefficient of 牛 (cow) becomes 1. This is done by dividing all terms of the first equation by the coefficient of 牛 in the first equation.
2. **Step 2**: Eliminate the 牛 term from the second equation by subtracting a multiple of the first equation from the second equation.
3. **Step 3**: Solve for 羊 (sheep) in the second equation, as it now only contains 羊 and 金 (gold taels).
4. **Step 4**: Substitute the value of 羊 back into the first equation to solve for 牛.

### Final Answer:
The values of 牛 (cow) and 羊 (sheep) in terms of gold taels are printed as the output.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 牛
Variable 'c' has wrong value. Expected: 1, Actual: 羊"""
