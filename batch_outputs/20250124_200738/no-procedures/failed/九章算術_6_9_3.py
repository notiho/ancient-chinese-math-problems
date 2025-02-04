"""
今有絡絲一斤為練絲一十二兩，練絲一斤為青絲一斤十二銖。今有青絲一斤，問︰本絡絲幾何？
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose 1 jin of raw silk (絡絲) produces 12 liang of refined silk (練絲), and 1 jin of refined silk produces 1 jin and 12 zhu of fine silk (青絲).
If there is 1 jin of fine silk (青絲), how much raw silk (絡絲) was originally required?

Answer: *a* jin.
"""

# 青絲一斤
青絲 = 1  # in jin

# 練絲一斤為青絲一斤十二銖
# 1 jin = 16 liang, so 12 zhu = 12 / 16 liang
練絲_to_青絲_ratio = 1 + Fraction(12, 16)

# 練絲 required to produce 1 jin of 青絲
練絲 = 青絲 / 練絲_to_青絲_ratio

# 絡絲一斤為練絲一十二兩
# 1 jin = 16 liang, so 12 liang = 12 / 16 jin
絡絲_to_練絲_ratio = Fraction(12, 16)

# 絡絲 required to produce 練絲
絡絲 = 練絲 / 絡絲_to_練絲_ratio

# Answer
a = 絡絲
a  # Output in jin#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 128/99, Actual: 16/21"""
