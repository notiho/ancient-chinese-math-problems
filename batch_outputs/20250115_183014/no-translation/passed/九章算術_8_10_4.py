"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese mathematical methods, specifically the "方程術" (method of solving equations). Let's translate this into Python code step by step.

The problem can be expressed as two equations:
1. \( 2M + 1B = 10000 + 0.5M \)
2. \( 1M + 2B = 10000 - 0.5B \)

Where \( M \) is the price of a horse (馬價), and \( B \) is the price of a cow (牛價). Simplifying these equations:
1. \( 1.5M + 1B = 10000 \)
2. \( 1M + 2.5B = 10000 \)

Now, we solve this system using the described method.


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 1.5M + 1B = 10000
# Equation 2: 1M + 2.5B = 10000
coefficients = [
    [Fraction(3, 2), 1, 10000],  # 1.5M + 1B = 10000
    [1, Fraction(5, 2), 10000]   # 1M + 2.5B = 10000
]

# Step 1: Normalize the first row (divide by the leading coefficient)
coefficients[0] = [x / coefficients[0][0] for x in coefficients[0]]

# Step 2: Eliminate the first variable from the second row
factor = coefficients[1][0]
coefficients[1] = [
    coefficients[1][i] - factor * coefficients[0][i]
    for i in range(len(coefficients[0]))
]

# Step 3: Solve for the second variable (B)
b = coefficients[1][2] / coefficients[1][1]

# Step 4: Back-substitute to solve for the first variable (M)
a = coefficients[0][2] - coefficients[0][1] * b

# Results
print(f"馬價 a = {a} 錢")
print(f"牛價 b = {b} 錢")


"""


### Explanation of the Code:
1. The coefficients of the equations are represented as a list of lists. Each sublist corresponds to an equation, with the coefficients of \( M \), \( B \), and the constant term.
2. The first row is normalized by dividing through by the leading coefficient.
3. The first variable (\( M \)) is eliminated from the second row using row operations.
4. The second variable (\( B \)) is solved directly from the second row.
5. Back-substitution is used to solve for the first variable (\( M \)).

### Final Answer:
The values of \( a \) (馬價) and \( b \) (牛價) are calculated and printed.
"""


"""
"""
