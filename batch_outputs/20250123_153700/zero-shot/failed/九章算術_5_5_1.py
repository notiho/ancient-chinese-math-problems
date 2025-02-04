"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a trapezoidal prism (a ditch or trench). Here's the Python code:


"""


from fractions import Fraction

# Given dimensions
top_width = Fraction(1, 1) + Fraction(5, 10)  # 1丈5尺 = 1 + 5/10丈
bottom_width = Fraction(1, 1)  # 1丈
depth = Fraction(5, 10)  # 5尺 = 5/10丈
length = Fraction(7, 1)  # 7丈

# Formula: ((top_width + bottom_width) / 2) * depth * length
average_width = (top_width + bottom_width) / 2
volume = average_width * depth * length

# Convert volume to 尺 (1丈 = 10尺)
a = volume * 10

# Output the result
a


"""


### Explanation:
1. **Units Conversion**: All dimensions are given in 丈 and 尺. Since 1丈 = 10尺, we ensure the final result is in 尺.
2. **Formula**: The formula for the volume of a trapezoidal prism is:
   \[
   \text{Volume} = \left(\frac{\text{Top Width} + \text{Bottom Width}}{2}\right) \times \text{Depth} \times \text{Length}
   \]
3. **Implementation**: The code calculates the average width, multiplies it by the depth and length, and converts the result to 尺.

### Final Answer:
The variable `a` will contain the volume in 尺.
"""


"""
Variable 'a' has wrong value. Expected: 4375, Actual: 175/4"""
