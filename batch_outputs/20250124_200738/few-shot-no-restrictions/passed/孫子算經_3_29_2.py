"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
術曰：上置三十五頭，下置九十四足。半其足，得四十七，以少減多，再命之，上三除下三，上五除下五，下有一除上一，下有二除上二，即得。
答曰：雉 a ，兔 b 。
"""

#----- content starts here -----
"""
Suppose there are pheasants and rabbits in the same cage. 
There are 35 heads (total animals) and 94 feet (total legs).
Question: how many pheasants and rabbits are there?

The procedure says: Place the 35 heads above and the 94 feet below. 
Halve the feet, obtaining 47. Subtract the smaller number from the larger number, and divide accordingly:
- Divide the remainder by 3 for the pheasants (3 legs per pheasant).
- Divide the remainder by 5 for the rabbits (5 legs per rabbit).
The solution is obtained.

Answer: there are *a* pheasants and *b* rabbits.
"""

# 上有三十五頭
heads = 35

# 下有九十四足
legs = 94

# 半其足，得四十七
half_legs = legs // 2

# 以少減多，再命之
difference = half_legs - heads

# 上三除下三 (pheasants have 2 legs)
pheasants = heads - difference

# 上五除下五 (rabbits have 4 legs)
rabbits = difference

# 答曰
a = pheasants
b = rabbits

# Output the result
a, b#----- content ends here -----

"""
"""
