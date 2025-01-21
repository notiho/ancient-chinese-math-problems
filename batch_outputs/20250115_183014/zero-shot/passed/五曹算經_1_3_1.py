"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
術曰：列一頭廣二十四步半之得一十二步以從三十步乘之得三百六十步以畝法除之即得。
答曰： a畝 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a trapezoidal field (圭田). The formula for the area of a trapezoid is:

\[
\text{Area} = \frac{\text{Base1} + \text{Base2}}{2} \times \text{Height}
\]

Here, the bases are 30 steps and 0 steps, and the height is 24 steps.

The area will be expressed in 畝 (mu) and 步 (bu). The conversion factor is \( 240 \, \text{bu} = 1 \, \text{mu} \).

### Python Code:

"""


from fractions import Fraction

# Given dimensions
base1 = 30  # steps
base2 = 0   # steps
height = 24  # steps

# Calculate the area in steps²
area_steps_squared = Fraction(base1 + base2, 2) * height

# Convert to 畝 (mu) and 步 (bu)
mu = area_steps_squared // 240  # 1 畝 = 240 步²
bu = area_steps_squared % 240   # Remaining 步²

# Assign the results to variables
a = mu
b = bu

# Results
a, b


"""


### Explanation:
1. The bases of the trapezoid are 30 steps and 0 steps.
2. The height is 24 steps.
3. The area in steps² is calculated as \( \frac{(30 + 0)}{2} \times 24 \).
4. The area is converted to 畝 (mu) and 步 (bu) using the conversion \( 240 \, \text{bu} = 1 \, \text{mu} \).
5. The results are stored in variables `a` (畝) and `b` (步).
"""


"""
"""
