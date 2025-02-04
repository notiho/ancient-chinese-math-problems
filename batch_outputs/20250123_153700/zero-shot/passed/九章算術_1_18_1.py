"""
今有田廣七分步之四，從五分步之三。問：為田幾何？
乘分術曰：母相乘為法，子相乘為實，實如法而一。
荅曰： a步 。
"""

"""
To solve this problem, we will use the given method of multiplying the numerators (子) and denominators (母) of the fractions to compute the area of the field.

The problem states:
- One part of the field is \( \frac{4}{7} \) (七分步之四).
- Another part of the field is \( \frac{3}{5} \) (五分步之三).
- The total area of the field is the product of these two fractions.

We will compute the result in Python using the `Fraction` class.


"""


from fractions import Fraction

# Define the fractions
part1 = Fraction(4, 7)  # 七分步之四
part2 = Fraction(3, 5)  # 五分步之三

# Multiply the fractions
a = part1 * part2  # 荅曰：a步

# The result is stored in the variable 'a'
a


"""


The variable `a` will contain the total area of the field in terms of steps (步).
"""


"""
"""
