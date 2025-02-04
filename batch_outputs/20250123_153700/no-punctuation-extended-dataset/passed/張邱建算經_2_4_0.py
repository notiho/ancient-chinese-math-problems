"""
今有遲行者五十步疾行者七十歩遲行者以先發疾行者以後發行八十七里一百五十步乃及之問遲行者先發行㡬何里
術曰以遲行步數減疾行步數餘以乗及步數為實以疾行步數為法實如法而一
答曰 a里
"""

"""
Suppose there is a slow walker who walks 50 bu and a fast walker who walks 70 bu.
The slow walker starts first, and the fast walker starts later.
After traveling 87 li and 150 bu, the fast walker catches up to the slow walker.
Question: how many li did the slow walker travel before the fast walker started?

The procedure says: Subtract the number of bu walked by the slow walker from the number of bu walked by the fast walker.
Multiply the remainder by the number of bu at the point of catching up, obtaining the dividend.
Divide the dividend by the number of bu walked by the fast walker, obtaining the result.

Answer: *a* li.
"""

# 遲行者五十步
遲行步數 = 50

# 疾行者七十步
疾行步數 = 70

# 行八十七里一百五十步
及里 = 87
及步數 = 150

# Convert 87 里 to 步 (1 里 = 300 步)
及步數 += 及里 * 300

# 以遲行步數減疾行步數
餘步數 = 疾行步數 - 遲行步數

# 餘以乘及步數，為實
實 = 餘步數 * 及步數

# 以疾行步數為法
法 = 疾行步數

# 實如法而一
a = Fraction(實, 法) / 300  # Convert 步 back to 里
"""
"""
