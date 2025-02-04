"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
術曰：上置三十五頭，下置九十四足。半其足，得四十七，以少減多，再命之，上三除下三，上五除下五，下有一除上一，下有二除上二，即得。
答曰：雉 a(=23) ，兔 b(=12) 。
"""

#----- content starts here -----
"""
Suppose there are pheasants and rabbits in the same cage. There are 35 heads above and 94 feet below.
Question: how many pheasants and rabbits are there respectively?

The procedure says: Place 35 heads above and 94 feet below. Halve the feet, obtaining 47.
Subtract the smaller number from the larger number, and repeat the operation.
Divide the upper number by 3, and the lower number by 3.
Divide the upper number by 5, and the lower number by 5.
When there is 1 below, divide the upper number by 1.
When there are 2 below, divide the upper number by 2.
This gives the answer.

Answer: There are *a*(=23) pheasants and *b*(=12) rabbits.
"""

# 上置三十五頭
頭數 = 35

# 下置九十四足
足數 = 94

# 半其足，得四十七
半足 = 足數 // 2

# 雉有兩足，兔有四足
雉足 = 2
兔足 = 4

# 設雉數為 a，兔數為 b
# 頭數 = 雉數 + 兔數
# 足數 = 雉數 * 雉足 + 兔數 * 兔足

# 解聯立方程
# 頭數 = a + b
# 足數 = 2a + 4b

# 化簡第二個方程
# 足數 = 2a + 4b
# 足數 = 2(a + 2b)
# 半足 = a + 2b

# 聯立兩個方程：
# 1. 頭數 = a + b
# 2. 半足 = a + 2b

# 用代入法解：
# 從方程 (1) 得到 a = 頭數 - b
# 將 a 代入方程 (2):
# 半足 = (頭數 - b) + 2b
# 半足 = 頭數 + b

# 解出 b:
b = 半足 - 頭數  # 12

# 解出 a:
a = 頭數 - b  # 23

# 答案
a = 23  # 雉數
b = 12  # 兔數#----- content ends here -----

"""
"""
