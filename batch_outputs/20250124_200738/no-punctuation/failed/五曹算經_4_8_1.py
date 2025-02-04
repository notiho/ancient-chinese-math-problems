"""
今有平地聚粟下周三丈高四尺問粟㡬何
術曰列下周三十尺自相乘得九百尺以高四尺乘之得三千六百尺以三十六除之得一百尺以斛法一尺六寸二分除之即得
答曰 a斛 奇 b分 
"""

#----- content starts here -----
"""
Suppose there is a flat ground with a pile of millet. The base circumference is 3 zhang, and the height is 4 chi.
Question: how much millet is there?

The procedure says: Take the base circumference, 30 chi, and multiply it by itself, obtaining 900 chi².
Multiply this by the height, 4 chi, obtaining 3600 chi³.
Divide this by 36, obtaining 100 chi³.
Divide this by the dou-measure, which is 1 chi 6 cun 2 fen (1.62 chi³), obtaining the result.

Answer: *a* dou and *b* fen.
"""

# 下周三丈 (convert to chi: 1丈 = 10尺)
下周 = 3 * 10  # in chi

# 高四尺
高 = 4  # in chi

# 斛法一尺六寸二分 (convert to chi³: 1尺 = 10寸, 1寸 = 10分)
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # in chi³

# 列下周三十尺，自相乘得九百尺
底積 = 下周 * 下周  # in chi²

# 以高四尺乘之，得三千六百尺
體積 = 底積 * 高  # in chi³

# 以三十六除之，得一百尺
體積 = Fraction(體積, 36)  # in chi³

# 以斛法一尺六寸二分除之，即得
總斛 = Fraction(體積, 斛法)

# 分解為斛和分
a = int(總斛)  # 整斛數
b = (總斛 - a) * 100  # 剩餘分數部分 (轉換為分)

a, b  # Answer: a斛 奇 b分#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 61
Variable 'b' has wrong value. Expected: 34/25, Actual: 5900/81"""
