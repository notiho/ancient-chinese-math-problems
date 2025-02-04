"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
術曰：列一頭廣二十四步半之得一十二步以從三十步乘之得三百六十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a field (田) shaped like a wedge (圭田). The field's dimensions are given as 30 steps long (從三十步) and 24 steps wide at one end (廣二十四步), tapering to 0 steps wide at the other end (無步). The area is to be expressed in terms of 畝 (a traditional Chinese unit of area) and steps (步).

The formula for the area of a wedge-shaped field is essentially the area of a triangle, which is calculated as:

\[
\text{Area} = \frac{\text{Base} \times \text{Height}}{2}
\]

Here, the base is the length of the field (30 steps), and the height is half the width at the wider end (24 steps / 2 = 12 steps).

The area in steps squared is then converted into 畝 and steps using the conversion factor: 1 畝 = 240 steps².

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions of the field
length = 30  # steps
width = 24  # steps

# Calculate the height as half the width
height = Fraction(width, 2)  # steps

# Calculate the area in steps²
area_steps_squared = Fraction(length) * height  # steps²

# Convert the area into 畝 and remaining steps
area_mu = area_steps_squared // 240  # whole 畝
remaining_steps = area_steps_squared % 240  # remaining steps²

# Assign the results to variables
a = area_mu  # 畝
b = remaining_steps  # steps²

# Output the results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Dimensions**: The length and width of the field are given as 30 steps and 24 steps, respectively.
2. **Height Calculation**: The height is half the width at the wider end, which is \( \frac{24}{2} = 12 \) steps.
3. **Area Calculation**: The area in steps² is calculated as \( \text{length} \times \text{height} = 30 \times 12 = 360 \) steps².
4. **Conversion to 畝 and Steps**: The area is converted into 畝 and remaining steps using the conversion factor \( 1 \text{ 畝} = 240 \text{ steps}^2 \). The integer division gives the number of 畝, and the remainder gives the remaining steps².

### Final Output:
The area of the field is:
- \( a = 1 \) 畝
- \( b = 120 \) steps²
"""


"""
"""
