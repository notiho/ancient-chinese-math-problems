"""
今有方田桑生中央，從角至桑，一百四十七步。問：為田幾何？
術曰：置角至桑一百四十七步，倍之，得二百九十四步，以五乘之，得一千四百七十步，以七除之，得二百一十步，自相乘，得四萬四千一百步，以二百四十步除之，即得。
答曰： a頃 ，奇 b步 。
"""

"""
Here is the Python code that translates the problem into a computation:


"""


from fractions import Fraction

# Given data
distance_to_tree = 147  # in steps

# Step 1: Double the distance
doubled_distance = distance_to_tree * 2  # 294 steps

# Step 2: Multiply by 5
multiplied_by_five = doubled_distance * 5  # 1470 steps

# Step 3: Divide by 7
divided_by_seven = Fraction(multiplied_by_five, 7)  # 210 steps

# Step 4: Square the result
squared_result = divided_by_seven ** 2  # 44100 square steps

# Step 5: Divide by 240 to convert to qing and steps
area_in_qing = squared_result // 240  # integer part in qing
remaining_steps = squared_result % 240  # remainder in steps

# Assign the results to variables
a = area_in_qing  # in qing
b = remaining_steps  # in steps


"""


The solution is stored in variables `a` (in qing) and `b` (in steps).
"""


"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 183"""
