"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
術曰：列一百四十七步以二乘之得二百九十四步以五乘之得一千四百七十步以七除之得二百一十步自相乘得四萬四千一百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a field based on the given steps and the method described.

Here is the Python code:


"""


from fractions import Fraction

# Given data
steps = 147

# Calculations
double_steps = steps * 2
five_times_steps = double_steps * 5
seven_division = Fraction(five_times_steps, 7)
area_in_steps = seven_division * seven_division  # 自相乘 (square the result)
area_in_acres = area_in_steps / 240  # 畝法 (1 畝 = 240 square steps)

# Extracting the integer part (a) and the fractional part (b)
a = int(area_in_acres)  # Integer part (頃)
b = (area_in_acres - a) * 240  # Remaining steps (奇步)

# Results
a, b


"""


### Explanation:
1. **Steps Calculation**: The problem starts with 147 steps. It is doubled, multiplied by 5, and divided by 7 as per the method described.
2. **Area Calculation**: The result is squared to get the area in square steps.
3. **Conversion to 畝**: The area in square steps is divided by 240 to convert it into 畝 (acres).
4. **Extracting Results**: The integer part of the area is the number of 畝 (`a`), and the fractional part is converted back into steps (`b`).

### Output:
The variables `a` and `b` will contain the final results:
- `a` is the number of 畝 (acres).
- `b` is the remaining steps (奇步).
"""


"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 183"""
