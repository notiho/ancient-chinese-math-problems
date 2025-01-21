"""
今有絹三千四百六十三匹一丈三尺四寸毎匹三貫五百文問計錢幾何
術曰先置絹數丈尺已下折半五因以五七因之即得
答曰 a貫
"""

"""
Suppose there are 3463 bolts of silk, each measuring 1 zhang, 3 chi, and 4 cun. Each bolt is worth 3 guan and 500 wen.
Question: how much money in total?

The procedure says: First, place the number of bolts of silk. Convert zhang, chi, and below into halves and fifths. Then multiply by 5 and 7, and the result is obtained.

Answer: *a* guan.
"""

# 絹三千四百六十三匹
絹數 = 3463

# 每匹一丈三尺四寸
丈 = 1
尺 = 3
寸 = 4

# 每匹三貫五百文
每匹價值_貫 = 3
每匹價值_文 = 500

# 先置絹數
總絹數 = 絹數

# 丈尺已下折半五
# 1 丈 = 10 尺, 1 尺 = 10 寸
總長度_寸 = (丈 * 10 * 10) + (尺 * 10) + 寸  # Convert everything to cun
折半五 = Fraction(總長度_寸, 2 * 5)  # Divide by 2 and 5

# 因以五七因之即得
總價值_文 = 總絹數 * ((每匹價值_貫 * 1000) + 每匹價值_文)  # Convert guan to wen and calculate total value

# Convert total value to guan
a = Fraction(總價值_文, 1000)  # 1 guan = 1000 wen
"""
Variable 'a' has wrong value. Expected: 4848669/400, Actual: 24241/2"""
