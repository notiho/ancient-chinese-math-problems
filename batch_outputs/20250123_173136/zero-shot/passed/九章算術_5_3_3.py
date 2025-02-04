"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a trapezoidal prism (a shape with a trapezoidal cross-section). Here's the Python code:


"""


from fractions import Fraction

# Given dimensions
lower_width = Fraction(2 * 10)  # Convert 2丈 to 尺 (1丈 = 10尺)
upper_width = Fraction(8)      # 8尺
height = Fraction(4)           # 4尺
length = Fraction(12 * 10 + 7) # Convert 12丈7尺 to 尺

# Calculation
average_width = (lower_width + upper_width) / 2  # Average of lower and upper widths
cross_section_area = average_width * height     # Cross-sectional area
volume = cross_section_area * length            # Volume of the prism

# Solution
a = volume


"""


### Explanation:
1. **Conversion of units**: The problem uses ancient Chinese units of measurement where 1丈 = 10尺. We convert all dimensions to 尺 for consistency.
2. **Average width**: The formula requires taking the average of the lower and upper widths.
3. **Cross-sectional area**: Multiply the average width by the height to get the area of the trapezoidal cross-section.
4. **Volume**: Multiply the cross-sectional area by the length to get the total volume.

### Final Answer:
The variable `a` contains the volume in 尺.
"""


"""
"""
