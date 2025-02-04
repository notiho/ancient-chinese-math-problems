"""
今有大器五小器一容三斛大器一小器五容二斛問大小器各容幾何
術曰假令大器五斗小器亦五斗盈一十斗令之大器五斗五升小器二斗五升不足二斗
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰大器容 a斛 小器容 b斛 
"""

#----- content starts here -----
"""
Suppose there is a large vessel and a small vessel. Five large vessels and one small vessel together hold 3 hu. 
One large vessel and five small vessels together hold 2 hu.
Question: how much does each large vessel and each small vessel hold?

The procedure says: Suppose the large vessel holds 5 dou, and the small vessel also holds 5 dou, making a total of 10 dou.
Adjust it such that the large vessel holds 5 dou and 5 sheng, and the small vessel holds 2 dou and 5 sheng, leaving a shortage of 2 dou.

The procedure for excess and shortage says: Place the rates of output (the coefficients of the vessels) and the excess or shortage below them.
Multiply the rates of output by the excess or shortage, and add them together to form the dividend.
Add the excess and shortage together to form the divisor.
Divide the dividend by the divisor to find the solution. If there is a fraction, simplify it.
If the excess and shortage are the same, adjust the rates of output by subtracting the smaller from the larger, and simplify the divisor and dividend accordingly.

Answer: the large vessel holds *a* hu, and the small vessel holds *b* hu.
"""

# 大器五小器一容三斛
rate1_large = 5
rate1_small = 1
total1 = 3  # in hu

# 大器一小器五容二斛
rate2_large = 1
rate2_small = 5
total2 = 2  # in hu

# 盈不足術
# 盈不足各居其下
excess = total1  # 3 hu
shortage = total2  # 2 hu

# 令維乘所出率并以為實
dividend = (rate1_large * shortage + rate2_large * excess)

# 并盈不足為法
divisor = (rate1_large + rate2_small )

#----- content ends here -----

"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
