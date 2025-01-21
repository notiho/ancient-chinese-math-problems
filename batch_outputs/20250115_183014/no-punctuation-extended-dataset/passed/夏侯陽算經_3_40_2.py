"""
今有兵一萬四千五百七十五人毎人給錢一貫四百四十文問錢幾何
術曰先置人數添四四即得
答曰 a貫 文
"""

"""
Suppose there are 14,575 soldiers. Each soldier is given 1 guan and 440 wen.
Question: how much money is needed in total?

The procedure says: First, place the number of people. Multiply it by 440, then divide by 1,000 to convert wen into guan. Add the guan part (1 guan per person). This gives the total amount.

Answer: *a* guan and *b* wen.
"""

# 兵一萬四千五百七十五人
兵 = 14575

# 每人給錢一貫四百四十文
每人貫 = 1
每人文 = 440

# 先置人數，計算總文數
總文 = 兵 * 每人文

# 將總文數轉換為貫和文
總貫 = 總文 // 1000  # 每 1000 文為 1 貫
剩餘文 = 總文 % 1000

# 加上每人 1 貫的部分
總貫 += 兵 * 每人貫

# 答案
a = 總貫
b = 剩餘文
"""
"""
