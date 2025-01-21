"""
今有絹三千四百六十三匹一丈三尺四寸毎匹三貫五百文問計錢幾何
術曰先置絹數丈尺已下折半五因以五七因之即得
答曰 a貫
"""

"""
Suppose there are 3463 bolts of silk, each measuring 1 zhang, 3 chi, and 4 cun in length. 
Each bolt is worth 3 guan and 500 wen.
Question: what is the total amount of money?

The procedure says: First, place the number of bolts of silk. 
For the zhang, chi, and below, reduce by half of 5 (i.e., divide by 2.5). 
Then multiply by 5 and multiply by 7 to obtain the result.

Answer: *a* guan.
"""

# 絹數
絹數 = 3463

# 每匹長度 1丈3尺4寸
丈 = 1
尺 = 3
寸 = 4

# 每匹價值 3貫500文
每匹價值 = 3 * 1000 + 500  # 1貫 = 1000文

# 先置絹數
總價值 = 絹數 * 每匹價值

# 丈尺已下折半五 (即除以2.5)
折半五 = Fraction(1, 2.5)

# 因以五
因五 = 5

# 七因之
因七 = 7

# 計算總價值
a = Fraction(總價值, 1000)  # 轉換為貫
"""
Code error: both arguments should be Rational instances"""
