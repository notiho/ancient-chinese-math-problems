"""
今有十五家共納兩稅錢一十貫文甲三人人各一貫文乙五人人各七百文丙七人人各五百文續奉符令都卻還七貫三百問隨元納數給付各幾何
術曰置卻還數以百除之所得為毎百還錢之數置百文減之餘為毎百錢在庫之數各置此數以各人所納錢數乗之各得其數
答曰甲 a人 各還 b文 乙 c人 各還 d文 丙 e人 各還 f文
"""

#----- content starts here -----
"""
Suppose there are 15 households collectively paying two taxes, totaling 10 guan and 0 wen.
- Group A consists of 3 people, each paying 1 guan (1000 wen).
- Group B consists of 5 people, each paying 700 wen.
- Group C consists of 7 people, each paying 500 wen.
Later, an official order is issued to return 7 guan and 300 wen in total.
Question: How much should each person in each group receive back, proportional to their original contributions?

The procedure says:
1. Place the amount to be returned and divide it by 100. The result is the amount returned per 100 wen.
2. Place 100 wen and subtract the amount returned per 100 wen. The remainder is the amount left in the treasury per 100 wen.
3. Place this remainder and multiply it by the amount each person originally paid. Each person’s returned amount is obtained.

Answer:
- Group A: *a* people, each receives *b* wen.
- Group B: *c* people, each receives *d* wen.
- Group C: *e* people, each receives *f* wen.
"""

# Total tax paid
總納稅 = 10 * 1000  # 10 guan = 10000 wen

# Group details
甲人數 = 3
甲每人納稅 = 1000  # 1 guan = 1000 wen

乙人數 = 5
乙每人納稅 = 700

丙人數 = 7
丙每人納稅 = 500

# Total amount to be returned
卻還總數 = 7 * 1000 + 300  # 7 guan and 300 wen = 7300 wen

# 每百還錢之數
每百還錢 = Fraction(卻還總數, 總納稅) * 100

# 每百錢在庫之數
每百在庫 = 100 - 每百還錢

# 甲各人還錢
甲每人還錢 = Fraction(每百還錢, 100) * 甲每人納稅

# 乙各人還錢
乙每人還錢 = Fraction(每百還錢, 100) * 乙每人納稅

# 丙各人還錢
丙每人還錢 = Fraction(每百還錢, 100) * 丙每人納稅

# Results
a = 甲人數
b = 甲每人還錢

c = 乙人數
d = 乙每人還錢

e = 丙人數
f = 丙每人還錢#----- content ends here -----

"""
"""
