"""
今有倉廣三丈，袤四丈五尺，容粟一萬斛。問︰高幾何？
術曰：置粟一萬斛積尺為實。廣袤相乘為法。實如法而一，得高尺。
荅曰： a丈 。
"""

"""
To solve this problem, we need to calculate the height of a rectangular storage space (倉) given its width (廣), length (袤), and volume (容). The formula for the volume of a rectangular prism is:

\[
\text{Volume} = \text{Width} \times \text{Length} \times \text{Height}
\]

Here are the given values:
- Width (廣) = 3 丈
- Length (袤) = 4 丈 5 尺 = \(4 + \frac{5}{10} = 4.5\) 丈
- Volume (容) = 1 萬斛 = 10,000 斛

We need to find the height (高). Rearranging the formula:

\[
\text{Height} = \frac{\text{Volume}}{\text{Width} \times \text{Length}}
\]

Now, let's write this in Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
width = Fraction(3)  # Width in 丈
length = Fraction(4) + Fraction(5, 10)  # Length in 丈 (4 丈 5 尺)
volume = Fraction(10000)  # Volume in 斛

# Calculate height
a = volume / (width * length)  # Height in 丈

# The result is stored in variable 'a'
a
#----- content ends here -----


"""


The variable `a` will contain the height in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 2, Actual: 20000/27"""
