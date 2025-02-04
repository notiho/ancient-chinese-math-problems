"""
今有竹高一丈，末折抵地，去本三尺。問︰折者高幾何？
術曰：以去本自乘，令如高而一，所得，以減竹高而半其餘，即折者之高也。
荅曰： a(=91/20)尺 。
"""

"""
Suppose there is a bamboo 1 zhang tall. Its tip bends and touches the ground, 3 chi away from its base.
Question: what is the height of the bent portion?

The procedure says: Multiply the distance from the base by itself. Let the result be divided by the height of the bamboo, obtaining the quotient.
Subtract this quotient from the height of the bamboo, and halve the remainder. This is the height of the bent portion.

Answer: *a*(=91/20) chi.
"""

from fractions import Fraction

# 竹高一丈 (convert to chi, 1丈 = 10尺)
竹高 = 10

# 去本三尺
去本 = 3

# 以去本自乘
去本平方 = 去本 * 去本

# 令如高而一，所得
所得 = Fraction(去本平方, 竹高)

# 以減竹高
餘 = 竹高 - 所得

# 而半其餘，即折者之高
a = Fraction(餘, 2)  # 91/20 chi
"""
"""
