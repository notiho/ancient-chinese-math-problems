"""
今有絹三千四百六十三匹一丈三尺四寸毎匹三貫五百文問計錢幾何
術曰先置絹數丈尺已下折半五因以五七因之即得
答曰 a貫
"""

#----- content starts here -----
"""
Suppose there are 3463 bolts of silk, each measuring 1 zhang, 3 chi, and 4 cun, and each bolt is worth 3 guan and 500 wen.
Question: how much money is the total worth?

The procedure says: First, place the number of bolts of silk. For the zhang, chi, and below, convert [the lengths] into halves and fives. Then multiply by 5 and 7, and it is obtained.

Answer: *a* guan.
"""

# 絹三千四百六十三匹
絹數 = 3463

# 每匹一丈三尺四寸
丈 = 1
尺 = 3
寸 = 4

# 每匹三貫五百文
每匹價值 = 3 * 1000 + 500  # Convert guan to wen (1 guan = 1000 wen)

# 先置絹數
總絹數 = 絹數

# 丈尺已下折半五
總長度 = 丈 * 10 + 尺 + Fraction(寸, 10)  # Convert zhang, chi, cun to a single unit (chi)
折半五 = 總長度 * Fraction(1, 2) * 5

# 因以五七因之即得
總價值 = 總絹數 * 每匹價值

# Convert total value from wen to guan
a = Fraction(總價值, 1000)  # Convert wen back to guan#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4848669/400, Actual: 24241/2"""
