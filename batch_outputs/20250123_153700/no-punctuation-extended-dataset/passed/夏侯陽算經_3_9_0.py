"""
今有十五家共納兩稅錢一十貫文甲三人人各一貫文乙五人人各七百文丙七人人各五百文續奉符令都卻還七貫三百問隨元納數給付各幾何
術曰置卻還數以百除之所得為毎百還錢之數置百文減之餘為毎百錢在庫之數各置此數以各人所納錢數乗之各得其數
答曰甲 a人 各還 b文 乙 c人 各還 d文 丙 e人 各還 f文
"""

"""
Suppose there are 15 households collectively paying two tax payments of 10 guan (10,000 wen). 
- Group A consists of 3 people, each paying 1 guan (1,000 wen).
- Group B consists of 5 people, each paying 700 wen.
- Group C consists of 7 people, each paying 500 wen.
Later, an official decree orders a refund of 7 guan and 300 wen (7,300 wen). 
Question: Based on the original amounts paid, how much does each person in each group receive as a refund?

The procedure says:
- Place the refund amount and divide it by 100. The result is the amount refunded per 100 wen.
- Place 100 wen and subtract the refund per 100 wen. The remainder is the amount retained in the treasury per 100 wen.
- For each group, multiply the amount each person originally paid by the refund per 100 wen to calculate the refund for each person.

Answer: Group A consists of *a* people, each refunded *b* wen. 
Group B consists of *c* people, each refunded *d* wen. 
Group C consists of *e* people, each refunded *f* wen.
"""

# Total households and refund amount
總戶數 = 15
卻還數 = 7300  # 7 guan and 300 wen = 7,300 wen

# Group details
甲人數 = 3
甲每人納 = 1000  # 1 guan = 1,000 wen

乙人數 = 5
乙每人納 = 700

丙人數 = 7
丙每人納 = 500

# 置卻還數，以百除之，所得為每百還錢之數
每百還錢 = Fraction(卻還數, 100)

# 置百文，減之，餘為每百錢在庫之數
每百庫存 = 100 - 每百還錢

# 各置此數，以各人所納錢數乘之，各得其數
甲每人還 = Fraction(甲每人納 * 每百還錢, 100)
乙每人還 = Fraction(乙每人納 * 每百還錢, 100)
丙每人還 = Fraction(丙每人納 * 每百還錢, 100)

# Final results
a = 甲人數
b = 甲每人還
c = 乙人數
d = 乙每人還
e = 丙人數
f = 丙每人還
"""
"""
