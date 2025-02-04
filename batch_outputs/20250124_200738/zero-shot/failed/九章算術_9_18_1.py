"""
今有邑方不知大小，各中開門。出北門三十步有木，出西門七百五十步見木。問︰邑方幾何？
術曰：令兩出門步數相乘，因而四之，為實。開方除之，即得邑方。
荅曰： a里 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a square city (邑方) with unknown side length. The distances from the north gate and west gate to a tree are given. The solution involves multiplying these distances, multiplying the result by 4, and then taking the square root to find the side length of the square city.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given distances
north_gate_distance = Fraction(30)  # 30 steps
west_gate_distance = Fraction(750)  # 750 steps

# Compute the area of the square city
area = 4 * north_gate_distance * west_gate_distance

# Compute the side length of the square city
a = math.sqrt(area)

# Convert steps to li (1 li = 180 steps)
a = Fraction(a) / 180  # Convert to li

# The side length of the square city in li
a
#----- content ends here -----


"""


The variable `a` will contain the side length of the square city in li.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 5/3"""
