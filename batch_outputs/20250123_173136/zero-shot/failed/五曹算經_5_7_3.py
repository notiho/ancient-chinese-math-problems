"""
今有錦一疋直錢八貫。問：一丈一尺一寸各直㡬何？
術曰：列錢八貫，以四十尺除之即尺價；進位即丈價；退位即寸價。
答曰:一丈 a貫文 ，一尺 b文 ，一寸 c文 。
"""

"""
To solve this problem, we will calculate the value of one丈 (zhang), one尺 (chi), and one寸 (cun) based on the given information.

The problem states that one bolt of silk (錦) is worth 8貫 (guan), and the total length of the silk is 40尺 (chi). From this, we can calculate the value of one尺 (chi), and then use the relationships between the units to calculate the value of one丈 (zhang) and one寸 (cun).

1丈 = 10尺  
1尺 = 10寸  

Here is the Python code to compute the values:


"""


from fractions import Fraction

# Given data
total_value = Fraction(8)  # 8貫
total_length = 40  # 40尺

# Calculate the value of one 尺 (chi)
b = total_value / total_length  # Value of one 尺 in 貫文

# Calculate the value of one 丈 (zhang)
a = b * 10  # 1丈 = 10尺

# Calculate the value of one 寸 (cun)
c = b / 10  # 1尺 = 10寸

# Results
a  # Value of one 丈 in 貫文
b  # Value of one 尺 in 貫文
c  # Value of one 寸 in 貫文


"""


### Explanation of the Results:
- `a` is the value of one丈 (zhang) in貫文.
- `b` is the value of one尺 (chi) in貫文.
- `c` is the value of one寸 (cun) in貫文.

You can now run this code to compute the exact values of `a`, `b`, and `c`.
"""


"""
Variable 'b' has wrong value. Expected: 200, Actual: 1/5
Variable 'c' has wrong value. Expected: 20, Actual: 1/50"""
