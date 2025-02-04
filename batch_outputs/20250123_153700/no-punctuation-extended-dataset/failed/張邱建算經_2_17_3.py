"""
今有清酒一㪷直粟十㪷醑酒一㪷直粟三㪷今持粟三斛得酒五㪷問清醑酒各㡬何
術曰置得酒㪷數以清酒直數乗之減去持粟㪷數餘為醑酒實又置得酒㪷數以醑酒直數乗之以減持粟㪷數餘為清酒實各以二直相減餘為法實如法而一即得以盈不足為之亦得
答曰醑酒 a㪷 清酒 b㪷
"""

"""
Suppose there is one dou of clear wine worth 10 dou of millet, and one dou of strong wine worth 3 dou of millet.
Now, with 3 hu of millet, 5 dou of wine is obtained.
Question: how much clear wine and strong wine are obtained respectively?

The procedure says: Place the number of dou of wine obtained and multiply it by the price of clear wine.
Subtract the amount of millet held; the remainder is the strong wine's value.
Then, place the number of dou of wine obtained and multiply it by the price of strong wine.
Subtract the amount of millet held; the remainder is the clear wine's value.
For each, subtract the two prices from each other, and the remainder is the divisor.
The values divided by the divisor give the amounts of clear and strong wine.
If there is excess or deficiency, adjust accordingly.

Answer: *a* dou of strong wine, *b* dou of clear wine.
"""

# 清酒一㪷直粟十㪷
清酒價 = 10

# 醑酒一㪷直粟三㪷
醑酒價 = 3

# 持粟三斛 (1斛 = 10斗)
持粟 = 3 * 10

# 得酒五㪷
得酒 = 5

# 置得酒㪷數以清酒直數乘之
清酒總價 = 得酒 * 清酒價

# 減去持粟㪷數，餘為醑酒實
醑酒實 = 清酒總價 - 持粟

# 置得酒㪷數以醑酒直數乘之
醑酒總價 = 得酒 * 醑酒價

# 減去持粟㪷數，餘為清酒實
清酒實 = 醑酒總價 - 持粟

# 各以二直相減，餘為法
法 = 清酒價 - 醑酒價

# 實如法而一，即得
a = Fraction(醑酒實, 法)  # 醑酒數量
b = Fraction(清酒實, 法)  # 清酒數量
"""
Variable 'b' has wrong value. Expected: 15/7, Actual: -15/7"""
