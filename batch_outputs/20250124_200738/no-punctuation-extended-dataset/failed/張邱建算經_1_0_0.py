"""
今有官獵得鹿賜圍兵初圍三人中賜鹿五頭次圍五人中賜鹿七頭次圍七人中賜鹿九頭併三圍賜鹿一十五萬二千三百三十三頭少半頭問圍兵㡬何
術曰以三賜人數互乗三賜鹿數併以為法三賜人數相乗併賜鹿數為實實如法而得一
答曰 a人
"""

#----- content starts here -----
"""
Suppose there is an official hunt, and the deer are distributed to the soldiers in the encirclement.
Initially, 3 people in the encirclement are given 5 deer.
Next, 5 people in the encirclement are given 7 deer.
Finally, 7 people in the encirclement are given 9 deer.
In total, the deer distributed across the three encirclements is 152,333 and a half.
Question: how many soldiers are in the encirclement?

The procedure says: Multiply the numbers of people in the three distributions with each other.
Add the numbers of deer distributed in the three cases, and take this as the divisor.
Multiply the numbers of people in the three distributions with the respective numbers of deer distributed, and add these, taking this as the dividend.
Divide the dividend by the divisor to obtain the number of soldiers.

Answer: *a* people.
"""

# 初圍三人中賜鹿五頭
初圍人數 = 3
初圍鹿數 = 5

# 次圍五人中賜鹿七頭
次圍人數 = 5
次圍鹿數 = 7

# 三圍七人中賜鹿九頭
三圍人數 = 7
三圍鹿數 = 9

# 併三圍賜鹿一十五萬二千三百三十三頭少半頭
總鹿數 = 152333 + Fraction(1, 2)

# 以三賜人數互乘
人數乘積 = 初圍人數 * 次圍人數 * 三圍人數

# 三賜鹿數併以為法
鹿數和 = 初圍鹿數 + 次圍鹿數 + 三圍鹿數
法 = 鹿數和

# 三賜人數相乘併賜鹿數為實
實 = (初圍人數 * 初圍鹿數) + (次圍人數 * 次圍鹿數) + (三圍人數 * 三圍鹿數)

# 實如法而得一
a = Fraction(總鹿數 * 實, 法 * 人數乘積)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 35000, Actual: 34427371/4410"""
