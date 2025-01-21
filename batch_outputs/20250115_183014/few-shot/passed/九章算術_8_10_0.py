"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This problem involves solving a system of linear equations using a method similar to Gaussian elimination, as described in the ancient Chinese "fangcheng" (方程) method. Let's translate the problem and procedure into Python code.

### Problem Description:
Suppose:
- The price of 2 horses and 1 cow exceeds 10,000 by the price of half a horse.
- The price of 1 horse and 2 cows is less than 10,000 by the price of half a cow.

Question: What are the prices of a horse and a cow?

### Procedure:
The procedure uses the "fangcheng" method, which is an ancient Chinese algorithm for solving systems of linear equations. The steps involve setting up equations, performing row operations, and solving for the unknowns.

### Python Code:


"""


from fractions import Fraction

# Define the equations based on the problem:
# 2馬 + 1牛 = 10000 + 0.5馬
# 1馬 + 2牛 = 10000 - 0.5牛

# Rewrite the equations in standard form:
# 1. 3/2馬 + 1牛 = 10000
# 2. 1馬 + 5/2牛 = 10000

# Coefficients of the equations:
# Equation 1: 3/2馬 + 1牛 = 10000
a1 = Fraction(3, 2)  # Coefficient of 馬 in equation 1
b1 = Fraction(1)     # Coefficient of 牛 in equation 1
c1 = 10000           # Constant term in equation 1

# Equation 2: 1馬 + 5/2牛 = 10000
a2 = Fraction(1)     # Coefficient of 馬 in equation 2
b2 = Fraction(5, 2)  # Coefficient of 牛 in equation 2
c2 = 10000           # Constant term in equation 2

# Step 1: Eliminate 馬 from the second equation.
# Multiply the first equation by 2 to eliminate fractions:
# 3馬 + 2牛 = 20000
# Multiply the second equation by 2:
# 2馬 + 5牛 = 20000

# New coefficients:
A1 = 3  # Coefficient of 馬 in the first equation
B1 = 2  # Coefficient of 牛 in the first equation
C1 = 20000  # Constant term in the first equation

A2 = 2  # Coefficient of 馬 in the second equation
B2 = 5  # Coefficient of 牛 in the second equation
C2 = 20000  # Constant term in the second equation

# Eliminate 馬 by multiplying the equations to align coefficients:
# Multiply the first equation by 2 and the second equation by 3:
# 6馬 + 4牛 = 40000
# 6馬 + 15牛 = 60000

# Subtract the first equation from the second:
# (6馬 + 15牛) - (6馬 + 4牛) = 60000 - 40000
# 11牛 = 20000

# Solve for 牛:
牛價 = Fraction(20000, 11)

# Step 2: Solve for 馬 using the first equation:
# 3馬 + 2牛 = 20000
# 3馬 = 20000 - 2牛
# 馬 = (20000 - 2牛) / 3

馬價 = Fraction(20000 - 2 * 牛價, 3)

# Final answers:
a = 馬價
b = 牛價

print(f"馬價: {a} 錢")
print(f"牛價: {b} 錢")


"""


### Explanation of the Code:
1. The problem is translated into two linear equations.
2. Fractions are used to ensure accuracy in calculations.
3. The "fangcheng" method is implemented step by step:
   - Eliminate one variable (馬) by aligning coefficients and subtracting equations.
   - Solve for the remaining variable (牛).
   - Substitute back to find the value of the eliminated variable (馬).
4. The final prices of the horse and cow are expressed as fractions for precision.

### Output:
The code will output the prices of the horse and the cow in terms of 錢 (money).
"""


"""
"""
