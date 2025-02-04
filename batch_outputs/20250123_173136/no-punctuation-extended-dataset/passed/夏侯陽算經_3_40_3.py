"""
今有兵一萬四千五百七十五人毎人給錢一貫四百四十文問錢幾何
術曰先置人數添四四即得
答曰 a貫 文
"""

"""
Suppose there are 14,575 soldiers. Each soldier is given 1 guan and 440 wen.
Question: how much money is required in total?

The procedure says: First, place the number of soldiers. Multiply it by 440, and add it to the number of soldiers. This gives the total amount in wen.
Convert the total amount into guan and wen.

Answer: *a* guan and *b* wen.
"""

# 兵一萬四千五百七十五人
兵數 = 14575

# 每人給錢一貫四百四十文
每人錢_文 = 1 * 1000 + 440  # 1貫 = 1000文

# 先置人數添四四即得
總錢_文 = 兵數 * 每人錢_文

# 將總文數轉換為貫和文
a = 總錢_文 // 1000  # 貫
b = 總錢_文 % 1000  # 文
"""
"""
