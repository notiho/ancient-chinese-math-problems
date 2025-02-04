"""
今有雉兔同籠上有三十五頭下有九十四足問雉兔各幾何
術曰上置三十五頭下置九十四足半其足得四十七以少減多再命之上三除下三上五除下五下有一除上一下有二除上二即得
答曰雉 a 兔 b 
"""

#----- content starts here -----
"""
Suppose there are pheasants and rabbits in the same cage. 
There are 35 heads above and 94 feet below.
Question: how many pheasants and rabbits are there respectively?

The procedure says: Place the 35 heads above and the 94 feet below.
Halve the feet, obtaining 47.
Subtract the smaller number from the larger number, and double the result.
Divide the result by 3 for the pheasants and by 5 for the rabbits.
If there is 1 left below, subtract 1 from the pheasants.
If there are 2 left below, subtract 2 from the pheasants.
This gives the result.

Answer: there are *a* pheasants and *b* rabbits.
"""

# 上有三十五頭
頭 = 35

# 下有九十四足
足 = 94

# 半其足得四十七
半足 = 足 // 2

# 以少減多再命之
差 = 半足 - 頭

# 上三除下三
pheasants = 差 * 2 // 3

# 上五除下五
rabbits = 頭 - pheasants

# 答曰雉 a 兔 b
a = pheasants
b = rabbits#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 23, Actual: 8
Variable 'b' has wrong value. Expected: 12, Actual: 27"""
