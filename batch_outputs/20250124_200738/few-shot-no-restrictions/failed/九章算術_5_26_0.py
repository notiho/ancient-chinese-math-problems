"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰：七萬六百六十六尺、太半尺。
負土往來七十步，其二十步上下棚除。棚除二當平道五，踟躕之間十加一，載輸之間三十步，定一返一百四十步。土籠積一尺六寸，秋程人功行五十九里半。問︰人到、積尺、用徒各幾何？
術曰：以一籠積尺乘程行步數為實。往來上下，棚除二當平道五。置定往來步數，十加一，及載輸之間三十步以為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
### Problem Breakdown:

#### Part 1: Calculating the volume of the pond (積幾何)
The pond has the following dimensions:
- Top width: 6 zhang
- Top length: 8 zhang
- Bottom width: 4 zhang
- Bottom length: 6 zhang
- Depth: 2 zhang

The pond is a frustum of a rectangular pyramid. The formula for the volume of a frustum is:

\[
V = \frac{1}{3} \cdot h \cdot (A_1 + A_2 + \sqrt{A_1 \cdot A_2})
\]

Where:
- \(h\) is the height (depth in this case),
- \(A_1\) is the area of the top rectangle,
- \(A_2\) is the area of the bottom rectangle.

#### Part 2: Calculating the labor required (人到、用徒)
- A single basket (土籠) carries **1 chi 6 cun** of soil.
- The total distance traveled per trip is **140 steps** (往返上下棚除).
- The formula for the distance traveled accounts for:
  - **棚除**: 2 steps are equivalent to 5 steps on flat ground.
  - **踟躕之間**: 10 steps are increased by 1 step.
  - **載輸**: 30 steps are added for loading and unloading.
- The total soil to be moved is the volume of the pond (calculated in Part 1).
- The total distance traveled per trip is **140 steps**.
- The number of workers required is determined by dividing the total soil volume by the amount of soil one person can carry in one trip.

---

### Python Code:


"""

#----- content starts here -----

from math import sqrt
from fractions import Fraction

# Part 1: Calculating the volume of the pond
# Dimensions of the pond
top_width = 6  # zhang
top_length = 8  # zhang
bottom_width = 4  # zhang
bottom_length = 6  # zhang
depth = 2  # zhang

# Convert zhang to chi (1 zhang = 10 chi)
top_width *= 10
top_length *= 10
bottom_width *= 10
bottom_length *= 10
depth *= 10

# Areas of the top and bottom rectangles
A1 = top_width * top_length
A2 = bottom_width * bottom_length

# Volume of the frustum
volume = Fraction(1, 3) * depth * (A1 + A2 + sqrt(A1 * A2))

# Convert volume to chi^3
volume_chi3 = volume

# Part 2: Calculating labor requirements
# Soil per basket (1 chi 6 cun = 1.6 chi)
basket_capacity = 1 + Fraction(6, 10)

# Total distance per trip (140 steps)
total_steps = 140

# Total soil to be moved
total_soil = volume_chi3

# Distance traveled per trip (adjustments for棚除, 踟躕, 載輸)
棚除_adjustment = Fraction(2, 5)  # 2棚除 = 5平道
踟躕_adjustment = Fraction(10 + 1, 10)  # 10加1
載輸_adjustment = 30  # 30 steps for loading/unloading

# Total adjusted steps per trip
adjusted_steps = total_steps * 棚除_adjustment + 踟躕_adjustment + 載輸_adjustment

# Soil moved per trip
soil_per_trip = basket_capacity * adjusted_steps

# Number of trips required
trips_required = total_soil / soil_per_trip

# Number of workers required
workers_required = trips_required

# Results
a = soil_per_trip  # Soil moved per trip (人到)
b = workers_required  # Number of workers required (用徒)

# Output results
print(f"Volume of the pond: {volume_chi3} chi^3")
print(f"One person can move: {a} chi^3 of soil per trip")
print(f"Number of workers required: {b}")
#----- content ends here -----


"""


---

### Explanation of Results:
1. **Volume of the pond**: This is calculated using the frustum formula.
2. **Soil moved per trip**: This is determined by the basket capacity and the adjusted distance traveled per trip.
3. **Number of workers required**: This is calculated by dividing the total soil volume by the amount of soil one person can move in one trip.

Let me know if you need further clarification!
"""


"""
Variable 'a' has wrong value. Expected: 204, Actual: 3484/25
Variable 'b' has wrong value. Expected: 53000/153, Actual: 506.79834240793286"""
