"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
荅曰：人到二百一尺、五十分尺之十三。用徒二百五十八人、一萬六十三分人之三千七百四十六。
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
To solve this problem, we need to compute the values of `a` (the distance each person travels in feet) and `b` (the number of workers required). Let's break it down step by step and translate it into Python code.

### Problem Analysis
1. **Volume Calculation**:
   - The volume of the irregular shape is given by the formula for a trapezoidal prism:
     \[
     V = \frac{1}{2} \times (A_{\text{top}} + A_{\text{bottom}}) \times \text{height}
     \]
     where \( A_{\text{top}} \) and \( A_{\text{bottom}} \) are the areas of the top and bottom faces, respectively.

   - \( A_{\text{top}} = \text{top width} \times \text{top length} \)
   - \( A_{\text{bottom}} = \text{bottom width} \times \text{bottom length} \)

   - The height is given as \( 6 \)丈 \( 5 \)尺, which needs to be converted to feet.

2. **Distance Calculation**:
   - The distance each person travels is calculated based on the total volume and the number of trips.

3. **Number of Workers**:
   - The number of workers is determined based on the total distance traveled and the capacity of each worker.

### Python Code

"""


from fractions import Fraction

# Dimensions
top_width = Fraction(2)  # 2 丈
top_length = Fraction(7)  # 7 丈
bottom_width = Fraction(8, 10)  # 8 尺 = 8/10 丈
bottom_length = Fraction(4)  # 4 丈
height = Fraction(6) + Fraction(5, 10)  # 6 丈 5 尺 = 6 + 5/10 丈

# Convert dimensions to feet (1 丈 = 10 尺, 1 尺 = 1 foot)
top_width_ft = top_width * 10
top_length_ft = top_length * 10
bottom_width_ft = bottom_width * 10
bottom_length_ft = bottom_length * 10
height_ft = height * 10

# Calculate areas
area_top = top_width_ft * top_length_ft
area_bottom = bottom_width_ft * bottom_length_ft

# Calculate volume
volume = Fraction(1, 2) * (area_top + area_bottom) * height_ft  # in cubic feet

# Given data for transportation
steps_per_trip = 200  # number of steps per trip
distance_per_step = Fraction(1)  # 1 foot per step
distance_per_trip = steps_per_trip * distance_per_step  # in feet
workers_per_cart = 6  # 6 workers per cart

# Calculate distance each person travels
a = volume / (distance_per_trip * workers_per_cart)  # in feet

# Calculate number of workers required
b = volume / a

# Results
a = a.limit_denominator()  # Simplify fraction
b = b.limit_denominator()  # Simplify fraction

# Output variables
a  # Distance each person travels in feet
b  # Number of workers required


"""


### Explanation of Variables
- `a`: The distance each person travels in feet.
- `b`: The number of workers required.

### Units
- All dimensions are converted to feet for consistency.
- The final results for `a` and `b` are in feet and workers, respectively.


"""


"""
Variable 'a' has wrong value. Expected: 10063/50, Actual: 559/12
Variable 'b' has wrong value. Expected: 2600000/10063, Actual: 1200"""
