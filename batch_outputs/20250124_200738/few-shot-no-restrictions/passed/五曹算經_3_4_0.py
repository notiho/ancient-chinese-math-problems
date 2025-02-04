"""
今有粟五百六十斛，凡粟八斗易麥五斗。問：得麥㡬何？
術曰：列粟五百六十斛，以五十乘之得二萬八千斛，以八千除之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 560 hu of millet, and the exchange rate is 8 dou of millet for 5 dou of wheat.
Question: how much wheat is obtained?

The procedure says: Place the 560 hu of millet, multiply it by 50 (to convert hu to dou), obtaining 28000 dou.
Divide it by 8 (the amount of millet exchanged for wheat), and the result is the amount of wheat in dou.
Finally, convert the result back to hu.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟五百六十斛
粟 = 560  # in hu

# 1 hu = 10 dou, convert 粟 to dou
粟_dou = 10 * 粟

# 凡粟八斗易麥五斗
粟兌換率 = 8  # 8 dou of millet
麥兌換率 = 5  # 5 dou of wheat

# Calculate total wheat in dou
麥_dou = Fraction(粟_dou * 麥兌換率, 粟兌換率)

# Convert 麥 back to hu
a = 麥_dou / 10  # 1 hu = 10 dou

a#----- content ends here -----

"""
"""
