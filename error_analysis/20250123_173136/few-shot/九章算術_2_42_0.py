"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per unit weight (both expensive and cheap rates).
Question: what are the rates for each unit of weight?

The procedure says: Place the quantities of shi, jun, jin, and liang as the divisor.
Multiply the total money by the respective unit to obtain the dividend.
Divide the dividend by the divisor to obtain the rate per unit.
If the dividend is less than the divisor, subtract the dividend from the divisor to reverse the calculation.
The divisor corresponds to the cheaper rate, and the dividend corresponds to the expensive rate.

Answer: The rate per shi is *a* qian, and the rate per liang is *b* qian.
The rate per jun is *c* qian, and the rate per jin is *d* qian.
"""
#ERR: misunderstood question

# 出錢一萬三千九百七十
錢數 = 13970

# 買絲一石二鈞二十八斤三兩五銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# 將所有重量轉換為最小單位（銖）
# 1 石 = 4 鈞, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
總銖 = (石 * 4 * 30 * 16 * 24) + (鈞 * 30 * 16 * 24) + (斤 * 16 * 24) + (兩 * 24) + 銖

# 計算每個單位的法（即重量轉換為銖）
石法 = 4 * 30 * 16 * 24
鈞法 = 30 * 16 * 24
斤法 = 16 * 24
兩法 = 24

# 計算每個單位的實（即錢數乘以單位重量）
石實 = 錢數 * 石法
鈞實 = 錢數 * 鈞法
斤實 = 錢數 * 斤法
兩實 = 錢數 * 兩法

# 計算每個單位的貴賤率
a = Fraction(石實, 總銖)  # 每石的貴賤率
b = Fraction(兩實, 總銖)  # 每兩的貴賤率
c = Fraction(鈞實, 總銖)  # 每鈞的貴賤率
d = Fraction(斤實, 總銖)  # 每斤的貴賤率
"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 643737600/79949
Variable 'b' has wrong value. Expected: 4, Actual: 335280/79949
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 160934400/79949
Variable 'd' has wrong value. Expected: 5, Actual: 5364480/79949"""
