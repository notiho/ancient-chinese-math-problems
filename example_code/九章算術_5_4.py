#今有隄下廣二丈上廣八尺高四尺袤一十二丈七尺問積幾何
#荅曰七千一百一十二尺
#冬程人功四百四十四尺問用徒幾何
#術曰以積尺爲實程功尺數爲法實如法而一卽用徒人數
#荅曰 a人

from fractions import Fraction

# 七千一百一十二尺
積尺 = 7112

# 人功四百四十四尺
程功尺數 = 444

# 以積尺爲實
實 = 積尺

# 程功尺數爲法
法 = 程功尺數

# 實如法而一卽用徒人數
a = Fraction(實, 法)

