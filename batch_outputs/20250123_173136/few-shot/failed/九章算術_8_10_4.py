"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This problem involves solving a system of linear equations, which is described in the ancient Chinese mathematical text using the "fangcheng" (方程) method. Below is the translation of the problem and its solution into Python code:

### Problem Description:
Two horses and one ox together cost slightly more than 10,000, equal to the price of half a horse.  
One horse and two oxen together cost slightly less than 10,000, equal to the price of half an ox.  
Question: What are the prices of a horse and an ox?

### Procedure:
The "fangcheng" method is described as follows:
1. Represent the system of equations using coefficients (秉) for each variable.
2. Use elimination by multiplying rows and subtracting to simplify the system.
3. Solve for each variable step by step using substitution and division.

### Equations:
Let the price of a horse be `x` and the price of an ox be `y`.  
From the problem, we have:
1. \( 2x + y = 10000 + \frac{x}{2} \)
2. \( x + 2y = 10000 + \frac{y}{2} \)

Rewriting these equations:
1. \( 4x + 2y = 20000 + x \) → \( 3x + 2y = 20000 \)
2. \( 2x + 4y = 20000 + y \) → \( 2x + 3y = 20000 \)

Now solve this system of equations using the "fangcheng" method.

---

### Python Code:


"""


from fractions import Fraction

# Coefficients for the equations:
# 3x + 2y = 20000
# 2x + 3y = 20000

# Initialize the coefficients for the equations
# Representing the system as:
# [3, 2, 20000]  ->  3x + 2y = 20000
# [2, 3, 20000]  ->  2x + 3y = 20000
coefficients = [
    [3, 2, 20000],
    [2, 3, 20000]
]

# Step 1: Eliminate one variable (use elimination to simplify the system)
# Multiply the first row by 2 and the second row by 3 to align coefficients of x
row1 = [2 * c for c in coefficients[0]]  # [6, 4, 40000]
row2 = [3 * c for c in coefficients[1]]  # [6, 9, 60000]

# Subtract row1 from row2 to eliminate x
row3 = [row2[i] - row1[i] for i in range(3)]  # [0, 5, 20000]

# Step 2: Solve for y (from row3)
# 5y = 20000
y = Fraction(row3[2], row3[1])  # y = 20000 / 5 = 4000

# Step 3: Substitute y back into one of the original equations to solve for x
# Using the first equation: 3x + 2y = 20000
# 3x + 2(4000) = 20000
x = Fraction(20000 - 2 * y, 3)  # x = (20000 - 8000) / 3 = 12000 / 3 = 4000

# Final results
a = x  # Price of a horse
b = y  # Price of an ox

# Output the results
a, b


"""


### Explanation of the Code:
1. The system of equations is represented as rows of coefficients.
2. Elimination is used to simplify the system by aligning and subtracting coefficients to eliminate one variable.
3. The remaining variable is solved directly, and the result is substituted back to find the other variable.
4. The solution is expressed using the `Fraction` class to ensure exact arithmetic.

### Answer:
- The price of a horse is \( a = 4000 \) qian.
- The price of an ox is \( b = 4000 \) qian.
"""


"""
Variable 'a' has wrong value. Expected: 60000/11, Actual: 4000
Variable 'b' has wrong value. Expected: 20000/11, Actual: 4000"""
