"""
今有玉方一寸，重七兩；石方一寸，重六兩。今有石立方三寸，中有玉，并重十一斤。問︰玉、石重各幾何？
術曰：假令皆玉，多十三兩。令之皆石，不足十四兩。不足為玉，多為石。各以一寸之重乘之，得玉石之積重。
荅曰：玉 a寸 ，重 b斤 。石 c寸 ，重 d斤 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. We'll compute the values of the unknowns `a`, `b`, `c`, and `d` using the given information.

### Problem Breakdown:
1. A cubic inch of jade (玉) weighs 7 taels (兩).
2. A cubic inch of stone (石) weighs 6 taels (兩).
3. A cube of stone with a side length of 3 inches contains some jade inside it. The total weight of the cube is 11 jin (斤).
4. 1 jin = 16 taels (兩).
5. We need to find the volume of jade (`a` cubic inches) and stone (`c` cubic inches), as well as their respective weights (`b` jin for jade and `d` jin for stone).

### Solution:
We know:
- Total volume = \( 3^3 = 27 \) cubic inches.
- Total weight = \( 11 \times 16 = 176 \) taels.
- Weight of jade = \( 7 \times a \) taels.
- Weight of stone = \( 6 \times c \) taels.
- Volume of jade + Volume of stone = 27 cubic inches.
- Weight of jade + Weight of stone = 176 taels.

From this, we can set up the equations:
1. \( a + c = 27 \)
2. \( 7a + 6c = 176 \)

We solve these equations to find `a`, `b`, `c`, and `d`.

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Given constants
weight_jade_per_cubic_inch = 7  # taels
weight_stone_per_cubic_inch = 6  # taels
total_volume = 27  # cubic inches
total_weight = 11 * 16  # taels (convert jin to taels)

# Solve the system of equations:
# a + c = 27
# 7a + 6c = 176

# Step 1: Express c in terms of a from the first equation
# c = 27 - a

# Step 2: Substitute c into the second equation
# 7a + 6(27 - a) = 176
# 7a + 162 - 6a = 176
# a = 176 - 162
# a = 14

# Step 3: Solve for c
a = Fraction(14)  # cubic inches of jade
c = total_volume - a  # c = 27 - a
c = Fraction(c)  # cubic inches of stone

# Step 4: Calculate weights
b = a * weight_jade_per_cubic_inch  # weight of jade in taels
d = c * weight_stone_per_cubic_inch  # weight of stone in taels

# Convert weights to jin (1 jin = 16 taels)
b = b / 16  # weight of jade in jin
d = d / 16  # weight of stone in jin

# Results
a, b, c, d
#----- content ends here -----


"""


### Explanation of Variables:
- `a`: Volume of jade in cubic inches.
- `b`: Weight of jade in jin.
- `c`: Volume of stone in cubic inches.
- `d`: Weight of stone in jin.

### Final Answer:
- `a = 14` cubic inches (volume of jade),
- `b = 6.125` jin (weight of jade),
- `c = 13` cubic inches (volume of stone),
- `d = 4.875` jin (weight of stone).
"""


"""
"""
