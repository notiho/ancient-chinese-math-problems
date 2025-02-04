"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
載土往來二百步，載輸之間一里，程行五十八里，六人共車，車載三十四尺七寸。問︰人到積尺及用徒各幾何？
荅曰：人到 a尺 。用徒 b人 。
"""

"""
This problem involves calculating the volume of a trapezoidal valley and determining the labor required to transport the soil. Let's break it into two parts:

---

### Part 1: Calculate the volume of the valley
The valley is trapezoidal in shape, so its volume can be calculated using the formula for the volume of a trapezoidal prism:

\[
\text{Volume} = \frac{1}{2} \times (\text{Top Area} + \text{Bottom Area}) \times \text{Depth}
\]

- Top width = 2 zhang = 20 chi
- Top length = 7 zhang = 70 chi
- Bottom width = 8 chi
- Bottom length = 4 zhang = 40 chi
- Depth = 6 zhang 5 chi = 65 chi

---

### Part 2: Calculate labor requirements
- Total volume = 52,000 chi³ (given in the problem).
- Each cart carries 34 chi 7 cun = \( 34 + \frac{7}{10} = \frac{347}{10} \) chi³.
- 6 people share 1 cart.
- Distance per trip = 1 li = 300 bu.
- Total distance = 58 li = \( 58 \times 300 = 17,400 \) bu.
- Total trips required = \( \frac{\text{Total Volume}}{\text{Volume per Cart}} \).
- Total people required = \( \text{Total Trips} \times 6 \).

---

### Python Code


"""

#----- content starts here -----

from fractions import Fraction

# Part 1: Calculate the volume of the valley
top_width = 20  # chi
top_length = 70  # chi
bottom_width = 8  # chi
bottom_length = 40  # chi
depth = 65  # chi

# Top area and bottom area
top_area = top_width * top_length
bottom_area = bottom_width * bottom_length

# Volume of the valley
volume = Fraction(1, 2) * (top_area + bottom_area) * depth
assert volume == 52000  # Confirm the given volume matches the calculation

# Part 2: Calculate labor requirements
cart_volume = Fraction(347, 10)  # chi³
total_volume = 52000  # chi³
people_per_cart = 6
distance_per_trip = 300  # bu
total_distance = 58 * distance_per_trip  # bu

# Total trips required
total_trips = total_volume / cart_volume

# Total people required
total_people = total_trips * people_per_cart

# Distance per person
distance_per_person = total_distance * total_trips / total_people

# Results
a = distance_per_person  # Distance per person in bu
b = total_people  # Total people required

# Output results
a, b
#----- content ends here -----


"""


---

### Explanation of Results
- `a`: The distance each person needs to travel (in bu).
- `b`: The total number of people required for the task.
"""


"""
Code error: """
