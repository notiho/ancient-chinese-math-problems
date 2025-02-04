"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
答曰：弦 a 。
"""

"""
This problem involves a right triangle where the product of the two legs (the "句" and "股") is given, and the relationship between one leg ("股") and the hypotenuse ("弦") is also provided. The goal is to find the length of the hypotenuse.

### Problem Breakdown:
1. The product of the two legs is \( 4036 \frac{1}{5} \), or \( \frac{20181}{5} \) when converted to a fraction.
2. The "股" (one leg) is shorter than the hypotenuse ("弦") by \( \frac{1}{5} \).
3. Using the Pythagorean theorem and the given relationships, we solve for the hypotenuse.

Here is the Python code to solve the problem:


"""


from fractions import Fraction

# Given values
product_of_legs = Fraction(20181, 5)  # 4036 1/5 converted to an improper fraction
difference_between_hypotenuse_and_leg = Fraction(1, 5)  # 股 is shorter than 弦 by 1/5

# Let 弦 = x, 股 = x - 1/5, and 句 = y
# From the problem, 股 * 句 = 4036 1/5
# 股 = x - 1/5, so (x - 1/5) * y = 4036 1/5
# From the Pythagorean theorem: 弦^2 = 股^2 + 句^2
# Substituting 股 = x - 1/5 and 句 = product_of_legs / 股, we solve for 弦 (x).

# Step 1: Express 股 and 句 in terms of 弦 (x)
def solve_hypotenuse():
    for x in range(1, 10000):  # Iterate over possible hypotenuse values
        x = Fraction(x)  # Treat x as a fraction
        股 = x - difference_between_hypotenuse_and_leg  # 股 = 弦 - 1/5
        if 股 <= 0:
            continue  # 股 must be positive
        句 = product_of_legs / 股  # 句 = product_of_legs / 股
        # Check if the Pythagorean theorem holds: 弦^2 = 股^2 + 句^2
        if x**2 == 股**2 + 句**2:
            return x

# Solve for the hypotenuse
a = solve_hypotenuse()
a


"""


### Explanation:
1. **股 and 句 Relationship**: We express 股 as \( x - \frac{1}{5} \) and 句 as \( \frac{\text{product\_of\_legs}}{\text{股}} \).
2. **Pythagorean Theorem**: Using \( \text{弦}^2 = \text{股}^2 + \text{句}^2 \), we check for the value of \( x \) (the hypotenuse) that satisfies the equation.
3. **Iterative Solution**: We iterate over possible values of \( x \) (the hypotenuse) and check if the equation holds.

### Answer:
The value of \( a \) (the hypotenuse) will be computed by the code above.
"""


"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: None"""
