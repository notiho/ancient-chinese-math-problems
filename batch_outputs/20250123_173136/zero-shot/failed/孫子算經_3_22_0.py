"""
今有方物一束外周，一市有三十二枚。問：積幾何？
術曰：重置二位左位減八餘加右位，至盡虛加一，即得。
答曰： a枚 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the total number of items ("積") in a bundle of objects arranged in a square shape, given that the outer perimeter contains 32 items. The solution involves following the described algorithm.

Here is the Python code:


"""


from fractions import Fraction

# Given data
outer_perimeter = 32  # The outer perimeter in items

# Step 1: Divide the outer perimeter by 4 to get the side length of the square
side_length = Fraction(outer_perimeter, 4)

# Step 2: Calculate the total number of items in the square (side_length^2)
a = side_length ** 2

# The total number of items is stored in variable 'a'
a


"""


### Explanation:
1. The outer perimeter of the square is given as 32 items.
2. Since a square has 4 equal sides, the length of one side is `outer_perimeter / 4`.
3. The total number of items in the square is the area of the square, which is `side_length^2`.

The result is stored in the variable `a`, which represents the total number of items in the bundle.
"""


"""
Variable 'a' has wrong value. Expected: 81, Actual: 64"""
