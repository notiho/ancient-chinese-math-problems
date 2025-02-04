"""
今有清酒一㪷直粟十㪷醑酒一㪷直粟三㪷今持粟三斛得酒五㪷問清醑酒各㡬何
術曰置得酒㪷數以清酒直數乗之減去持粟㪷數餘為醑酒實又置得酒㪷數以醑酒直數乗之以減持粟㪷數餘為清酒實各以二直相減餘為法實如法而一即得以盈不足為之亦得
答曰醑酒 a㪷 清酒 b㪷
"""

"""
Suppose there is one dou of clear wine worth 10 dou of millet, and one dou of strong wine worth 3 dou of millet.
Now, with 3 hu of millet, 5 dou of wine is obtained.
Question: how much clear wine and strong wine are obtained respectively?

The procedure says: Place the number of dou of wine obtained, and multiply it by the price of clear wine. Subtract the amount of millet held, and the remainder is the amount of strong wine.
Then, place the number of dou of wine obtained, and multiply it by the price of strong wine. Subtract the amount of millet held, and the remainder is the amount of clear wine.
For each, subtract the two prices from each other, and the remainder is the divisor.
Divide the amounts by the divisor to obtain the result.
If there is surplus or deficiency, adjust accordingly.

Answer: *a* dou of strong wine, *b* dou of clear wine.
"""

from fractions import Fraction

# Clear wine price and strong wine price
清酒直 = 10  # Clear wine price in dou of millet
醑酒直 = 3   # Strong wine price in dou of millet

# Total millet and total wine obtained
持粟 = 3 * 10  # Convert hu to dou (1 hu = 10 dou)
得酒 = 5       # Total wine obtained in dou

# Step 1: Calculate the amount of strong wine
# 置得酒㪷數以清酒直數乗之減去持粟㪷數餘為醑酒實
醑酒實 = (得酒 * 清酒直) - 持粟

# Step 2: Calculate the amount of clear wine
# 置得酒㪷數以醑酒直數乗之以減持粟㪷數餘為清酒實
清酒實 = (得酒 * 醑酒直) - 持粟

# Step 3: Calculate the divisor
# 各以二直相減餘為法
法 = 清酒直 - 醑酒直

# Step 4: Divide the amounts by the divisor
# 實如法而一即得
a = Fraction(醑酒實, 法)  # Strong wine in dou
b = Fraction(清酒實, 法)  # Clear wine in dou

# Results
a, b  # a is the amount of strong wine, b is the amount of clear wine
"""
Variable 'b' has wrong value. Expected: 15/7, Actual: -15/7"""
