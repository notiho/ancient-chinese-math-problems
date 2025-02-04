"""
今有地，長一千步，廣五百步，尺有鶉、寸有鷃。問鶉、鷃各幾何？
術曰：置長一千步，以廣五百步乘之，得五十萬；以三十六乘之，得一千八百萬尺，即得鶉數；上十之，即得鷃數。
答曰：鶉 a ，鷃 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the number of "鶉" (a) and "鷃" (b) based on the given dimensions of the land and the conversion factors.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions of the land
length = 1000  # in steps
width = 500  # in steps

# Step 1: Calculate the area in steps
area_steps = length * width  # Area in steps^2

# Step 2: Convert the area to square feet (尺)
area_feet = area_steps * 36  # 1 step^2 = 36 square feet

# Step 3: Calculate the number of 鶉 (a)
a = area_feet  # 鶉 is the total area in square feet

# Step 4: Calculate the number of 鷃 (b)
b = a * 10  # 鷃 is 10 times the number of 鶉

# The answers
print("鶉 (a):", a)
print("鷃 (b):", b)
#----- content ends here -----


"""


### Explanation:
1. The area of the land is calculated by multiplying the length and width in steps.
2. Each step squared is equivalent to 36 square feet (尺), so the area in steps is converted to square feet.
3. The number of "鶉" (a) is equal to the total area in square feet.
4. The number of "鷃" (b) is 10 times the number of "鶉".

### Output:
```
鶉 (a): 18000000
鷃 (b): 180000000
```
"""


"""
Variable 'b' has wrong value. Expected: 1000080000000, Actual: 180000000"""
