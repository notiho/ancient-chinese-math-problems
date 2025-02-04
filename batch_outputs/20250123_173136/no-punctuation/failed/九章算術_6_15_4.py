"""
今有客馬日行三百里客去忘持衣日已三分之一主人乃覺持衣追及與之而還至家視日四分之三問主人馬不休日行幾何
術曰置四分日之三除三分日之一半其餘以為法副置法增三分日之一以三百里乘之為實實如法得主人馬一日行
荅曰 a里 
"""

"""
Suppose there is a traveler whose horse travels 300 li per day. The traveler forgets to bring their clothes, and after 1/3 of the day has passed, the host realizes this and starts chasing the traveler with the clothes. The host catches up, gives the clothes, and returns home. By the time the host returns home, 3/4 of the day has passed.
Question: How far does the host's horse travel per day if it does not rest?

The procedure says: Place 3/4 of the day as the dividend and divide it by 1/3 of the day, subtracting half of the remainder. Use the result as the divisor.
Additionally, place the divisor, add 1/3 of the day to it, and multiply it by 300 li to obtain the dividend. Divide the dividend by the divisor to find how far the host's horse travels in one day.

The answer says: *a* li.
"""

from fractions import Fraction

# 客馬日行三百里
客馬日行 = 300

# 日已三分之一
三分日之一 = Fraction(1, 3)

# 日四分之三
四分日之三 = Fraction(3, 4)

# 置四分日之三，除三分日之一
商 = 四分日之三 / 三分日之一

# 半其餘，以為法
法 = 商 - Fraction(1, 2)

# 副置法，增三分日之一
增量 = 法 + 三分日之一

# 以三百里乘之，為實
實 = 客馬日行 * 增量

# 實如法，得主人馬一日行
a = 實 / 法
"""
Variable 'a' has wrong value. Expected: 780, Actual: 2500/7"""
