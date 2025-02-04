"""
今有十五家共納兩稅錢一十貫文甲三人人各一貫文乙五人人各七百文丙七人人各五百文續奉符令都卻還七貫三百問隨元納數給付各幾何
術曰置卻還數以百除之所得為毎百還錢之數置百文減之餘為毎百錢在庫之數各置此數以各人所納錢數乗之各得其數
答曰甲 a人 各還 b文 乙 c人 各還 d文 丙 e人 各還 f文
"""

#----- content starts here -----
"""
Suppose there are 15 households collectively paying a total of 10 guan wen in taxes. 
Group A consists of 3 people, each paying 1 guan wen. 
Group B consists of 5 people, each paying 700 wen. 
Group C consists of 7 people, each paying 500 wen. 
Later, an official decree orders that 7 guan 300 wen be refunded. 
Question: How much should each person in each group be refunded proportionally to their original contributions?

The procedure says: 
Place the amount to be refunded and divide it by 100. The result is the amount refunded per 100 wen. 
Place 100 wen and subtract the refunded amount per 100 wen. The remainder is the amount remaining in the treasury per 100 wen. 
For each group, multiply the amount remaining in the treasury per 100 wen by the amount each person in that group originally paid. 
Each person in the group receives their proportional refund.

Answer: Group A has *a* people, each refunded *b* wen. 
Group B has *c* people, each refunded *d* wen. 
Group C has *e* people, each refunded *f* wen.
"""

# Total refund amount: 7 guan 300 wen
# Convert to wen
卻還數 = 7 * 1000 + 300

# Total tax paid: 10 guan wen
# Convert to wen
總納稅 = 10 * 1000

# Group details
甲人數 = 3
甲每人納稅 = 1000  # 1 guan = 1000 wen

乙人數 = 5
乙每人納稅 = 700

丙人數 = 7
丙每人納稅 = 500

# 置卻還數以百除之，所得為每百還錢之數
每百還錢 = Fraction(卻還數, 總納稅) * 100

# 置百文減之，餘為每百錢在庫之數
每百在庫 = 100 - 每百還錢

# 各置此數以各人所納錢數乘之，各得其數
甲每人還 = Fraction(甲每人納稅 * 每百還錢, 100)
乙每人還 = Fraction(乙每人納稅 * 每百還錢, 100)
丙每人還 = Fraction(丙每人納稅 * 每百還錢, 100)

# Results
a = 甲人數
b = 甲每人還
c = 乙人數
d = 乙每人還
e = 丙人數
f = 丙每人還#----- content ends here -----

"""
"""
