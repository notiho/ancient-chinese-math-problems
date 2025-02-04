"""
今有鱉臑下廣五尺無袤上袤四尺無廣高七尺問積幾何
術曰廣袤相乘以高乘之六而一
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a truncated pyramid-like shape (a frustum) with:
- The bottom width (廣) being 5 chi and no length (袤),
- The top length (袤) being 4 chi and no width (廣),
- The height (高) being 7 chi.
Question: what is the volume?

The procedure says: Multiply the width and length together, then multiply by the height. Divide by 6 to obtain the volume.

Answer: *a* cubic chi.
"""

# 下廣五尺
下廣 = 5

# 上袤四尺
上袤 = 4

# 高七尺
高 = 7

# 廣袤相乘
廣袤積 = 下廣 * 上袤

# 以高乘之
體積 = 廣袤積 * 高

# 六而一
a = Fraction(體積, 6)#----- content ends here -----

"""
"""
