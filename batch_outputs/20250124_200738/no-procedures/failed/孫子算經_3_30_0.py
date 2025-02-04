"""
今有九里渠，三寸魚頭，頭相次。問：魚得幾何？
答曰： a 。
"""

#----- content starts here -----
"""
Suppose there is a canal 9 li long, and fish heads are spaced 3 cun apart, one after another in sequence.
Question: how many fish are there?

Answer: *a* fish.
"""

# 1 里 = 300 步, 1 步 = 5 尺, 1 尺 = 10 寸
# Therefore, 1 里 = 300 * 5 * 10 = 15000 寸

# Canal length in li
canal_length_li = 9

# Convert canal length to cun
canal_length_cun = canal_length_li * 15000

# Distance between fish heads in cun
distance_between_fish_heads = 3

# Total number of fish
a = canal_length_cun // distance_between_fish_heads

a  # Output the result#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 54000, Actual: 45000"""
