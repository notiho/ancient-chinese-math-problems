"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
術曰：以句高乘東南隅入下股，如上股而一，所得減句高，餘為法；以東北隅下股減東南隅下股，餘以乘矩間為實。實如法而一，得邑南北長也。求邑廣：以入橫句乘矩間為實。實如法而一，即得邑東西廣。
答曰：南北長 a(=4/3)里 ；東西廣 b(=10/9)里 。
"""

#----- content starts here -----
"""
Suppose there is a mountain overlooking a city, and the city is south of the mountain. 
A carpenter's square is placed on the mountain, with the vertical leg (ju) set to a height of 3 chi 5 cun. 
The end of the vertical leg aligns with the southeast and northeast corners of the city. 
From the end of the vertical leg, looking toward the northeast corner, the lower leg (gu) is entered by 1 zhang 2 chi. 
A horizontal leg is then placed at the intersection of the lower leg, and from the end of the vertical leg, looking toward the northwest corner, the horizontal leg is entered by 5 chi. 
Looking toward the southeast corner, the lower leg is entered by 1 zhang 8 chi. 
Another carpenter's square is set above, with the distance between the squares being 4 zhang. 
From the end of the vertical leg, looking toward the southeast corner, the upper leg is entered by 1 zhang 7 chi 5 cun. 
Question: What are the width and length of the city?

The procedure says: 
To find the north-south length: Multiply the vertical leg height by the southeast corner's lower leg entry. Divide by the upper leg entry, subtract the vertical leg height, and the remainder is the divisor. 
Subtract the southeast corner's lower leg entry from the northeast corner's lower leg entry, multiply the remainder by the distance between the squares, and this is the dividend. 
Divide the dividend by the divisor to get the city's north-south length.

To find the east-west width: Multiply the horizontal leg entry by the distance between the squares, and this is the dividend. 
Divide the dividend by the divisor to get the city's east-west width.

Answer: The north-south length is *a*(=4/3) li, and the east-west width is *b*(=10/9) li.
"""

# 句高三尺五寸
句高 = Fraction(3, 1) + Fraction(5, 10)

# 東北隅入下股一丈二尺
東北隅下股 = Fraction(1, 1) * 10 + Fraction(2, 1)

# 東南隅入下股一丈八尺
東南隅下股 = Fraction(1, 1) * 10 + Fraction(8, 1)

# 入橫句五尺
入橫句 = Fraction(5, 1)

# 矩間相去四丈
矩間 = Fraction(4, 1) * 10

# 東南隅入上股一丈七尺五寸
東南隅上股 = Fraction(1, 1) * 10 + Fraction(7, 1) + Fraction(5, 10)

# 求邑南北長
# 以句高乘東南隅入下股
南北實 = 句高 * 東南隅下股

# 如上股而一
南北實 = Fraction(南北實, 東南隅上股)

# 所得減句高，餘為法
南北法 = 南北實 - 句高

# 以東北隅下股減東南隅下股
南北差 = 東北隅下股 - 東南隅下股

# 餘以乘矩間為實
南北實 = 南北差 * 矩間

# 實如法而一
南北長 = Fraction(南北實, 南北法)

# 求邑東西廣
# 以入橫句乘矩間為實
東西實 = 入橫句 * 矩間

# 實如法而一
東西廣 = Fraction(東西實, 南北法)

# Convert to li (1 li = 180 chi)
a = Fraction(North_South_Length, 180)  # 4/3 li
b = Fraction(East_West_Width, 180)  # 10/9 li#----- content ends here -----

"""
Code error: name 'North_South_Length' is not defined"""
