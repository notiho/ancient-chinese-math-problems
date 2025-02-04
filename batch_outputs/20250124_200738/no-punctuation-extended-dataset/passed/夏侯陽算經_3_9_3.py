"""
今有十五家共納兩稅錢一十貫文甲三人人各一貫文乙五人人各七百文丙七人人各五百文續奉符令都卻還七貫三百問隨元納數給付各幾何
術曰置卻還數以百除之所得為毎百還錢之數置百文減之餘為毎百錢在庫之數各置此數以各人所納錢數乗之各得其數
答曰甲 a人 各還 b文 乙 c人 各還 d文 丙 e人 各還 f文
"""

#----- content starts here -----
"""
Suppose there are 15 households collectively paying two-tax money of 10 guan wen.
Among them:
- Group A has 3 people, and each pays 1 guan wen.
- Group B has 5 people, and each pays 700 wen.
- Group C has 7 people, and each pays 500 wen.
Later, an official decree orders a refund of 7 guan 300 wen.
Question: Based on the original amount paid, how much does each person in each group get refunded?

The procedure says:
- Place the refund amount and divide it by 100. The result is the amount refunded per 100 wen.
- Place 100 wen and subtract the refund amount per 100 wen. The remainder is the amount retained in the treasury per 100 wen.
- For each group, multiply the amount retained per 100 wen by the amount originally paid by each person in that group to determine the amount retained for each person.
- Subtract the retained amount from the original amount paid by each person to determine the refund for each person.

Answer:
- Group A: *a* people, each refunded *b* wen.
- Group B: *c* people, each refunded *d* wen.
- Group C: *e* people, each refunded *f* wen.
"""

# Total households and refund amount
總戶數 = 15
總納稅 = 10 * 1000  # Convert guan to wen
卻還數 = 7 * 1000 + 300  # Convert guan and wen to wen

# Group details
甲人數 = 3
甲每人納稅 = 1 * 1000  # Convert guan to wen

乙人數 = 5
乙每人納稅 = 700

丙人數 = 7
丙每人納稅 = 500

# 置卻還數以百除之，所得為每百還錢之數
每百還錢 = Fraction(卻還數, 100)

# 置百文減之，餘為每百錢在庫之數
每百在庫 = 100 - 每百還錢

# 各置此數以各人所納錢數乘之，各得其數
甲每人在庫 = Fraction(每百在庫 * 甲每人納稅, 100)
乙每人在庫 = Fraction(每百在庫 * 乙每人納稅, 100)
丙每人在庫 = Fraction(每百在庫 * 丙每人納稅, 100)

# 各人退款 = 原納稅 - 在庫
甲每人退款 = 甲每人納稅 - 甲每人在庫
乙每人退款 = 乙每人納稅 - 乙每人在庫
丙每人退款 = 丙每人納稅 - 丙每人在庫

# Results
a = 甲人數
b = 甲每人退款
c = 乙人數
d = 乙每人退款
e = 丙人數
f = 丙每人退款#----- content ends here -----

"""
"""
