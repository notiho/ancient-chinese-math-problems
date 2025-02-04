"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
術曰：以句高乘東南隅入下股，如上股而一，所得減句高，餘為法；以東北隅下股減東南隅下股，餘以乘矩間為實。實如法而一，得邑南北長也。求邑廣：以入橫句乘矩間為實。實如法而一，即得邑東西廣。
答曰：南北長 a(=4/3)里 ；東西廣 b(=10/9)里 。
"""

#----- content starts here -----
"""
Suppose there is a mountain overlooking a city, and the city lies to the south of the mountain.
A carpenter's square is placed on the mountain, with the vertical leg (立句) being 3 chi and 5 cun high.
The endpoint of the vertical leg aligns with the southeast and northeast corners of the city.
From the endpoint of the vertical leg, looking toward the northeast corner, the lower leg (下股) extends inward by 1 zhang and 2 chi.
A horizontal leg (橫句) is placed at the intersection of the lower leg, and from the endpoint of the vertical leg, looking toward the northwest corner, the horizontal leg extends inward by 5 chi.
Looking toward the southeast corner, the lower leg extends inward by 1 zhang and 8 chi.
Another carpenter's square is set above, with the distance between the two squares being 4 zhang.
From the endpoint of the vertical leg, looking toward the southeast corner, the upper leg (上股) extends inward by 1 zhang, 7 chi, and 5 cun.
Question: What are the width (east-west) and length (north-south) of the city?

The procedure says:
To find the north-south length:
Multiply the height of the vertical leg by the inward extension of the lower leg toward the southeast corner.
Divide by the inward extension of the upper leg, subtract 1, and subtract the height of the vertical leg from the result. The remainder is the divisor.
Subtract the inward extension of the lower leg toward the southeast corner from the inward extension of the lower leg toward the northeast corner.
Multiply the remainder by the distance between the two carpenter's squares to get the dividend.
Divide the dividend by the divisor, subtract 1, and the result is the north-south length of the city.

To find the east-west width:
Multiply the inward extension of the horizontal leg by the distance between the two carpenter's squares to get the dividend.
Divide the dividend by the divisor, subtract 1, and the result is the east-west width of the city.

Answer: The north-south length is *a*(=4/3) li, and the east-west width is *b*(=10/9) li.
"""

# Constants
句高 = Fraction(3, 1) + Fraction(5, 10)  # 3 chi 5 cun = 3.5 chi
東北隅入下股 = Fraction(1, 1) * 10 + Fraction(2, 1)  # 1 zhang 2 chi = 12 chi
東南隅入下股 = Fraction(1, 1) * 10 + Fraction(8, 1)  # 1 zhang 8 chi = 18 chi
矩間 = Fraction(4, 1) * 10  # 4 zhang = 40 chi
上股 = Fraction(1, 1) * 10 + Fraction(7, 1) + Fraction(5, 10)  # 1 zhang 7 chi 5 cun = 17.5 chi
入橫句 = Fraction(5, 1)  # 5 chi

# 求邑南北長
# Step 1: Multiply the height of the vertical leg by the inward extension of the lower leg toward the southeast corner
南北長分子1 = 句高 * 東南隅入下股

# Step 2: Divide by the inward extension of the upper leg, subtract 1, and subtract the height of the vertical leg
南北長法 = Fraction(南北長分子1, 上股) - 1 - 句高

# Step 3: Subtract the inward extension of the lower leg toward the southeast corner from the inward extension of the lower leg toward the northeast corner
南北長分子2 = 東北隅入下股 - 東南隅入下股

# Step 4: Multiply the remainder by the distance between the two carpenter's squares
南北長實 = 南北長分子2 * 矩間

# Step 5: Divide the dividend by the divisor, subtract 1
a = Fraction(南北長實, 南北長法) - 1  # 4/3 li

# 求邑東西廣
# Step 1: Multiply the inward extension of the horizontal leg by the distance between the two carpenter's squares
東西廣實 = 入橫句 * 矩間

# Step 2: Divide the dividend by the divisor, subtract 1
b = Fraction(東西廣實, 南北長法) - 1  # 10/9 li#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 797/3
Variable 'b' has wrong value. Expected: 10/9, Actual: -2009/9"""
