"""
今有粟五百六十斛，凡粟八斗易麥五斗。問：得麥㡬何？
術曰：列粟五百六十斛，以五十乘之得二萬八千斛，以八千除之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 560 hu of millet. For every 8 dou of millet, 5 dou of wheat can be exchanged.
Question: how much wheat is obtained?

The procedure says: Place the 560 hu of millet, multiply it by 50 (since 1 hu = 10 dou, and 8 dou is scaled to 5 dou of wheat). 
Divide the result by 8000 (since 1 hu = 10 dou, and the exchange ratio is scaled accordingly), and the result is obtained.

Answer: *a* hu of wheat.
"""

from fractions import Fraction

# 粟五百六十斛
粟 = 560  # in hu

# 每斛有10斗
粟斗 = 粟 * 10  # Convert hu to dou

# 凡粟八斗易麥五斗
粟兌換率 = 8  # 8 dou of millet
麥兌換率 = 5  # 5 dou of wheat

# 計算比例
比例 = Fraction(麥兌換率, 粟兌換率)

# 計算麥的總量 (以斗為單位)
麥斗 = 粟斗 * 比例

# 將斗轉換為斛 (10斗 = 1斛)
麥斛 = 麥斗 / 10

# 答案
a = 麥斛
a#----- content ends here -----

"""
"""
