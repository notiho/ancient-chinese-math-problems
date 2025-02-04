"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a(=1140)翭 ， b(=3)翭 一錢 其 c(=960)翭 ， d(=4)翭 一錢
"""

"""
Suppose there is an expenditure of 610 qian to buy 2100 feathers (翭). It is desired to determine the rates of their relative value (贵贱率).
Question: what are the quantities and rates for each?

The procedure for reversing the rates says: Take the amount of money as the divisor (法), and the quantity being rated as the dividend (实). Divide the dividend by the divisor to get the rate for one unit. If the dividend is less than the divisor, subtract the dividend from the divisor, making the divisor smaller and the dividend larger. For two items, multiply the divisor and dividend by the respective quantities to determine the total quantities.

Answer: *a*(=1140) feathers at *b*(=3) feathers per qian, and *c*(=960) feathers at *d*(=4) feathers per qian.
"""

# 出錢六百一十
錢數 = 610

# 買羽二千一百翭
羽數 = 2100

# 貴賤率分為兩部分
# 第一部分：3翭一錢
# 第二部分：4翭一錢

# 設第一部分的羽數為 a，第二部分的羽數為 c
# 設第一部分的錢數為 x，第二部分的錢數為 y

# 總羽數條件：a + c = 2100
# 總錢數條件：x + y = 610
# 第一部分條件：x = a / 3
# 第二部分條件：y = c / 4

# 代入條件，解聯立方程：
# a + c = 2100
# a / 3 + c / 4 = 610

# 通分處理第二條件：
# 4a / 12 + 3c / 12 = 610
# 4a + 3c = 7320

# 解聯立方程：
# a + c = 2100
# 4a + 3c = 7320

# 消去 c：
# c = 2100 - a
# 4a + 3(2100 - a) = 7320
# 4a + 6300 - 3a = 7320
# a = 7320 - 6300
# a = 1140

# 求 c：
# c = 2100 - a
# c = 2100 - 1140
# c = 960

# 第一部分的羽數
a = 1140

# 第一部分的率
b = 3

# 第二部分的羽數
c = 960

# 第二部分的率
d = 4
"""
"""
