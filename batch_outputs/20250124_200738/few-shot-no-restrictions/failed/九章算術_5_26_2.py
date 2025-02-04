"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰：七萬六百六十六尺、太半尺。
負土往來七十步，其二十步上下棚除。棚除二當平道五，踟躕之間十加一，載輸之間三十步，定一返一百四十步。土籠積一尺六寸，秋程人功行五十九里半。問︰人到、積尺、用徒各幾何？
術曰：以一籠積尺乘程行步數為實。往來上下，棚除二當平道五。置定往來步數，十加一，及載輸之間三十步以為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
### Part 1: Calculating the volume of the irregular pond (盤池)

The pond has an irregular shape with different dimensions for the top and bottom. The formula for the volume of a frustum (truncated prism) is used:

\[
V = \frac{1}{6} \cdot \text{depth} \cdot \left(\text{top area} + \text{bottom area} + \sqrt{\text{top area} \cdot \text{bottom area}}\right)
\]

#### Step 1: Calculate the top and bottom areas
- Top dimensions: width = 6 丈, length = 8 丈
- Bottom dimensions: width = 4 丈, length = 6 丈
- Depth = 2 丈

1 丈 = 10 尺 (convert all dimensions to 尺).



The volume of the pond is approximately **70666 尺 and a little over half a 尺**.

---

### Part 2: Calculating labor requirements for moving the soil

#### Step 1: Given data
- **土籠積**: Each basket holds 1 尺 6 寸 = \(1 + \frac{6}{10} = \frac{16}{10} = \frac{8}{5}\) 尺.
- **秋程人功行**: Each person can travel 59.5 里 in a day.
- **往來步數**: 70 步 for a round trip.
- **棚除**: 20 步 for loading/unloading. Each棚除 2 步 is equivalent to 5 平道步.
- **踟躕之間**: 10 加 1 (10 hesitation steps add 1 step).
- **載輸之間**: 30 步 for carrying the load.
- **定一返**: 140 步 for a full round trip.

#### Step 2: Calculate the number of steps per round trip
The total number of steps for a round trip is:

\[
\text{Total steps} = \text{定一返} + \text{棚除 adjustment} + \text{踟躕 adjustment} + \text{載輸 adjustment}
\]



#### Step 3: Calculate the soil moved by one person in one day
The total soil moved by one person in one day is:

\[
\text{Soil moved per person} = \text{basket volume} \times \frac{\text{daily distance}}{\text{total steps per trip}}
\]



#### Step 4: Calculate the number of workers required
The total number of workers required is:

\[
\text{Number of workers} = \frac{\text{total soil volume}}{\text{soil moved per person}}
\]



#### Final Answer:

"""

#----- content starts here -----

from fractions import Fraction
import math

# Dimensions in 尺
top_width = 6 * 10
top_length = 8 * 10
bottom_width = 4 * 10
bottom_length = 6 * 10
depth = 2 * 10

# Calculate areas
top_area = top_width * top_length
bottom_area = bottom_width * bottom_length

# Frustum volume formula
volume = Fraction(1, 6) * depth * (top_area + bottom_area + math.sqrt(top_area * bottom_area))

# Convert to 尺
volume_in_chi = volume

# Given data
basket_volume = Fraction(8, 5)  # Each basket holds 1 尺 6 寸
daily_distance = 59.5 * 180  # Convert 里 to 步 (1 里 = 180 步)
round_trip_steps = 140  # 定一返
棚除_adjustment = Fraction(20, 2) * Fraction(5, 2)  # 棚除: 2 步 = 5 平道步
踟躕_adjustment = Fraction(10, 1) + 1  # 踟躕之間: 10 加 1
載輸_adjustment = 30  # 載輸之間

# Total steps per round trip
total_steps_per_trip = round_trip_steps + 棚除_adjustment + 踟躕_adjustment + 載輸_adjustment

# Soil moved per person in 尺
soil_moved_per_person = basket_volume * (daily_distance / total_steps_per_trip)

# Total soil volume (from Part 1)
total_soil_volume = volume_in_chi

# Number of workers required
workers_required = total_soil_volume / soil_moved_per_person

a = soil_moved_per_person  # 尺 moved per person
b = math.ceil(workers_required)  # Number of workers (round up to the nearest whole number)
#----- content ends here -----


"""


- **人到 a 尺**: Each person moves approximately \(a\) 尺 of soil in one day.
- **用徒 b 人**: Approximately \(b\) workers are required to move all the soil.
"""


"""
Variable 'a' has wrong value. Expected: 204, Actual: 83.18446601941747
Variable 'b' has wrong value. Expected: 53000/153, Actual: 425"""
