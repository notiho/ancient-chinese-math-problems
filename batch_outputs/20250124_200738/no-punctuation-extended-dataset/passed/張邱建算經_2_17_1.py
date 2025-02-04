"""
今有清酒一㪷直粟十㪷醑酒一㪷直粟三㪷今持粟三斛得酒五㪷問清醑酒各㡬何
術曰置得酒㪷數以清酒直數乗之減去持粟㪷數餘為醑酒實又置得酒㪷數以醑酒直數乗之以減持粟㪷數餘為清酒實各以二直相減餘為法實如法而一即得以盈不足為之亦得
答曰醑酒 a㪷 清酒 b㪷
"""

#----- content starts here -----
"""
Suppose there is 1 dou of clear wine worth 10 dou of millet, and 1 dou of strong wine worth 3 dou of millet.
Now, with 3 hu of millet, 5 dou of wine is obtained.
Question: how much clear wine and strong wine are obtained respectively?

The procedure says: Place the number of dou of wine obtained and multiply it by the price of clear wine.
Subtract the amount of millet held, and the remainder is the amount of strong wine.
Then, place the number of dou of wine obtained and multiply it by the price of strong wine.
Subtract the amount of millet held, and the remainder is the amount of clear wine.
For each, subtract the two prices, and the remainder is the divisor.
Divide the amounts by the divisor, and the result is the answer.
If there is surplus or deficiency, adjust accordingly.

Answer: *a* dou of strong wine, *b* dou of clear wine.
"""

from fractions import Fraction

# 清酒一㪷直粟十㪷
清酒價 = 10

# 醑酒一㪷直粟三㪷
醑酒價 = 3

# 持粟三斛 (1斛 = 10斗)
持粟 = 3 * 10

# 得酒五㪷
得酒 = 5

# 置得酒㪷數，以清酒直數乘之
清酒實 = 得酒 * 清酒價

# 減去持粟㪷數，餘為醑酒實
醑酒實 = 清酒實 - 持粟

# 置得酒㪷數，以醑酒直數乘之
醑酒實_alt = 得酒 * 醑酒價

# 減去持粟㪷數，餘為清酒實
清酒實_alt = 持粟 - 醑酒實_alt

# 各以二直相減，餘為法
法 = 清酒價 - 醑酒價

# 實如法而一，即得
a = Fraction(醑酒實, 法)
b = Fraction(清酒實_alt, 法)#----- content ends here -----

"""
"""
