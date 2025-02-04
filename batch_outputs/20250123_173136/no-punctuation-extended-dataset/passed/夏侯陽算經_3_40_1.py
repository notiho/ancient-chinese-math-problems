"""
今有兵一萬四千五百七十五人毎人給錢一貫四百四十文問錢幾何
術曰先置人數添四四即得
答曰 a貫 文
"""

"""
Suppose there are 14,575 soldiers. Each soldier is given 1 guan and 440 wen.
Question: how much money is needed in total?

The procedure says: First, place the number of people. Multiply it by 440 and add it to the number of people. This gives the total amount in wen.
Convert the total wen into guan and wen.

Answer: *a* guan and *b* wen.
"""

# 兵一萬四千五百七十五人
人數 = 14575

# 每人給錢一貫四百四十文
每人錢 = 1 * 1000 + 440  # Convert 1 guan and 440 wen into total wen (1 guan = 1000 wen)

# 先置人數添四四即得
總錢文 = 人數 * 每人錢

# Convert total wen into guan and remaining wen
a = 總錢文 // 1000  # Total guan
b = 總錢文 % 1000   # Remaining wen
"""
"""
