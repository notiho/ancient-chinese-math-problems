"""
今有甲乙丙丁戊五人共獵獲鹿約以甲六乙五丙四丁三戊二分之今獲鹿五問各得幾何
術曰列置甲六乙五丙四丁三戊二各自為差副併為法以鹿數乘未併者各自為實實如法而一
答曰甲得 a鹿 乙得 b鹿 丙得 c鹿 丁得 d鹿 戊得 e鹿
"""

"""
Suppose there are five people: Jia, Yi, Bing, Ding, and Wu. They hunted together and caught 5 deer.
The deer are to be divided proportionally according to the weights: Jia gets 6 parts, Yi gets 5 parts, Bing gets 4 parts, Ding gets 3 parts, and Wu gets 2 parts.
Question: how much does each person get?

The procedure says: Place the weights for Jia, Yi, Bing, Ding, and Wu in a line.
Each of them becomes its own term in the sequence.
Add them together to form the divisor.
Multiply the total number of deer by each weight (before summing), forming the dividend for each.
Divide each dividend by the divisor to obtain the number of deer for each person.

The answer says: Jia gets *a* deer, Yi gets *b* deer, Bing gets *c* deer, Ding gets *d* deer, and Wu gets *e* deer.
"""

# 列置甲六乙五丙四丁三戊二，各自為差
權重 = [6, 5, 4, 3, 2]

# 副併為法
法 = sum(權重)

# 獲鹿五
鹿數 = 5

# 以鹿數乘未併者，各自為實
實 = [鹿數 * i for i in 権重]

# 實如法而一
a, b, c, d, e = [Fraction(i, 法) for i in 實]
"""
Code error: name '権重' is not defined"""
