"""
今有素一匹一丈，價直六百二十五。今有錢五百，問︰得素幾何？
術曰：以價直為法，以一匹一丈尺數乘今有錢數為實。實如法得素數。
荅曰：得素 a匹 。
"""

#----- content starts here -----

# 素一匹一丈，價直六百二十五
價直 = 625

# 錢五百
錢 = 500

# 一匹一丈尺數
匹數 = 1

# 以價直為法
法 = 價直

# 以一匹一丈尺數乘今有錢數為實
實 = 匹數 * 錢

# 實如法得素數
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1, Actual: 4/5"""
