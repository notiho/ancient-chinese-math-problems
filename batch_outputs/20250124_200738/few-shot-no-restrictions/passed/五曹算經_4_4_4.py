"""
今有圓囷周三丈，高一丈六尺。問：受粟㡬何？
術曰：列周三丈自相乘得九百尺以高一丈六尺乘之得一萬四千四百尺以十二除之得一千二百尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical granary with a circumference of 3 zhang and a height of 1 zhang 6 chi.
Question: how much grain can it hold?

The procedure says: Take the circumference of 3 zhang, square it, obtaining 900 chi². Multiply this by the height of 1 zhang 6 chi, obtaining 14400 chi³. Divide this by 12 to get 1200 chi³. Finally, divide this by the volume of 1 hu (1 chi 6 cun 2 fen) to obtain the result.

Answer: *a* hu and *b* chi³.
"""

from fractions import Fraction

# 圓囷周三丈 (circumference = 3 zhang)
周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高一丈六尺 (height = 1 zhang 6 chi)
高 = 1 * 10 + 6  # Convert zhang and chi to chi

# 列周三丈自相乘得九百尺 (square the circumference)
周平方 = 周 ** 2

# 以高一丈六尺乘之得一萬四千四百尺 (multiply by height)
體積 = 周平方 * 高

# 以十二除之得一千二百尺 (divide by 12)
體積除以十二 = Fraction(體積, 12)

# 斛法一尺六寸二分 (1 hu = 1 chi 6 cun 2 fen = 1.62 chi³)
斛法 = Fraction(162, 100)  # Convert 1 chi 6 cun 2 fen to a fraction (1.62 chi³)

# Divide the volume by the volume of 1 hu
斛數 = 體積除以十二 / 斛法

# Extract the integer part (a hu) and the remainder (b chi³)
a = int(斛數)  # Integer part (number of hu)
b = 體積除以十二 - a * 斛法  # Remainder in chi³

# Convert b to a fraction for clarity
b = Fraction(b)

a, b  # Output the result as (a hu, b chi³)#----- content ends here -----

"""
"""
