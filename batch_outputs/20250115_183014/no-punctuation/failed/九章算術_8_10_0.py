"""
今有二馬一牛價過一萬如半馬之價一馬二牛價不滿一萬如半牛之價問牛馬價各幾何
術曰如方程損益之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰馬價 a錢 牛價 b錢 
"""

"""
This problem involves solving a system of equations using the ancient Chinese "fangcheng" (method of elimination). Let's break it down step by step and implement it in Python.

### Problem:
We are given:
1. The price of two horses and one cow exceeds 10,000.
2. The price of half a horse and one horse plus two cows is less than 10,000.
3. The price of half a cow is also involved.

We need to find the price of one horse (`a`) and one cow (`b`).

### Procedure:
The "fangcheng" method involves setting up equations, eliminating variables step by step, and solving for the unknowns. Here's the Python implementation:


"""


from fractions import Fraction

# Step 1: Define the equations based on the problem
# Let x = price of one horse, y = price of one cow
# Equation 1: 2x + y = 10000 + surplus (we'll call it s1)
# Equation 2: 0.5x + x + 2y = 10000 - deficit (we'll call it s2)
# Equation 3: 0.5y = some value (we'll call it s3)

# Step 2: Rewrite the equations in terms of fractions
# Equation 1: 2x + y = 10000
# Equation 2: 1.5x + 2y = 10000
# Equation 3: 0.5y = y / 2

# Step 3: Use fangcheng (elimination) to solve for x and y
# Multiply Equation 1 by 2 to align coefficients of y
# 4x + 2y = 20000
# Subtract Equation 2 from this result:
# (4x + 2y) - (1.5x + 2y) = 20000 - 10000
# 2.5x = 10000
# x = 10000 / 2.5

# Solve for x
x = Fraction(10000, 5)  # Simplify 10000 / 2.5 to 10000 / 5
x = 4000  # Price of one horse

# Substitute x back into Equation 1 to solve for y
# 2x + y = 10000
# 2(4000) + y = 10000
# 8000 + y = 10000
# y = 10000 - 8000

y = 2000  # Price of one cow

# Final answers
a = x  # Price of one horse
b = y  # Price of one cow

# Output the results
print(f"馬價 {a} 錢 牛價 {b} 錢")


"""


### Explanation:
1. We set up the equations based on the problem statement.
2. Using the "fangcheng" method, we eliminate variables step by step to solve for the unknowns.
3. The solution gives us the price of one horse (`a`) and one cow (`b`).

### Answer:
- 馬價 `4000` 錢
- 牛價 `2000` 錢
"""


"""
Variable 'a' has wrong value. Expected: 60000/11, Actual: 4000
Variable 'b' has wrong value. Expected: 20000/11, Actual: 2000"""
