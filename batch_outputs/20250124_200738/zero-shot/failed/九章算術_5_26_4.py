"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰：七萬六百六十六尺、太半尺。
負土往來七十步，其二十步上下棚除。棚除二當平道五，踟躕之間十加一，載輸之間三十步，定一返一百四十步。土籠積一尺六寸，秋程人功行五十九里半。問︰人到、積尺、用徒各幾何？
術曰：以一籠積尺乘程行步數為實。往來上下，棚除二當平道五。置定往來步數，十加一，及載輸之間三十步以為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
To solve the problems, we will translate the ancient Chinese math problems into Python code. We'll use the `Fraction` class from the `fractions` module to handle fractional values.

### Problem 1: Volume of the Trapezoidal Prism (盤池)
The problem describes a trapezoidal prism with:
- Top dimensions: 6丈 (length) × 8丈 (width)
- Bottom dimensions: 4丈 (length) × 6丈 (width)
- Depth: 2丈

The formula for the volume of a trapezoidal prism is:
\[
V = \frac{1}{2} \times (A_{\text{top}} + A_{\text{bottom}}) \times \text{depth}
\]
Where \( A_{\text{top}} \) and \( A_{\text{bottom}} \) are the areas of the top and bottom faces.



### Problem 2: Labor and Volume Calculation (負土)
The problem involves calculating the total distance traveled by a person carrying soil, the total volume of soil transported, and the number of workers required.

#### Given:
- One basket holds \( 1 \)尺 \( 6 \)寸 = \( 1 + \frac{6}{10} = \frac{16}{10} = \frac{8}{5} \) 尺³ of soil.
- Total distance traveled per trip: \( 140 \) steps.
- \( 20 \) steps are on a slope, where \( 2 \) slope steps are equivalent to \( 5 \) flat steps.
- \( 10 \) steps are "hesitant" steps, where \( 10 \) hesitant steps are equivalent to \( 11 \) flat steps.
- \( 30 \) steps are for loading/unloading.
- Total distance traveled: \( 59.5 \) 里 (1 里 = 300 步).

#### To Find:
1. Total soil transported (\( a \)) in cubic 尺.
2. Number of workers required (\( b \)).


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions in 丈
top_length = 6
top_width = 8
bottom_length = 4
bottom_width = 6
depth = 2

# Calculate areas of top and bottom faces
A_top = top_length * top_width
A_bottom = bottom_length * bottom_width

# Calculate volume
V = Fraction(1, 2) * (A_top + A_bottom) * depth

# Convert volume to cubic 尺 (1 丈 = 10 尺)
V_cubic_chi = V * 10 * 10 * 10  # Convert 丈^3 to 尺^3

# Result
volume = V_cubic_chi  # Volume in cubic 尺
volume

# Given values
basket_volume = Fraction(8, 5)  # Volume of one basket in cubic 尺
total_distance_li = Fraction(59, 2)  # Total distance in 里
steps_per_li = 300  # Steps in one 里
total_steps = total_distance_li * steps_per_li  # Total steps traveled

# Step conversions
slope_steps = 20
hesitant_steps = 10
loading_steps = 30
flat_steps_equivalent = slope_steps * Fraction(5, 2) + hesitant_steps * Fraction(11, 10) + loading_steps

# Total steps per trip
steps_per_trip = 140
flat_steps_per_trip = steps_per_trip - flat_steps_equivalent

# Soil transported per trip
soil_per_trip = basket_volume * flat_steps_per_trip

# Total soil transported
a = soil_per_trip * total_steps / steps_per_trip

# Number of workers required
b = total_steps / steps_per_trip

# Results
a, b
#----- content ends here -----


"""


### Final Results:
- \( a \): Total soil transported in cubic 尺.
- \( b \): Number of workers required.
"""


"""
Variable 'a' has wrong value. Expected: 204, Actual: 4956
Variable 'b' has wrong value. Expected: 53000/153, Actual: 885/14"""
