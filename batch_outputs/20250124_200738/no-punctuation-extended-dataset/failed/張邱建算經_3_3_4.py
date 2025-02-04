"""
今有倉東西袤一丈二尺南北廣七尺南壁髙九尺北壁髙八尺問受粟幾何
術曰併南北壁髙而半之以廣袤乘之為實實如斛法而一得斛數
答曰得 a斛
"""

#----- content starts here -----
"""
Suppose there is a granary with an east-west length of 1 zhang 2 chi, a north-south width of 7 chi, a south wall height of 9 chi, and a north wall height of 8 chi.
Question: how much millet can it hold?

The procedure says: Add the heights of the south and north walls, then halve the sum.
Multiply this by the width and length to obtain the volume.
Divide the volume by the hu divisor (10 cubic chi per hu) to obtain the number of hu.

Answer: it holds *a* hu.
"""

# 東西袤一丈二尺
袤 = 1 * 10 + 2  # Convert zhang and chi to chi

# 南北廣七尺
廣 = 7

# 南壁髙九尺
南壁高 = 9

# 北壁髙八尺
北壁高 = 8

# 併南北壁髙而半之
平均高 = (南壁高 + 北壁高) / 2

# 以廣袤乘之，為實
實 = 平均高 * 廣 * 袤

# 斛法：10立方尺為1斛
斛法 = 10

# 實如斛法而一，得斛數
a = Fraction(實, 斛法)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
