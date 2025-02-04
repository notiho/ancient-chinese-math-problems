"""
今有雉兔同籠上有三十五頭下有九十四足問雉兔各幾何
術曰上置三十五頭下置九十四足半其足得四十七以少減多再命之上三除下三上五除下五下有一除上一下有二除上二即得
答曰雉 a 兔 b 
"""

"""
Suppose there are pheasants and rabbits in the same cage. 
There are 35 heads on top and 94 feet below.
Question: how many pheasants and rabbits are there respectively?

The procedure says: Place 35 heads on top and 94 feet below.
Halve the feet, obtaining 47.
Subtract the smaller from the larger, and divide it twice.
For the top, divide by 3; for the bottom, divide by 3.
For the top, divide by 5; for the bottom, divide by 5.
If there is 1 below, subtract 1 from the top.
If there are 2 below, subtract 2 from the top.
This gives the result.

Answer: there are *a* pheasants and *b* rabbits.
"""

# 上有三十五頭
頭 = 35

# 下有九十四足
足 = 94

# 半其足得四十七
半足 = 足 // 2

# 以少減多
差 = 半足 - 頭

# 再命之上三除下三
上三 = 差 // 3
下三 = 差 % 3

# 上五除下五
上五 = 差 // 5
下五 = 差 % 5

# 下有一除上一
if 下三 == 1:
    上三 -= 1

# 下有二除上二
if 下三 == 2:
    上三 -= 2

# 雉數 (pheasants)
a = 頭 - 上三

# 兔數 (rabbits)
b = 上三
"""
Variable 'a' has wrong value. Expected: 23, Actual: 31
Variable 'b' has wrong value. Expected: 12, Actual: 4"""
