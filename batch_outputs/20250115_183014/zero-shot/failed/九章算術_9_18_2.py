"""
今有邑方不知大小，各中開門。出北門三十步有木，出西門七百五十步見木。問︰邑方幾何？
術曰：令兩出門步數相乘，因而四之，為實。開方除之，即得邑方。
荅曰： a里 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical method into Python code. The problem involves finding the side length of a square city (邑方) where the distances to a tree from the north gate and west gate are given. The solution involves multiplying the two distances, multiplying the result by 4, and then taking the square root to find the side length.

Here is the Python code:


"""


from fractions import Fraction
import math

# Given distances
north_gate_distance = Fraction(30)  # in steps
west_gate_distance = Fraction(750)  # in steps

# Compute the area-related value
product_of_distances = north_gate_distance * west_gate_distance
area_times_four = product_of_distances * 4

# Compute the side length of the square city
a = Fraction(math.sqrt(area_times_four))

# The result is in steps, convert to li (1 li = 180 steps)
a = a / 180  # Convert steps to li

# The side length of the square city is stored in variable 'a'


"""


The variable `a` will contain the side length of the square city in **li**.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 5/3"""
