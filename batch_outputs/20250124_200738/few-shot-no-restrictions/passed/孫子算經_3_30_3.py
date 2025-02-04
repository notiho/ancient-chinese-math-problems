"""
今有九里渠，三寸魚頭，頭相次。問：魚得幾何？
術曰：置九里以三百步乘之，得二千七百步；又以六尺乘之，得一萬六千二百尺，上十之，得一十六萬二千寸，以魚三寸除之，即得。
答曰： a 。
"""

#----- content starts here -----
"""
Suppose there is a canal 9 li long, with fish heads spaced 3 cun apart, one after the other.
Question: how many fish are there?

The procedure says: Take the 9 li and multiply it by 300 bu, obtaining 2700 bu.
Then multiply it by 6 chi, obtaining 16200 chi.
Convert it to cun by multiplying by 10, obtaining 162000 cun.
Divide this by 3 cun (the spacing of the fish), and the result is the number of fish.

Answer: *a* fish.
"""

from fractions import Fraction

# 1 里 = 300 步
里_to_步 = 300

# 1 步 = 6 尺
步_to_尺 = 6

# 1 尺 = 10 寸
尺_to_寸 = 10

# 渠長九里
渠長_里 = 9

# 魚頭間距三寸
魚頭間距_寸 = 3

# 置九里以三百步乘之，得二千七百步
渠長_步 = 渠長_里 * 里_to_步

# 又以六尺乘之，得一萬六千二百尺
渠長_尺 = 渠長_步 * 步_to_尺

# 上十之，得一十六萬二千寸
渠長_寸 = 渠長_尺 * 尺_to_寸

# 以魚三寸除之，即得
a = Fraction(渠長_寸, 魚頭間距_寸)

a  # Number of fish#----- content ends here -----

"""
"""
