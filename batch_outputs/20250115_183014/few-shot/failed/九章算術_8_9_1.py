"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
This problem involves solving a system of equations based on the given relationships between the amounts of money held by two individuals, A (甲) and B (乙). The solution uses a method akin to solving simultaneous equations, as described in the ancient Chinese "fangcheng" (方程) method.

### Problem Restatement:
Two individuals, A and B, hold an unknown amount of money.  
- If A takes half of B's money, A will have 50 units of money.  
- If B takes more than half of A's money (specifically, \( \frac{3}{2} \) of half of A's money), B will also have 50 units of money.  
The question is: How much money does A (甲) and B (乙) each hold?

### Procedure:
The procedure follows the ancient "fangcheng" (方程) method, which is essentially solving a system of linear equations. The relationships can be expressed as:

1. \( A + \frac{1}{2}B = 50 \)  
2. \( B + \frac{3}{4}A = 50 \)  

We will solve these equations step by step.

---

### Python Code Implementation:


"""


from fractions import Fraction

# Define the equations:
# A + (1/2)B = 50
# B + (3/4)A = 50

# Let A = 甲, B = 乙
# Step 1: Express the equations in terms of fractions
# Equation 1: A + (1/2)B = 50
# Equation 2: B + (3/4)A = 50

# Step 2: Solve for B in terms of A using Equation 1
# B = 2 * (50 - A)
B = lambda A: 2 * (50 - A)

# Step 3: Substitute B into Equation 2 and solve for A
# (2 * (50 - A)) + (3/4)A = 50
# Expand: 100 - 2A + (3/4)A = 50
# Combine terms: 100 - (2 - 3/4)A = 50
# Simplify: 100 - (8/4 - 3/4)A = 50
# 100 - (5/4)A = 50
# (5/4)A = 100 - 50
# (5/4)A = 50
# A = 50 * (4/5)
A = Fraction(50) * Fraction(4, 5)

# Step 4: Solve for B using the value of A
B_value = B(A)

# Results
a = A  # A's money
b = B_value  # B's money

# Output the results
a, b


"""


---

### Explanation of the Code:
1. **Define the equations**: The problem is translated into two linear equations based on the relationships provided.
2. **Solve for one variable**: Using Equation 1, \( B \) is expressed in terms of \( A \).
3. **Substitute into the second equation**: The expression for \( B \) is substituted into Equation 2, leaving an equation with only \( A \).
4. **Solve for \( A \)**: The equation is simplified to find the value of \( A \).
5. **Find \( B \)**: The value of \( A \) is substituted back into the expression for \( B \) to find its value.
6. **Output the results**: The final values of \( A \) (甲) and \( B \) (乙) are displayed.

---

### Answer:
The amounts of money held by A (甲) and B (乙) are:

- \( a = 40 \) (甲持 40 錢)  
- \( b = 20 \) (乙持 20 錢)  
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 40
Variable 'b' has wrong value. Expected: 25, Actual: 20"""
