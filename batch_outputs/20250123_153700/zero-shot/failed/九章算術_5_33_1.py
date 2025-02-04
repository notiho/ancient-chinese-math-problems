"""
今有倉廣三丈，袤四丈五尺，容粟一萬斛。問︰高幾何？
術曰：置粟一萬斛積尺為實。廣袤相乘為法。實如法而一，得高尺。
荅曰： a丈 。
"""

"""
To solve this problem, we will calculate the height of the granary (denoted as "a") based on the given dimensions and volume. The problem provides the width (3丈), length (4丈5尺), and volume (1萬斛). We will compute the height using the formula provided.

### Definitions:
1 丈 = 10 尺  
1 萬 = 10,000

### Formula:
Volume = Width × Length × Height  
Height = Volume ÷ (Width × Length)

### Python Code:

"""


from fractions import Fraction

# Given values
width = Fraction(3)  # in 丈
length = Fraction(4) + Fraction(5, 10)  # 4丈5尺 converted to 丈
volume = Fraction(10000)  # 1萬斛

# Calculate height
a = volume / (width * length)

# Result
a  # in 丈


"""


The variable `a` will contain the height of the granary in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 2, Actual: 20000/27"""
