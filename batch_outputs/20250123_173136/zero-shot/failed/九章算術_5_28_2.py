"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
載土往來二百步，載輸之間一里，程行五十八里，六人共車，車載三十四尺七寸。問︰人到積尺及用徒各幾何？
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a trapezoidal prism and determining the number of workers required to transport the soil.

Here is the Python code:


"""


from fractions import Fraction

# Given dimensions of the trapezoidal prism
top_width = Fraction(2)  # 2丈
top_length = Fraction(7)  # 7丈
bottom_width = Fraction(8, 10)  # 8尺 = 8/10丈
bottom_length = Fraction(4)  # 4丈
depth = Fraction(6) + Fraction(5, 10)  # 6丈5尺 = 6 + 5/10丈

# Calculate the volume of the trapezoidal prism
# Volume = (1/2) * depth * (top_area + bottom_area)
top_area = top_width * top_length
bottom_area = bottom_width * bottom_length
volume = Fraction(1, 2) * depth * (top_area + bottom_area)

# Convert volume to cubic 尺 (1丈³ = 1000尺³)
volume_in_cubic_chi = volume * 1000

# Output the volume
積 = volume_in_cubic_chi  # Volume in cubic 尺
print(f"積: {積}尺")  # Expected: 52000尺

# Given data for transportation
往來步數 = Fraction(200)  # 200 steps round trip
載輸之間 = Fraction(1)  # 1里
程行 = Fraction(58)  # 58里
車載 = Fraction(34) + Fraction(7, 10)  # 34尺7寸 = 34 + 7/10尺
車人數 = Fraction(6)  # 6 people per cart

# Calculate total steps
程行步數 = 程行 * 360  # 1里 = 360 steps
總步數 = 往來步數 + (載輸之間 * 360)

# Calculate the total soil transported by one person
一人所到尺 = (車載 * 程行步數) / (總步數 * 車人數)

# Calculate the number of workers required
用徒 = volume_in_cubic_chi / 一人所到尺

# Output the results
a = 一人所到尺  # Soil transported by one person
b = 用徒  # Number of workers required

print(f"人到 a尺: {a}")
print(f"用徒 b人: {b}")


"""


### Explanation:
1. **Volume Calculation**:
   - The volume of the trapezoidal prism is calculated using the formula for the volume of a trapezoidal prism:  
     \( V = \frac{1}{2} \times \text{depth} \times (\text{top area} + \text{bottom area}) \).
   - The areas of the top and bottom faces are calculated using their respective dimensions.
   - The volume is then converted from cubic 丈 to cubic 尺 (1丈³ = 1000尺³).

2. **Transportation Calculation**:
   - The total steps for transportation are calculated by adding the round-trip steps and the steps for the 1里 distance.
   - The total soil transported by one person is calculated by dividing the total soil transported by the total steps and the number of people per cart.
   - The number of workers required is calculated by dividing the total volume of soil by the amount transported by one person.

### Output:
The program will output the following:
- \( a \): The amount of soil transported by one person in cubic 尺.
- \( b \): The number of workers required.
"""


"""
Variable 'a' has wrong value. Expected: 10063/50, Actual: 30189/140
Variable 'b' has wrong value. Expected: 2600000/10063, Actual: 7826000/30189"""
