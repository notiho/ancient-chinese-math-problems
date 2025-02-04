"""
今有錦一疋直錢八貫。問：一丈一尺一寸各直㡬何？
術曰：列錢八貫，以四十尺除之即尺價；進位即丈價；退位即寸價。
答曰:一丈 a貫文 ，一尺 b文 ，一寸 c文 。
"""

"""
To solve this problem, we need to calculate the value of one丈 (zhang), one尺 (chi), and one寸 (cun) based on the given total value of the fabric and its length. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total value of the fabric in 貫 (1 貫 = 1000 文)
total_value = 8  # 貫

# Total length of the fabric in 尺 (1 丈 = 10 尺, 1 尺 = 10 寸)
total_length_in_chi = 40  # 尺

# Calculate the value of one 尺 (chi)
b = Fraction(total_value * 1000, total_length_in_chi)  # 文 per 尺

# Calculate the value of one 丈 (zhang)
a = b * 10 / 1000  # 貫 per 丈 (10 尺 = 1 丈)

# Calculate the value of one 寸 (cun)
c = b / 10  # 文 per 寸 (10 寸 = 1 尺)

# Results
a, b, c
#----- content ends here -----


"""


### Explanation:
1. The total value of the fabric is 8 貫 (8000 文).
2. The total length of the fabric is 40 尺.
3. To find the value of one 尺 (b), divide the total value (in 文) by the total length (in 尺).
4. To find the value of one 丈 (a), multiply the value of one 尺 by 10 (since 1 丈 = 10 尺) and convert it back to 貫.
5. To find the value of one 寸 (c), divide the value of one 尺 by 10 (since 1 尺 = 10 寸).

### Final Values:
- `a = Fraction(2, 1)` 貫 per 丈
- `b = Fraction(200, 1)` 文 per 尺
- `c = Fraction(20, 1)` 文 per 寸
"""


"""
"""
