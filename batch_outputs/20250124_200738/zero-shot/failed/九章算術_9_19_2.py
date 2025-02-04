"""
今有邑方不知大小，各中開門。出北門二十步有木。出南門十四步，折而西行一千七百七十五步見木。問︰邑方幾何？
術曰：以出北門步數乘西行步數，倍之，為實。并出南門步數為從法，開方除之，即邑方。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the side length of a square-shaped city ("邑方") based on the given distances. Let's compute the solution step by step.

### Problem Breakdown:
1. The city is square-shaped, and its side length is unknown (`a`).
2. From the north gate, walking 20 steps north leads to a tree.
3. From the south gate, walking 14 steps south and then 1775 steps west leads to the same tree.
4. The formula provided is:
   - Multiply the north gate steps (20) by the westward steps (1775), double the result, and add the south gate steps (14).
   - Take the square root of this result to find the side length of the square (`a`).

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction
import math

# Given values
north_steps = 20  # steps north from the north gate
south_steps = 14  # steps south from the south gate
west_steps = 1775  # steps west after walking south

# Compute the area-related value
numerator = 2 * north_steps * west_steps + south_steps

# Compute the side length of the square (a)
a = math.sqrt(numerator)

# Result
a = Fraction(a).limit_denominator()  # Represent as a fraction if necessary
#----- content ends here -----


"""


### Explanation:
1. `north_steps` is the number of steps north from the north gate (20).
2. `south_steps` is the number of steps south from the south gate (14).
3. `west_steps` is the number of steps west after walking south (1775).
4. The formula calculates the square's side length (`a`) by taking the square root of the computed value.

### Final Answer:
The variable `a` contains the side length of the square in steps.
"""


"""
Variable 'a' has wrong value. Expected: 250, Actual: 101212953/379808"""
