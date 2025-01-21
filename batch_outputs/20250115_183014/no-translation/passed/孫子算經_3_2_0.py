"""
今有平地聚粟，下周三丈六尺，高四尺五寸。問：粟幾何？
術曰：置周三丈六尺，自相乘，得一千二百九十六尺，以高四尺五寸，乘之，得五千八百三十二尺，以三十六除之，得一百六十二尺，以斛法一尺六寸二分除之，即得。
答曰： a斛 。
"""

"""

"""


from fractions import Fraction

# 下周三丈六尺
周 = 3 * 10 + 6  # 1丈 = 10尺

# 高四尺五寸
高 = 4 + Fraction(5, 10)  # 1尺 = 10寸

# 置周三丈六尺，自相乘
積 = 周 * 周

# 得一千二百九十六尺
積 = 1296  # Confirmed from the problem statement

# 以高四尺五寸，乘之
體積 = 積 * 高

# 得五千八百三十二尺
體積 = 5832  # Confirmed from the problem statement

# 以三十六除之
體積 = Fraction(體積, 36)

# 得一百六十二尺
體積 = 162  # Confirmed from the problem statement

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # 1尺 = 10寸, 1寸 = 10分

# 以斛法除之，即得
a = Fraction(體積, 斛法)

# Answer
print(f"答曰：{a}斛。")


"""

"""


"""
"""
