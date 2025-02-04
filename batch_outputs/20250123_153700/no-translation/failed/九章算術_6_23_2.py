"""
今有假田，初假之歲三畝一錢，明年四畝一錢，後年五畝一錢。凡三歲得一百，問︰田幾何？
術曰：置畝數及錢數，令畝數互乘錢數，并以為法。畝數相乘，又以百錢乘之，為實。實如法得一畝。
荅曰： a頃 。
"""

"""

"""


from fractions import Fraction

# 初假之歲三畝一錢，明年四畝一錢，後年五畝一錢
畝數 = [3, 4, 5]
錢數 = [1, 1, 1]

# 凡三歲得一百錢
總錢 = 100

# 令畝數互乘錢數，并以為法
法 = sum(畝數[i] * 錢數[j] for i in range(len(畝數)) for j in range(len(錢數)))

# 畝數相乘，又以百錢乘之，為實
實 = sum(畝數[i] * 畝數[j] for i in range(len(畝數)) for j in range(len(畝數))) * 總錢

# 實如法得一畝
一畝 = Fraction(實, 法)

# 百畝為一頃
a = 一畝 / 100


"""

"""


"""
Variable 'a' has wrong value. Expected: 60/47, Actual: 4"""
