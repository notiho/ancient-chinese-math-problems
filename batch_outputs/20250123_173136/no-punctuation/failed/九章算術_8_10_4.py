"""
今有二馬一牛價過一萬如半馬之價一馬二牛價不滿一萬如半牛之價問牛馬價各幾何
術曰如方程損益之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰馬價 a錢 牛價 b錢 
"""

"""
To solve this problem, we will use the ancient Chinese method of "fangcheng" (simultaneous equations). The problem involves two variables: the price of a horse and the price of a cow. Let's translate the procedure into Python step by step.

### Problem:
Two horses and one cow together cost more than 10,000 qian.  
The price of half a horse and one horse plus two cows together cost less than 10,000 qian.  
What are the prices of a horse and a cow?

### Procedure:
The "fangcheng" method involves setting up a system of equations and solving it step by step using elimination and substitution.

### Equations:
1. \( 2x + y = 10000 \) (price of 2 horses and 1 cow is 10,000 qian)
2. \( 0.5x + x + 2y = 10000 \) (price of half a horse, one horse, and two cows is 10,000 qian)

Where:
- \( x \) is the price of a horse,
- \( y \) is the price of a cow.

### Python Implementation:


"""


from fractions import Fraction

# Step 1: Define the equations
# Equation 1: 2x + y = 10000
# Equation 2: 0.5x + x + 2y = 10000

# Normalize Equation 2: Combine terms
# 1.5x + 2y = 10000

# Step 2: Represent the coefficients of the equations
# Coefficients for Equation 1: [2, 1, 10000]
# Coefficients for Equation 2: [1.5, 2, 10000]

# Convert coefficients to fractions for precise calculations
eq1 = [Fraction(2), Fraction(1), Fraction(10000)]
eq2 = [Fraction(3, 2), Fraction(2), Fraction(10000)]

# Step 3: Eliminate one variable (y) using the "fangcheng" method
# Multiply eq1 by 2 (to align the coefficient of y with eq2)
eq1_scaled = [2 * eq1[0], 2 * eq1[1], 2 * eq1[2]]  # [4, 2, 20000]

# Subtract eq2 from the scaled eq1 to eliminate y
# [4, 2, 20000] - [1.5, 2, 10000]
eq3 = [eq1_scaled[0] - eq2[0], eq1_scaled[1] - eq2[1], eq1_scaled[2] - eq2[2]]  # [2.5, 0, 10000]

# Step 4: Solve for x (price of a horse)
x = eq3[2] / eq3[0]  # x = 10000 / 2.5
x = Fraction(x)

# Step 5: Substitute x back into one of the original equations to solve for y
# Using Equation 1: 2x + y = 10000
y = eq1[2] - (eq1[0] * x)  # y = 10000 - 2x

# Step 6: Output the results
a = x  # Price of a horse
b = y  # Price of a cow

print(f"馬價 a = {a} 錢")
print(f"牛價 b = {b} 錢")


"""


### Explanation of the Code:
1. **Equation Setup**: The equations are set up based on the problem description. Fractions are used to ensure precise calculations.
2. **Elimination**: The "fangcheng" method eliminates one variable by scaling and subtracting equations.
3. **Substitution**: After finding one variable, it is substituted back into one of the original equations to find the other variable.
4. **Result**: The prices of the horse and cow are printed as fractions for exact values.

### Answer:
The price of a horse is \( a \) qian, and the price of a cow is \( b \) qian.
"""


"""
Variable 'a' has wrong value. Expected: 60000/11, Actual: 4000
Variable 'b' has wrong value. Expected: 20000/11, Actual: 2000"""
