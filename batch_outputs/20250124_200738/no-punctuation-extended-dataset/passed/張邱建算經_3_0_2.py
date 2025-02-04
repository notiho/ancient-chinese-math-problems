"""
今有甲乙丙丁戊五人共獵獲鹿約以甲六乙五丙四丁三戊二分之今獲鹿五問各得幾何
術曰列置甲六乙五丙四丁三戊二各自為差副併為法以鹿數乘未併者各自為實實如法而一
答曰甲得 a鹿 乙得 b鹿 丙得 c鹿 丁得 d鹿 戊得 e鹿
"""

#----- content starts here -----
"""
Suppose there are five people: Jia, Yi, Bing, Ding, and Wu. They hunted together and caught 5 deer.
The deer are to be divided proportionally according to their shares: Jia gets 6 parts, Yi gets 5 parts, Bing gets 4 parts, Ding gets 3 parts, and Wu gets 2 parts.
Question: how much does each person get?

The procedure says: Place the shares of Jia, Yi, Bing, Ding, and Wu in a line.
Each of them becomes its own term in the sequence.
Add them together to form the divisor.
Multiply the total number of deer by the individual shares (not yet added together), making each its own dividend.
Divide each dividend by the divisor to obtain the number of deer for each person.

The answer says: Jia gets *a* deer, Yi gets *b* deer, Bing gets *c* deer, Ding gets *d* deer, and Wu gets *e* deer.
"""

# 列置甲六乙五丙四丁三戊二，各自為差
shares = [6, 5, 4, 3, 2]

# 副併為法
法 = sum(shares)

# 以鹿數乘未併者
鹿數 = 5
實 = [鹿數 * share for share in shares]

# 實如法而一
a, b, c, d, e = [Fraction(share, 法) for share in 實]#----- content ends here -----

"""
"""
