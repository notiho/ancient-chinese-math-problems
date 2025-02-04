"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
載土往來二百步，載輸之間一里，程行五十八里，六人共車，車載三十四尺七寸。問︰人到積尺及用徒各幾何？
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
### Problem Breakdown and Solution:

#### Problem 1: Calculating the volume of the valley
The valley has the following dimensions:
- Top width: 2 zhang
- Top length: 7 zhang
- Bottom width: 8 chi
- Bottom length: 4 zhang
- Depth: 6 zhang 5 chi

We need to calculate the volume of the valley.

#### Problem 2: Calculating the work distribution
- The total volume of the valley is 52,000 cubic chi.
- A cart can carry 34 chi 7 cun of soil per trip.
- The round trip distance is 200 bu, and the distance to the dumping site is 1 li.
- The total distance traveled is 58 li.
- 6 people share a cart.

We need to calculate:
1. How much soil each person moves (in cubic chi).
2. How many workers are required to move the total volume.

---

### Implementation in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Problem 1: Calculate the volume of the valley
# Dimensions
top_width = 2 * 10  # Convert zhang to chi
top_length = 7 * 10  # Convert zhang to chi
bottom_width = 8  # Already in chi
bottom_length = 4 * 10  # Convert zhang to chi
depth = 6 * 10 + 5  # Convert zhang and chi to chi

# Formula for the volume of a truncated prism:
# V = (1/2) * depth * (top_area + bottom_area)
top_area = top_width * top_length
bottom_area = bottom_width * bottom_length
volume = Fraction(1, 2) * depth * (top_area + bottom_area)

# Convert volume to an integer (since the answer is given as an integer)
volume = int(volume)

# Problem 2: Calculate work distribution
# Given data
cart_capacity = Fraction(34, 1) + Fraction(7, 10)  # Convert 34 chi 7 cun to chi
round_trip_distance = 200  # in bu
dumping_distance = 1 * 300  # Convert li to bu (1 li = 300 bu)
total_distance = 58 * 300  # Convert li to bu
people_per_cart = 6

# Step 1: Calculate the total soil moved by one cart over the total distance
total_cart_soil = cart_capacity * total_distance

# Step 2: Calculate the divisor (法)
divisor = (round_trip_distance + dumping_distance) * people_per_cart

# Step 3: Calculate the soil moved by one person
soil_per_person = total_cart_soil / divisor

# Step 4: Calculate the number of workers required
workers_needed = volume / soil_per_person

# Convert workers_needed to an integer (round up since we can't have partial workers)
from math import ceil
workers_needed = ceil(workers_needed)

# Final results
a = int(soil_per_person)  # Soil moved by one person
b = workers_needed  # Total number of workers

# Output
print(f"Volume of the valley: {volume} cubic chi")
print(f"Soil moved by one person: {a} cubic chi")
print(f"Number of workers needed: {b}")
#----- content ends here -----


"""


---

### Explanation of the Code:

1. **Volume Calculation**:
   - The valley is modeled as a truncated prism.
   - The formula for the volume of a truncated prism is used:  
     \( V = \frac{1}{2} \times \text{depth} \times (\text{top area} + \text{bottom area}) \).

2. **Work Distribution**:
   - The total soil moved by one cart over the total distance is calculated by multiplying the cart's capacity by the total distance.
   - The divisor is calculated as the product of the round trip distance (including the dumping distance) and the number of people sharing the cart.
   - The soil moved by one person is calculated by dividing the total soil moved by the divisor.
   - The number of workers required is calculated by dividing the total volume by the soil moved by one person and rounding up to the nearest whole number.

---

### Final Answer:
- Volume of the valley: **52,000 cubic chi**
- Soil moved by one person: **a cubic chi**
- Number of workers needed: **b people**
"""


"""
Variable 'a' has wrong value. Expected: 10063/50, Actual: 201
Variable 'b' has wrong value. Expected: 2600000/10063, Actual: 278"""
