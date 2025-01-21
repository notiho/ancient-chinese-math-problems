"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
荅曰：人到二百一尺、五十分尺之十三。用徒二百五十八人、一萬六十三分人之三千七百四十六。
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
To solve this problem, we need to compute the values of `a` (the distance in feet a person travels) and `b` (the number of workers needed). Let's break the problem into steps and translate it into Python code.

### Problem Breakdown:
1. **Volume Calculation**:
   - The volume of the irregular shape is given. The top width, bottom width, length, and depth are provided.
   - The volume is calculated using the formula for a trapezoidal prism:
     \[
     V = \frac{1}{2} \times (上廣 + 下廣) \times 深 \times 袤
     \]

2. **Distance Calculation**:
   - The distance a person travels (`a`) is calculated based on the total volume, the number of steps taken, and the number of people per cart.

3. **Number of Workers Calculation**:
   - The number of workers (`b`) is calculated by dividing the total volume by the distance traveled by one person.

### Python Code:

"""


from fractions import Fraction

# Given dimensions
top_width = Fraction(2 * 10)  # 上廣二丈 = 2丈 = 20尺
bottom_width = Fraction(8)    # 下廣八尺 = 8尺
top_length = Fraction(7 * 10) # 袤七丈 = 7丈 = 70尺
bottom_length = Fraction(4 * 10)  # 袤四丈 = 4丈 = 40尺
depth = Fraction(6 * 10 + 5)  # 深六丈五尺 = 6丈5尺 = 65尺

# Volume calculation
volume = Fraction(1, 2) * (top_width + bottom_width) * depth * (top_length + bottom_length)

# Given parameters for distance and workers
steps = Fraction(1)  # Number of steps (not explicitly given in the problem)
cart_people = Fraction(6)  # Number of people per cart

# Distance traveled by one person
a = (volume * steps) / cart_people

# Number of workers needed
b = volume / a

# Output the results
a, b


"""


### Explanation:
1. **Volume Calculation**:
   - The volume is calculated using the trapezoidal prism formula.
   - The dimensions are converted into feet (尺) as needed.

2. **Distance Calculation**:
   - The distance traveled by one person (`a`) is calculated using the formula provided in the problem.

3. **Number of Workers Calculation**:
   - The number of workers (`b`) is calculated by dividing the total volume by the distance traveled by one person.

### Results:
The variables `a` and `b` will contain the respective values for the distance traveled by one person and the number of workers needed.
"""


"""
Variable 'a' has wrong value. Expected: 10063/50, Actual: 50050/3
Variable 'b' has wrong value. Expected: 2600000/10063, Actual: 6"""
