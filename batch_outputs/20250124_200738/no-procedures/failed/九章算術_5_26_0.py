"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰：七萬六百六十六尺、太半尺。
負土往來七十步，其二十步上下棚除。棚除二當平道五，踟躕之間十加一，載輸之間三十步，定一返一百四十步。土籠積一尺六寸，秋程人功行五十九里半。問︰人到、積尺、用徒各幾何？
荅曰：人到 a尺 。用徒 b人 。
"""

"""
This problem involves calculating the volume of a trapezoidal pond and then determining the labor required to transport the excavated soil. Let's break it into parts.

---

### Part 1: Calculate the volume of the pond

The pond is trapezoidal in shape, with the following dimensions:
- Top width: 6 zhang
- Top length: 8 zhang
- Bottom width: 4 zhang
- Bottom length: 6 zhang
- Depth: 2 zhang

The formula for the volume of a trapezoidal prism is:

\[
\text{Volume} = \frac{\text{Top Area} + \text{Bottom Area}}{2} \times \text{Depth}
\]

1 zhang = 10 chi, so we convert all dimensions to chi.

---

### Part 2: Labor calculation

The problem also provides details about the transportation of soil:
- Round trip distance: 140 bu
- Soil basket capacity: 1 chi 6 cun (convert to chi: \(1 + \frac{6}{10} = 1.6\) chi)
- Worker efficiency: 59.5 li per day (1 li = 300 bu)

We need to calculate:
1. Total volume of soil transported in chi³.
2. Number of trips required.
3. Number of workers needed.

---

Here is the Python code to solve the problem:


"""

#----- content starts here -----

from fractions import Fraction

# Part 1: Calculate the volume of the pond
# Dimensions in zhang
top_width = 6
top_length = 8
bottom_width = 4
bottom_length = 6
depth = 2

# Convert dimensions to chi (1 zhang = 10 chi)
top_width *= 10
top_length *= 10
bottom_width *= 10
bottom_length *= 10
depth *= 10

# Calculate top and bottom areas
top_area = top_width * top_length
bottom_area = bottom_width * bottom_length

# Calculate volume of the pond
volume = Fraction((top_area + bottom_area), 2) * depth  # in chi³

# Part 2: Labor calculation
# Soil basket capacity in chi³
basket_capacity = Fraction(16, 10)  # 1 chi 6 cun = 1.6 chi³

# Round trip distance in bu
round_trip_distance = 140

# Worker efficiency in bu per day (59.5 li = 59.5 * 300 bu)
worker_efficiency = Fraction(59.5 * 300)

# Total trips required to transport all soil
total_trips = volume / basket_capacity

# Total distance traveled for all trips
total_distance = total_trips * round_trip_distance

# Number of workers needed
workers_needed = total_distance / worker_efficiency

# Results
a = volume  # Total volume of soil in chi³
b = workers_needed  # Number of workers needed

print(f"Total volume of soil (chi³): {a}")
print(f"Number of workers needed: {b}")
#----- content ends here -----


"""


---

### Explanation of Results:
1. `a` represents the total volume of soil in chi³.
2. `b` represents the number of workers needed to transport the soil.

This calculation ensures that the excavation and labor requirements are accurately determined based on the given dimensions and conditions.
"""


"""
Variable 'a' has wrong value. Expected: 204, Actual: 72000
Variable 'b' has wrong value. Expected: 53000/153, Actual: 6000/17"""
