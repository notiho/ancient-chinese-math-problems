"""
今有十五家共納兩稅錢一十貫文甲三人人各一貫文乙五人人各七百文丙七人人各五百文續奉符令都卻還七貫三百問隨元納數給付各幾何
術曰置卻還數以百除之所得為毎百還錢之數置百文減之餘為毎百錢在庫之數各置此數以各人所納錢數乗之各得其數
答曰甲 a人 各還 b文 乙 c人 各還 d文 丙 e人 各還 f文
"""

#----- content starts here -----
"""
Suppose there are 15 households collectively paying two-tax money of 10 guan-wen.
Group A has 3 people, each paying 1 guan-wen.
Group B has 5 people, each paying 700 wen.
Group C has 7 people, each paying 500 wen.
Later, an official order is issued to return 7 guan 300 wen in total.
Question: how much does each person in each group receive back according to their original contribution?

The procedure says: Place the amount to be returned and divide it by 100. The result is the amount of money returned per 100 wen.
Place 100 wen and subtract the returned amount per 100 wen. The remainder is the amount of money per 100 wen that stays in the treasury.
For each group, multiply this remainder by the amount of money each person originally paid. Each person in the group receives this amount.

Answer: Group A has *a* people, each receiving *b* wen.
Group B has *c* people, each receiving *d* wen.
Group C has *e* people, each receiving *f* wen.
"""

# Total return amount: 7 guan 300 wen
卻還總數 = 7 * 1000 + 300  # Convert guan to wen

# Divide by 100 to find the return per 100 wen
每百還錢數 = Fraction(卻還總數, 100)

# Place 100 wen and subtract the return amount per 100 wen
每百錢在庫數 = 100 - 每百還錢數

# Group A: 3 people, each paying 1 guan (1000 wen)
甲人數 = 3
甲每人納錢 = 1000
甲每人還錢 = Fraction(每百還錢數 * 甲每人納錢, 100)

# Group B: 5 people, each paying 700 wen
乙人數 = 5
乙每人納錢 = 700
乙每人還錢 = Fraction(每百還錢數 * 乙每人納錢, 100)

# Group C: 7 people, each paying 500 wen
丙人數 = 7
丙每人納錢 = 500
丙每人還錢 = Fraction(每百還錢數 * 丙每人納錢, 100)

# Final results
a = 甲人數
b = 甲每人還錢
c = 乙人數
d = 乙每人還錢
e = 丙人數
f = 丙每人還錢#----- content ends here -----

"""
"""
