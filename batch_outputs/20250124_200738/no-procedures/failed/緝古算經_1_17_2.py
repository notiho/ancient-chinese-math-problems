"""
假令有股弦相乘冪四千七百三十九五分之三，句少於弦五十四五分之二。問：股多少？
答曰： a 。
"""

"""
This problem involves solving a right triangle where the relationship between the sides (the "leg" and "hypotenuse") is given. Let's break it down step by step and solve it.

### Problem Breakdown:
- The product of the two legs (股 and 弦) is given as \( 4739 \frac{3}{5} \) (or \( \frac{23696}{5} \)).
- The difference between the hypotenuse (弦) and the other leg (句) is \( 54 \frac{2}{5} \) (or \( \frac{272}{5} \)).
- We need to find the value of the leg \( 股 \) (denoted as \( a \)).

---

### Python Code Solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
product_of_legs = Fraction(23696, 5)  # 股弦相乘冪
difference = Fraction(272, 5)        # 弦 - 句

# Let 股 = x and 弦 = y
# We know:
# 1. x * y = product_of_legs
# 2. y - x = difference

# From the second equation, y = x + difference
# Substitute into the first equation:
# x * (x + difference) = product_of_legs
# Solve for x:
# x^2 + difference * x - product_of_legs = 0

# Coefficients of the quadratic equation
a_coeff = 1
b_coeff = difference
c_coeff = -product_of_legs

# Solve the quadratic equation using the quadratic formula:
# x = (-b ± sqrt(b^2 - 4ac)) / 2a

# Calculate the discriminant
discriminant = b_coeff**2 - 4 * a_coeff * c_coeff

# Take the positive root (since lengths are positive)
股 = (-b_coeff + discriminant**0.5) / (2 * a_coeff)

# Output the result
股 = Fraction(股)
股
#----- content ends here -----


"""


---

### Explanation:
1. The quadratic equation is derived from the relationships given in the problem.
2. The discriminant is calculated to ensure the solution is real.
3. The positive root is taken because side lengths cannot be negative.

Let me know if you'd like further clarification!
"""


"""
Missing variable in output: 'a'"""
