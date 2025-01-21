"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of "fangcheng" (方程), which is an early form of solving simultaneous equations. Let's translate the problem and procedure into Python code.

### Problem:
Two horses and one cow together cost more than 10,000, equal to the price of half a horse.  
One horse and two cows together cost less than 10,000, equal to the price of half a cow.  
Question: What are the prices of a horse and a cow?

### Procedure:
The "fangcheng" method involves setting up a matrix of coefficients and solving it step by step using elimination and substitution. Here's the Python implementation:


"""


from fractions import Fraction

# Define the equations based on the problem:
# 2馬 + 1牛 = 10000 (equal to half a horse)
# 1馬 + 2牛 = 10000 (equal to half a cow)

# Coefficients of the equations:
# Equation 1: 2馬 + 1牛 - 10000 = 0
# Equation 2: 1馬 + 2牛 - 10000 = 0

# Represent the system as a matrix:
# [ 2  1 | 10000 ]
# [ 1  2 | 10000 ]

# Step 1: Eliminate one variable (牛) using the "fangcheng" method.
# Multiply the first equation by 2 and the second equation by 1 to align 牛 coefficients:
# [ 4  2 | 20000 ]
# [ 1  2 | 10000 ]

# Subtract the second equation from the first:
# [ 3  0 | 10000 ]  (This gives the value of 馬)

# Step 2: Solve for 馬:
馬價 = Fraction(10000, 3)

# Step 3: Substitute 馬價 into one of the original equations to solve for 牛:
# Using the first equation: 2馬 + 1牛 = 10000
牛價 = Fraction(10000 - 2 * 馬價, 1)

# Final results:
a = 馬價
b = 牛價

print(f"馬價: {a}錢, 牛價: {b}錢")


"""


### Explanation:
1. The system of equations is represented as a matrix.
2. The "fangcheng" method eliminates one variable (牛) by aligning coefficients and subtracting equations.
3. The remaining equation is solved for 馬 (horse price).
4. The value of 馬 is substituted back into one of the original equations to solve for 牛 (cow price).

### Answer:
The price of a horse is `a` qian, and the price of a cow is `b` qian.
"""


"""
Variable 'a' has wrong value. Expected: 60000/11, Actual: 10000/3
Variable 'b' has wrong value. Expected: 20000/11, Actual: 10000/3"""
