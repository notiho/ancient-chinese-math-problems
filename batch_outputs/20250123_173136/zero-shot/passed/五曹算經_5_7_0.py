"""
今有錦一疋直錢八貫。問：一丈一尺一寸各直㡬何？
術曰：列錢八貫，以四十尺除之即尺價；進位即丈價；退位即寸價。
答曰:一丈 a貫文 ，一尺 b文 ，一寸 c文 。
"""

"""
To solve this problem, we will compute the value of one丈 (zhang), one尺 (chi), and one寸 (cun) based on the given total value of the fabric and its length. Here's the Python code:


"""


from fractions import Fraction

# Total value of the fabric in 貫 (guan)
total_value = 8  # 貫

# Total length of the fabric in 尺 (chi)
total_length = 40  # 尺

# Value of one 尺 (chi)
b = Fraction(total_value, total_length) * 1000  # Convert 貫 to 文 (1 貫 = 1000 文)

# Value of one 丈 (zhang) (1 丈 = 10 尺)
a = b * 10 / 1000  # Convert back to 貫

# Value of one 寸 (cun) (1 尺 = 10 寸)
c = b / 10  # 文

# Results
a  # Value of one 丈 in 貫
b  # Value of one 尺 in 文
c  # Value of one 寸 in 文


"""


### Explanation:
1. The total value of the fabric is 8貫, and the total length is 40尺.
2. To find the value of one尺, divide the total value by the total length and convert 貫 to 文 (1貫 = 1000文).
3. To find the value of one丈, multiply the value of one尺 by 10 (since 1丈 = 10尺) and convert back to 貫.
4. To find the value of one寸, divide the value of one尺 by 10 (since 1尺 = 10寸).

### Final Answer:
- `a = 2` 貫文 (value of one丈)
- `b = 200` 文 (value of one尺)
- `c = 20` 文 (value of one寸)
"""


"""
"""
