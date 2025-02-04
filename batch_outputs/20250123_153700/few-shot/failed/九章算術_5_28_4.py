"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
荅曰：人到二百一尺、五十分尺之十三。用徒二百五十八人、一萬六十三分人之三千七百四十六。
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
This problem involves calculating the volume of a valley and determining how far a person can carry the load, as well as the number of workers required. Let's break it down step by step.

### Problem Setup
1. **Valley Dimensions**:
   - Top width: 2 zhang (20 chi)
   - Top length: 7 zhang (70 chi)
   - Bottom width: 8 chi
   - Bottom length: 4 zhang (40 chi)
   - Depth: 6 zhang 5 chi (65 chi)

2. **Volume Calculation**:
   The valley is a frustum of a rectangular pyramid. The formula for the volume of a frustum is:
   \[
   V = \frac{h}{3} \times (A_1 + A_2 + \sqrt{A_1 \times A_2})
   \]
   where:
   - \(h\) is the depth,
   - \(A_1\) is the area of the top rectangle,
   - \(A_2\) is the area of the bottom rectangle.

3. **Human Work Calculation**:
   - A cart's capacity is given in chi.
   - The number of steps (distance) a person can carry a load is calculated based on the cart's capacity and the total distance traveled.
   - The total number of workers required is determined by dividing the total volume by the amount each person can carry.

---

### Solution in Python Code


"""


from fractions import Fraction
import math

# Dimensions of the valley
top_width = 20  # Top width in chi (2 zhang = 20 chi)
top_length = 70  # Top length in chi (7 zhang = 70 chi)
bottom_width = 8  # Bottom width in chi
bottom_length = 40  # Bottom length in chi
depth = 65  # Depth in chi (6 zhang 5 chi = 65 chi)

# Calculate the areas of the top and bottom rectangles
A1 = top_width * top_length  # Top area
A2 = bottom_width * bottom_length  # Bottom area

# Calculate the volume of the frustum
volume = Fraction(depth, 3) * (A1 + A2 + math.sqrt(A1 * A2))

# Answer for the volume
volume_in_chi = volume  # Total volume in chi^3
print(f"Volume: {volume_in_chi} chi^3")

# Human work calculation
cart_capacity = 240  # Capacity of one cart in chi^3
distance_one_way = 1000  # One li = 1000 steps
round_trip_distance = 2 * distance_one_way  # Round trip distance
cart_people = 6  # 6 people per cart

# Calculate the total number of steps for one cart
steps_per_cart = cart_capacity * round_trip_distance

# Calculate the divisor (法)
divisor = steps_per_cart * cart_people

# Calculate how far one person can carry (人到)
person_reach = Fraction(steps_per_cart, divisor)

# Calculate the number of workers required (用徒)
workers_needed = Fraction(volume_in_chi, person_reach)

# Simplify the results
a = person_reach
b = workers_needed

print(f"Person reach: {a} chi")
print(f"Workers needed: {b} people")


"""


---

### Explanation of the Code
1. **Volume Calculation**:
   - The formula for the volume of a frustum is applied using the given dimensions.
   - The result is stored in `volume_in_chi`.

2. **Human Work Calculation**:
   - The cart's capacity and the round-trip distance are used to calculate the total steps required for one cart.
   - The divisor is calculated by multiplying the steps per cart by the number of people per cart.
   - The distance one person can carry is calculated as `person_reach`.
   - The total number of workers required is calculated as `workers_needed`.

3. **Output**:
   - The results for `a` (distance one person can carry) and `b` (number of workers needed) are printed.

---

### Final Answer
- **Person reach**: \(a\) chi.
- **Workers needed**: \(b\) people.
"""


"""
Code error: both arguments should be Rational instances"""
