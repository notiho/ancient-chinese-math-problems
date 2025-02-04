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

# Total value of the fabric in 貫 (guan)
total_value = 8  # 貫

# Total length of the fabric in 尺 (chi)
total_length = 40  # 尺

# Calculate the value of one 尺 (chi)
b = Fraction(total_value * 1000, total_length)  # Convert 貫 to 文 (1貫 = 1000文)

# Calculate the value of one 丈 (zhang), which is 10 尺
a = b * 10 / 1000  # Convert back to 貫

# Calculate the value of one 寸 (cun), which is 1/10 of a 尺
c = b / 10  # In 文

# Results
a  # Value of one 丈 in 貫
b  # Value of one 尺 in 文
c  # Value of one 寸 in 文
#----- content ends here -----


"""


### Explanation:
1. The total value of the fabric is 8貫, and its length is 40尺.
2. To find the value of one 尺, divide the total value (in 文) by the total length (in 尺). Since 1貫 = 1000文, we multiply the total value by 1000 to convert it to 文.
3. The value of one 丈 is 10 times the value of one 尺, converted back to 貫.
4. The value of one 寸 is 1/10 of the value of one 尺.

### Final Answer:
- `a = 2` 貫文 (value of one 丈)
- `b = 200` 文 (value of one 尺)
- `c = 20` 文 (value of one 寸)
"""


"""
"""
