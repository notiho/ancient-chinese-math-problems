"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of the "盤池" (a type of trapezoidal prism) using the given formula. The formula involves doubling the lengths of the top and bottom, multiplying by their respective widths, summing the results, and then multiplying by the depth. Finally, the result is divided by 6.

The dimensions of the "盤池" are:
- Top length (上袤): 6丈
- Top width (上廣): 6丈
- Bottom length (下袤): 4丈
- Bottom width (下廣): 4丈
- Depth (深): 2丈

We will compute the volume step by step.

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Dimensions in 丈
top_length = 6  # 上袤
top_width = 6   # 上廣
bottom_length = 4  # 下袤
bottom_width = 4   # 下廣
depth = 2  # 深

# Step 1: Double the lengths
double_top_length = 2 * top_length
double_bottom_length = 2 * bottom_length

# Step 2: Multiply by their respective widths
top_area = double_top_length * top_width
bottom_area = double_bottom_length * bottom_width

# Step 3: Sum the areas
total_area = top_area + bottom_area

# Step 4: Multiply by the depth
volume = total_area * depth

# Step 5: Divide by 6
a = Fraction(volume, 6)  # Volume in cubic 丈

# The answer is stored in variable 'a'
#----- content ends here -----


"""


### Explanation of the Code:
1. **Doubling the lengths**: The formula requires doubling the top and bottom lengths.
2. **Calculating areas**: Multiply the doubled lengths by their respective widths to get the areas of the top and bottom.
3. **Summing the areas**: Add the two areas together.
4. **Multiplying by depth**: Multiply the summed area by the depth of the pool.
5. **Dividing by 6**: Finally, divide the result by 6 to get the final volume.

### Final Answer:
The volume of the "盤池" is stored in the variable `a` as a `Fraction` in cubic 丈.
"""


"""
Variable 'a' has wrong value. Expected: 212000/3, Actual: 104/3"""
