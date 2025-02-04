"""
又有邪田，正廣六十五步，一畔從一百步，一畔從七十二步。問：為田幾何？
術曰：并兩邪而半之，以乘正從若廣。又可半正從若廣，以乘并。畝法而一。
荅曰： a畝 。
"""

"""
To solve this problem, we need to calculate the area of an irregular quadrilateral field (邪田). The field has one side (正廣) of 65 steps, one diagonal (正從) of 100 steps, and the other diagonal (正從) of 72 steps. The formula provided in the problem states that we should:

1. Add the two diagonals (正從) together and divide by 2 (average of the diagonals).
2. Multiply this average by the side 正廣 (65 steps).
3. Convert the result into 畝 (a traditional Chinese unit of area).

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Given values
正廣 = 65  # in steps
正從1 = 100  # in steps
正從2 = 72  # in steps

# Step 1: Average the two diagonals
average_diagonal = Fraction(正從1 + 正從2, 2)

# Step 2: Multiply the average diagonal by 正廣
area_in_steps = average_diagonal * 正廣

# Step 3: Convert steps^2 to 畝 (1 畝 = 240 steps^2)
a = area_in_steps / 240

# The result is stored in variable 'a'


"""


The variable `a` will contain the area of the field in 畝.
"""


"""
"""
