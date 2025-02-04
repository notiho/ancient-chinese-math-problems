"""
今有木長二丈，圍之三尺。葛生其下，纏木七周，上與木齊。問︰葛長幾何？
術曰：以七周乘三尺為股，木長為句，為之求弦。弦者，葛之長。
荅曰： a丈 。
"""

"""
To solve this problem, we need to calculate the length of the vine (葛) that wraps around the tree seven times and reaches the top of the tree. The tree's height is given as 2丈, and the circumference of the tree is 3尺. The vine forms a helical path, and the length of the vine can be calculated as the hypotenuse of a right triangle, where:

- One leg (股) is the total horizontal distance traveled by the vine, which is the circumference of the tree (3尺) multiplied by the number of wraps (7).
- The other leg (句) is the height of the tree (2丈).
- The hypotenuse (弦) is the length of the vine (葛).

We will use the Pythagorean theorem to calculate the hypotenuse.

Here is the Python code:


"""


from fractions import Fraction
import math

# Given values
tree_height = Fraction(2)  # Height of the tree in 丈
circumference = Fraction(3, 10)  # Circumference of the tree in 丈 (1丈 = 10尺)
wraps = 7  # Number of wraps

# Calculate the total horizontal distance (股)
horizontal_distance = wraps * circumference

# Calculate the length of the vine (弦) using the Pythagorean theorem
a = math.sqrt(float(tree_height**2 + horizontal_distance**2))

# Convert the result back to a Fraction for precise representation
a = Fraction(a).limit_denominator()

# The length of the vine (葛) in 丈
print(f"The length of the vine is {a}丈.")


"""


The variable `a` will store the length of the vine in 丈.
"""


"""
"""
