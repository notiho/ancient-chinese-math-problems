"""
今有女子善織，日自倍，五日織五尺。問︰日織幾何？
術曰：置一、二、四、八、十六為列衰，副并為法，以五尺乘未并者，各自為實，實如法得一尺。
荅曰：初日織 a寸 。次日織 b寸 。次日織 c寸 。次日織 d尺 。次日織 e尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem describes a woman weaving cloth, doubling her output each day, and completing 5 feet (or 5尺) of cloth in 5 days. We need to calculate how much she weaves each day, expressed in terms of "a", "b", "c", "d", and "e".

Here is the Python code:


"""


from fractions import Fraction

# Total woven cloth in 5 days
total_cloth = 5  # in 尺

# The weaving doubles each day: a, 2a, 4a, 8a, 16a
# Total cloth = a + 2a + 4a + 8a + 16a = 31a
total_factor = 1 + 2 + 4 + 8 + 16  # Sum of the geometric progression
a = Fraction(total_cloth, total_factor)  # First day's weaving in 尺

# Calculate the weaving for each day
b = 2 * a  # Second day's weaving in 尺
c = 4 * a  # Third day's weaving in 尺
d = 8 * a  # Fourth day's weaving in 尺
e = 16 * a  # Fifth day's weaving in 尺

# Convert to smaller units (寸) where necessary
# 1 尺 = 10 寸
a寸 = a * 10  # First day's weaving in 寸
b寸 = b * 10  # Second day's weaving in 寸
c寸 = c * 10  # Third day's weaving in 寸

# Results
a寸 = a寸  # First day's weaving in 寸
b寸 = b寸  # Second day's weaving in 寸
c寸 = c寸  # Third day's weaving in 寸
d尺 = d  # Fourth day's weaving in 尺
e尺 = e  # Fifth day's weaving in 尺


"""


### Explanation:
1. The total cloth woven in 5 days is 5尺.
2. The weaving doubles each day, forming a geometric progression: a, 2a, 4a, 8a, 16a.
3. The total cloth woven is the sum of this progression: \( a + 2a + 4a + 8a + 16a = 31a \).
4. Solving for \( a \), we find \( a = \frac{5}{31} \) 尺.
5. Using \( a \), we calculate the weaving for each day:
   - \( b = 2a \), \( c = 4a \), \( d = 8a \), \( e = 16a \).
6. Convert \( a \), \( b \), and \( c \) to smaller units (寸) since 1 尺 = 10 寸.

### Final Results:
- \( a寸 = \frac{50}{31} \) 寸
- \( b寸 = \frac{100}{31} \) 寸
- \( c寸 = \frac{200}{31} \) 寸
- \( d尺 = \frac{40}{31} \) 尺
- \( e尺 = \frac{80}{31} \) 尺
"""


"""
Variable 'a' has wrong value. Expected: 50/31, Actual: 5/31
Variable 'b' has wrong value. Expected: 100/31, Actual: 10/31
Variable 'c' has wrong value. Expected: 200/31, Actual: 20/31"""
