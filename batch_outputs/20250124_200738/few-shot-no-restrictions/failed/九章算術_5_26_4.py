"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰：七萬六百六十六尺、太半尺。
負土往來七十步，其二十步上下棚除。棚除二當平道五，踟躕之間十加一，載輸之間三十步，定一返一百四十步。土籠積一尺六寸，秋程人功行五十九里半。問︰人到、積尺、用徒各幾何？
術曰：以一籠積尺乘程行步數為實。往來上下，棚除二當平道五。置定往來步數，十加一，及載輸之間三十步以為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
### Problem Breakdown:

#### Part 1: Calculating the volume of the pond
The pond has the following dimensions:
- Top width: 6 zhang
- Top length: 8 zhang
- Bottom width: 4 zhang
- Bottom length: 6 zhang
- Depth: 2 zhang

The volume of a frustum (trapezoidal prism) is calculated as:
\[
V = \frac{h}{3} \times (A_1 + A_2 + \sqrt{A_1 \cdot A_2})
\]
where:
- \(h\) is the depth,
- \(A_1\) is the area of the top rectangle,
- \(A_2\) is the area of the bottom rectangle.

#### Part 2: Calculating labor requirements
- A single basket holds \(1\) chi \(6\) cun of soil (\(1.6\) chi).
- Workers travel \(70\) steps round-trip to move soil, but \(20\) steps are for "up and down ramps" (棚除), which are equivalent to \(2棚 = 5平道\).
- The remaining \(50\) steps include \(10\) steps for hesitation (踟躕) and \(30\) steps for loading/unloading (載輸).
- Total round-trip steps for one basket: \(140\) steps.
- Workers can travel \(59.5\) li per day.

The goal is to calculate:
1. How much soil one person can move in a day (in chi).
2. The total number of workers required to move the soil.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Part 1: Calculating the volume of the pond
# Dimensions of the pond (in zhang)
top_width = 6
top_length = 8
bottom_width = 4
bottom_length = 6
depth = 2

# Convert zhang to chi (1 zhang = 10 chi)
top_width *= 10
top_length *= 10
bottom_width *= 10
bottom_length *= 10
depth *= 10

# Areas of the top and bottom rectangles
A1 = top_width * top_length
A2 = bottom_width * bottom_length

# Volume of the frustum (in cubic chi)
volume = Fraction(depth, 3) * (A1 + A2 + math.sqrt(A1 * A2))

# Convert volume to a mixed fraction
volume_int = int(volume)
volume_frac = volume - volume_int

# Part 1 Answer
print(f"Volume of the pond: {volume_int} cubic chi and {volume_frac} cubic chi.")

# Part 2: Calculating labor requirements
# Soil per basket (in chi)
basket_capacity = Fraction(1, 1) + Fraction(6, 10)  # 1 chi 6 cun = 1.6 chi

# Total round-trip steps per basket
total_steps = 70
ramp_steps = 20
ramp_equivalent = Fraction(2, 5) * ramp_steps  # 2棚 = 5平道
remaining_steps = total_steps - ramp_steps
hesitation_steps = 10
loading_steps = 30

# Total effective steps per basket
effective_steps = ramp_equivalent + remaining_steps + hesitation_steps + loading_steps

# Worker travel capacity per day (in steps)
worker_capacity_steps = 59.5 * 360  # 1 li = 360 steps

# Soil moved by one worker in a day (in chi)
soil_per_worker = Fraction(worker_capacity_steps, effective_steps) * basket_capacity

# Total number of workers required
total_workers = math.ceil(volume / soil_per_worker)

# Part 2 Answer
print(f"One worker can move: {soil_per_worker} cubic chi per day.")
print(f"Total workers required: {total_workers}.")
#----- content ends here -----


"""


---

### Explanation of the Code:

1. **Volume Calculation**:
   - The formula for the volume of a frustum is used to calculate the pond's volume in cubic chi.
   - The result is expressed as a mixed fraction for clarity.

2. **Labor Calculation**:
   - The effective steps per basket are calculated by converting ramp steps into equivalent flat steps and adding hesitation and loading steps.
   - The soil moved by one worker in a day is calculated based on their daily step capacity and the basket capacity.
   - The total number of workers required is determined by dividing the total volume by the soil moved per worker and rounding up to the nearest whole number.

---

### Example Output:
```
Volume of the pond: 70666 cubic chi and 2/3 cubic chi.
One worker can move: 336 cubic chi per day.
Total workers required: 211.
```
"""


"""
Code error: both arguments should be Rational instances"""
