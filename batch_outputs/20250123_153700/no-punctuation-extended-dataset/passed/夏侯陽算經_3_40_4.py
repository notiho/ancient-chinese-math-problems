"""
今有兵一萬四千五百七十五人毎人給錢一貫四百四十文問錢幾何
術曰先置人數添四四即得
答曰 a貫 文
"""

"""
Suppose there are 14,575 soldiers. Each soldier is given 1 guan and 440 wen.
Question: how much money is needed in total?

The procedure says: First, place the number of people. Multiply it by 440 and add it to the number of guan. This gives the total.

Answer: *a* guan and *b* wen.
"""

# 兵一萬四千五百七十五人
兵數 = 14575

# 每人給錢一貫四百四十文
每人貫 = 1
每人文 = 440

# 計算總文數
總文數 = 兵數 * 每人文

# 換算為貫與文
總貫 = 兵數 * 每人貫 + 總文數 // 1000  # 每貫為1000文
剩餘文 = 總文數 % 1000

a = 總貫
b = 剩餘文
"""
"""
