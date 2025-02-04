"""
今有米三千四百五十六斛毎斗身内抽二升充腳問正腳各幾何
術曰先置米數去二得正米以二因退位得腳米
答曰正 a斛 腳 b斛
"""

#----- content starts here -----
"""
Suppose there are 3456 hu of rice. For every dou, 2 sheng are taken out to be allocated as "foot rice."
Question: how much is the "correct rice" and how much is the "foot rice"?

The procedure says: First, place the total amount of rice. Remove 2 [sheng per dou] to obtain the "correct rice."
Use 2 to calculate the "foot rice" by reversing the position.

Answer: the "correct rice" is *a* hu, and the "foot rice" is *b* hu.
"""

# 米三千四百五十六斛
總米 = 3456

# 每斛有10斗，每斗抽2升，計算每斛抽出的升數
每斛抽升數 = 10 * 2

# 每斛有100升，計算抽出部分占每斛的比例
抽出比例 = Fraction(每斛抽升數, 100)

# 計算腳米
腳米 = 總米 * 抽出比例

# 計算正米
正米 = 總米 - 腳米

a = 正米
b = 腳米#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2288, Actual: 13824/5
Variable 'b' has wrong value. Expected: 576, Actual: 3456/5"""
