"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
答曰：弦 a 。
"""

"""
This problem involves a classic right triangle relationship where the hypotenuse (弦), the base (股), and the height (句) are related by the Pythagorean theorem. Let's break it down step by step:

### Problem:
- The product of the base (股) and the height (句) is given as \( 4036 \frac{1}{5} \) (or \( \frac{20181}{5} \)).
- The base (股) is \( \frac{1}{5} \) less than the hypotenuse (弦).
- We are tasked to find the hypotenuse (弦).

---

### Solution in Python:


"""


from fractions import Fraction

# Given values
product_of_base_and_height = Fraction(20181, 5)  # 股 * 句 = 4036 1/5
difference_between_hypotenuse_and_base = Fraction(1, 5)  # 弦 - 股 = 1/5

# Let the hypotenuse (弦) be x
# Then the base (股) is x - 1/5
# Using the Pythagorean theorem: 弦^2 = 股^2 + 句^2
# 股 * 句 is given, so 句 = 股 * 句 / 股

# Step 1: Express 股 and 句
# 股 = x - 1/5
# 句 = product_of_base_and_height / 股

# Step 2: Substitute into the Pythagorean theorem
# x^2 = 股^2 + 句^2
# x^2 = (x - 1/5)^2 + (product_of_base_and_height / (x - 1/5))^2

# Step 3: Solve for x (弦)

# Define a function to solve for x
def find_hypotenuse():
    for i in range(1, 10000):  # Iterate through possible values (approximation)
        x = Fraction(i, 1)  # Hypotenuse as a fraction
        base = x - difference_between_hypotenuse_and_base  # 股 = 弦 - 1/5
        if base <= 0:
            continue
        height = product_of_base_and_height / base  # 句 = 股 * 句 / 股
        if x**2 == base**2 + height**2:  # Check Pythagorean theorem
            return x

# Find the hypotenuse
a = find_hypotenuse()
a


"""


### Explanation:
1. We use the relationship between the hypotenuse (弦), base (股), and height (句) via the Pythagorean theorem.
2. The base (股) is expressed as \( x - \frac{1}{5} \), where \( x \) is the hypotenuse.
3. The height (句) is calculated as \( \frac{\text{product\_of\_base\_and\_height}}{\text{base}} \).
4. We substitute these into the Pythagorean theorem and solve for \( x \) iteratively.

### Final Answer:
The hypotenuse \( a \) will be the result of the function `find_hypotenuse()`.
"""


"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: None"""
