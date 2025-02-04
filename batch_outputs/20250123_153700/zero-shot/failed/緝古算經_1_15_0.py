"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
術曰：冪自乘，倍少數而一，為實。半少，為廉法，從。開立方除之，即股。加差，即弦。
答曰：弦 a 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code. Here's the step-by-step solution:

1. **Given**:
   - The product of the leg (股) and the hypotenuse (弦) is \( \frac{4036}{5} \).
   - The leg (股) is less than the hypotenuse (弦) by \( \frac{1}{5} \).

2. **Procedure**:
   - Compute the cube of the given product \( \frac{4036}{5} \).
   - Multiply the difference \( \frac{1}{5} \) by 2 and add 1 to get the "實" (real value).
   - Divide the cube of the product by the "實" to compute the leg (股).
   - Add the difference \( \frac{1}{5} \) to the leg to compute the hypotenuse (弦).

3. **Solution in Python**:


"""


from fractions import Fraction

# Given values
product = Fraction(4036, 5)  # The product of the leg and hypotenuse
difference = Fraction(1, 5)  # The difference between the hypotenuse and leg

# Step 1: Compute the cube of the product
cube_product = product ** 3

# Step 2: Compute the "實" (real value)
real_value = 2 * difference + 1

# Step 3: Compute the leg (股)
leg = cube_product / real_value

# Step 4: Compute the hypotenuse (弦)
a = leg + difference

# The hypotenuse is stored in variable 'a'


"""


The variable `a` contains the value of the hypotenuse (弦) as a `Fraction`.
"""


"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: 65743598691/175"""
