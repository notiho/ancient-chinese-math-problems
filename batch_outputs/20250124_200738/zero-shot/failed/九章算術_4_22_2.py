"""
今有積四千五百尺。問︰為立圓徑幾何？
開立圓術曰：置積尺數，以十六乘之，九而一，所得開立方除之，即丸徑。
荅曰： a尺 。
"""

"""
To solve this problem, we need to compute the diameter of a sphere (丸徑) given its volume (積). The formula provided in the problem can be translated into Python code as follows:

1. Multiply the volume by 16.
2. Divide the result by 9.
3. Take the cube root of the result.
4. The result is the diameter of the sphere.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given volume
volume = Fraction(4500)  # in cubic feet

# Step 1: Multiply the volume by 16
step1 = volume * 16

# Step 2: Divide the result by 9
step2 = step1 / 9

# Step 3: Take the cube root of the result
a = step2 ** Fraction(1, 3)  # Diameter of the sphere in feet

# The diameter of the sphere is stored in variable 'a'
#----- content ends here -----


"""


The solution is stored in the variable `a`, which represents the diameter of the sphere in feet.
"""


"""
Variable 'a' has wrong value. Expected: 20, Actual: 19.999999999999996"""
