"""
今有委菽依垣下周三丈高七尺問積及為菽各幾何
委粟術曰下周自乘以高乘之三十六而一其依垣者十八而一其依垣內角者九而一程粟一斛積二尺七寸其米一斛積一尺六寸五分寸之一其菽答麻麥一斛皆二尺四寸十分寸之三
荅曰積 a尺 為菽 b斛 
"""

#----- content starts here -----
"""
Suppose there is a pile of beans leaning against a wall. Its base circumference is 3 zhang, and its height is 7 chi.
Question: what is the volume of the pile, and how many dou of beans does it make?

The procedure for piled grain says: 
- For a pile with a full circular base, square the base circumference, multiply by the height, and divide by 36.
- For a pile leaning against a wall, divide by 18.
- For a pile leaning into a corner, divide by 9.

For beans, 1 hu occupies 2 chi 7 cun of volume.
For rice, 1 hu occupies 1 chi 6 cun 5 fen of volume.
For beans, hemp, and wheat, 1 hu occupies 2 chi 4 cun 3 fen of volume.

Answer: the volume is *a* chi³, and it makes *b* hu of beans.
"""

# 下周三丈
下周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高七尺
高 = 7

# 委粟術曰：下周自乘
下周平方 = 下周 * 下周

# 以高乘之
積 = 下周平方 * 高

# 其依垣者十八而一
積依垣 = Fraction(積, 18)

# 程粟一斛積二尺七寸 (Convert 2 chi 7 cun to chi)
一斛積 = 2 + Fraction(7, 10)  # 7 cun = 7/10 chi

# 其菽答麻麥一斛皆二尺四寸十分寸之三 (Convert 2 chi 4 cun 3 fen to chi)
菽一斛積 = 2 + Fraction(4, 10) + Fraction(3, 100)  # 4 cun = 4/10 chi, 3 fen = 3/100 chi

# 積 a尺
a = 積依垣

# 為菽 b斛
b = Fraction(積依垣, 菽一斛積)#----- content ends here -----

"""
"""
