"""
今有上禾七秉損實一斗益之下禾二秉而實一十斗下禾八秉益實一斗與上禾二秉而實一十斗問上下禾實一秉各幾何
術曰如方程損之曰益益之曰損損實一斗者其實過一十斗也益實一斗者其實不滿一十斗也
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉實 a斗 下禾一秉實 b斗 
"""

"""
This is a classic problem involving a system of linear equations, as described in ancient Chinese mathematics. The procedure involves solving the equations step by step using elimination and substitution. Let's translate the problem and the procedure into Python code.

### Problem Breakdown:
- There are two types of grain: upper grain (上禾) and lower grain (下禾).
- The relationships are given as:
  1. 7 units of upper grain lose 1 dou, and when 2 units of lower grain are added, the total is 10 dou.
  2. 8 units of lower grain gain 1 dou, and when 2 units of upper grain are added, the total is 10 dou.
- We are tasked to find how much one unit of upper grain (上禾) and one unit of lower grain (下禾) yield in dou.

### Procedure:
The procedure involves solving the system of equations using elimination and substitution, as described in the ancient text.


"""


from fractions import Fraction

# Define the equations based on the problem:
# Let x = the yield of one unit of upper grain (上禾) in dou
# Let y = the yield of one unit of lower grain (下禾) in dou

# Equation 1: 7x - 1 + 2y = 10
# Simplify: 7x + 2y = 11

# Equation 2: 8y + 1 + 2x = 10
# Simplify: 2x + 8y = 9

# Coefficients of the equations:
# Equation 1: 7x + 2y = 11
# Equation 2: 2x + 8y = 9

# Step 1: Eliminate one variable (e.g., x) by multiplying the equations to align coefficients
# Multiply Equation 1 by 2 and Equation 2 by 7:
# 14x + 4y = 22  (Equation 1 scaled)
# 14x + 56y = 63 (Equation 2 scaled)

# Subtract the scaled Equation 1 from the scaled Equation 2 to eliminate x:
# (14x + 56y) - (14x + 4y) = 63 - 22
# 52y = 41
y = Fraction(41, 52)  # Solve for y (yield of one unit of lower grain)

# Step 2: Substitute y back into one of the original equations to solve for x
# Use Equation 1: 7x + 2y = 11
# 7x + 2(Fraction(41, 52)) = 11
# 7x = 11 - 2(Fraction(41, 52))
# 7x = Fraction(572, 52) - Fraction(82, 52)
# 7x = Fraction(490, 52)
x = Fraction(490, 52) / 7  # Solve for x (yield of one unit of upper grain)
x = Fraction(70, 52)

# Simplify the fractions:
x = Fraction(35, 26)  # Yield of one unit of upper grain
y = Fraction(41, 52)  # Yield of one unit of lower grain

# Final answer:
a = x  # Yield of one unit of upper grain
b = y  # Yield of one unit of lower grain

print(f"上禾一秉實 {a} 斗")
print(f"下禾一秉實 {b} 斗")


"""


### Explanation of the Code:
1. The problem is translated into two linear equations based on the relationships provided.
2. The equations are solved step by step using elimination to remove one variable and substitution to solve for the other.
3. The results are expressed as fractions (`Fraction` class) to ensure accuracy, as ancient Chinese mathematics often dealt with fractional results.

### Final Answer:
- 上禾一秉實 \( \frac{35}{26} \) 斗
- 下禾一秉實 \( \frac{41}{52} \) 斗
"""


"""
"""
