"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰：七萬六百六十六尺、太半尺。
負土往來七十步，其二十步上下棚除。棚除二當平道五，踟躕之間十加一，載輸之間三十步，定一返一百四十步。土籠積一尺六寸，秋程人功行五十九里半。問︰人到、積尺、用徒各幾何？
術曰：以一籠積尺乘程行步數為實。往來上下，棚除二當平道五。置定往來步數，十加一，及載輸之間三十步以為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
To solve the problems, we will translate the ancient Chinese math problems into Python code. We'll use the `Fraction` class from the `fractions` module to handle fractional values.

### Problem 1: Volume of the Pond
The pond has an upper surface with dimensions 6丈 by 8丈, a lower surface with dimensions 4丈 by 6丈, and a depth of 2丈. The volume is calculated using the formula for the volume of a truncated prism:
\[
V = \frac{1}{3} \times h \times (A_1 + A_2 + \sqrt{A_1 \times A_2})
\]
where \(A_1\) and \(A_2\) are the areas of the upper and lower surfaces, and \(h\) is the depth.



### Problem 2: Labor and Volume Transport
The problem involves calculating the total distance traveled by one person, the total volume of soil transported, and the number of workers required.

#### Given:
- Soil basket capacity: \(1\)尺\(6\)寸 = \(1 + \frac{6}{10} = \frac{16}{10} = \frac{8}{5}\) 尺³
- Total distance per round trip: \(140\) steps
- Conversion factors:
  - \(棚除\): \(2\)棚除 = \(5\)平道
  - \(踟躕之間\): \(10 + 1 = 11\)
  - \(載輸之間\): \(30\)
- Total distance covered: \(59.5\)里 = \(59.5 \times 300 = 17850\) steps (1里 = 300 steps)

#### Calculations:
1. Total soil volume transported by one person:
   \[
   \text{Volume per person} = \text{Basket capacity} \times \text{Total steps covered}
   \]
2. Total distance per round trip:
   \[
   \text{Round trip distance} = \text{棚除 factor} + \text{踟躕之間} + \text{載輸之間}
   \]
3. Number of workers required:
   \[
   \text{Workers} = \frac{\text{Total soil volume}}{\text{Volume per person}}
   \]


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions of the pond
upper_length = Fraction(6)  # in 丈
upper_width = Fraction(8)   # in 丈
lower_length = Fraction(4)  # in 丈
lower_width = Fraction(6)   # in 丈
depth = Fraction(2)         # in 丈

# Calculate areas of the upper and lower surfaces
A1 = upper_length * upper_width  # in 丈²
A2 = lower_length * lower_width  # in 丈²

# Calculate the volume of the pond
V = Fraction(1, 3) * depth * (A1 + A2 + (A1 * A2).sqrt())  # in 丈³

# Convert volume to cubic 尺 (1 丈³ = 1000 尺³)
V_cubic_chi = V * 1000

# Final answer
volume = V_cubic_chi

# Given data
basket_capacity = Fraction(8, 5)  # in 尺³
total_steps = Fraction(59.5 * 300)  # in steps
round_trip_distance = Fraction(140)  # in steps

# Factors
pengchu_factor = Fraction(2, 5)  # 2棚除 = 5平道
chichu_factor = Fraction(11)  # 踟躕之間
zaisu_factor = Fraction(30)  # 載輸之間

# Total round trip distance
round_trip_distance = pengchu_factor + chichu_factor + zaisu_factor

# Volume transported by one person
volume_per_person = basket_capacity * total_steps

# Total soil volume
total_volume = volume_per_person * round_trip_distance

# Number of workers required
workers = total_volume / volume_per_person

# Final answers
a = volume_per_person  # in 尺³
b = workers  # number of workers
#----- content ends here -----


"""


### Final Results:
- `a`: Total distance traveled by one person in 尺.
- `b`: Number of workers required.
"""


"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
