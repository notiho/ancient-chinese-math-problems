"""
今有獸，六首四足；禽，二首二足，上有七十六首，下有四十六足。問：禽、獸各幾何？
術曰：倍足以減首，餘半之，即獸；以四乘獸，減足，餘半之，即禽。
答曰： a 獸 b 禽。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the number of "獸" (beasts) and "禽" (birds) based on the given number of heads and feet.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_heads = 76  # Total number of heads
total_feet = 46   # Total number of feet

# Step 1: Calculate the number of beasts (獸)
# "倍足以減首，餘半之，即獸" translates to:
# Double the total feet, subtract the total heads, then divide the result by 2 to get the number of beasts.
a = (2 * total_feet - total_heads) / 2

# Step 2: Calculate the number of birds (禽)
# "以四乘獸，減足，餘半之，即禽" translates to:
# Multiply the number of beasts by 4, subtract the total feet, then divide the result by 2 to get the number of birds.
b = (4 * a - total_feet) / 2

# Convert to Fraction for exact representation
a = Fraction(a)
b = Fraction(b)

# Results
a, b
#----- content ends here -----


"""


### Explanation:
1. The problem states that beasts have 6 heads and 4 feet, while birds have 2 heads and 2 feet.
2. The total number of heads is 76, and the total number of feet is 46.
3. Using the ancient method:
   - First, double the total feet, subtract the total heads, and divide by 2 to find the number of beasts (`a`).
   - Then, multiply the number of beasts by 4, subtract the total feet, and divide by 2 to find the number of birds (`b`).

### Output:
The variables `a` and `b` will contain the number of beasts and birds, respectively, as fractions.
"""


"""
Variable 'b' has wrong value. Expected: 7, Actual: -7"""
