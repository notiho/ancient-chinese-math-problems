"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
術曰：上置三十五頭，下置九十四足。半其足，得四十七，以少減多，再命之，上三除下三，上五除下五，下有一除上一，下有二除上二，即得。
答曰：雉 a ，兔 b 。
"""

#----- content starts here -----
"""
Suppose there are pheasants and rabbits in the same cage. 
There are 35 heads in total and 94 feet in total. 
Question: how many pheasants and rabbits are there?

The procedure says: Place the 35 heads above and the 94 feet below. 
Halve the number of feet, obtaining 47. Subtract the smaller number of heads from the larger number of halved feet. 
Divide the result by the difference in the number of feet between a rabbit and a pheasant (2 feet). 
This gives the number of rabbits. Subtract the number of rabbits from the total number of heads to get the number of pheasants.

Answer: *a* pheasants, *b* rabbits.
"""

# 上有三十五頭
heads = 35

# 下有九十四足
feet = 94

# 半其足，得四十七
half_feet = feet // 2

# 以少減多，再命之
difference = half_feet - heads

# 上三除下三 (difference in feet between a rabbit and a pheasant is 2)
rabbits = difference // 2

# 上五除下五 (number of pheasants is total heads minus rabbits)
pheasants = heads - rabbits

# 答曰：雉 a ，兔 b
a = pheasants
b = rabbits#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 23, Actual: 29
Variable 'b' has wrong value. Expected: 12, Actual: 6"""
