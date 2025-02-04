"""
今有登山臨邑，邑在山南。偃矩山上，令句高三尺五寸。令句端與邑東南隅及東北隅參相直。從句端遙望東北隅，入下股一丈二尺。又施橫句于入股之會，從立句端望西北隅，入橫句五尺。望東南隅，入下股一丈八尺。又設重矩于上，令矩間相去四丈。更從立句端望東南隅，入上股一丈七尺五寸。問邑廣長各幾何？
術曰：以句高乘東南隅入下股，如上股而一，所得減句高，餘為法；以東北隅下股減東南隅下股，餘以乘矩間為實。實如法而一，得邑南北長也。求邑廣：以入橫句乘矩間為實。實如法而一，即得邑東西廣。
答曰：南北長 a(=4/3)里 ；東西廣 b(=10/9)里 。
"""

"""
Suppose there is a mountain overlooking a city, with the city located to the south of the mountain. 
A carpenter's square is placed on the mountain, with the vertical leg (立句) set to a height of 3 chi 5 cun. 
The endpoint of the vertical leg is aligned with the southeast and northeast corners of the city. 
From the endpoint of the vertical leg, looking toward the northeast corner, the lower leg (下股) extends inward by 1 zhang 2 chi. 
A horizontal leg (橫句) is then placed at the meeting point of the lower leg, and from the endpoint of the vertical leg, looking toward the northwest corner, the horizontal leg extends inward by 5 chi. 
Looking toward the southeast corner, the lower leg extends inward by 1 zhang 8 chi. 
A second carpenter's square is set above the first, with the distance between the two squares being 4 zhang. 
From the endpoint of the vertical leg of the upper square, looking toward the southeast corner, the upper leg (上股) extends inward by 1 zhang 7 chi 5 cun. 
Question: What are the north-south length and east-west width of the city?

The procedure says: 
To find the north-south length: Multiply the height of the vertical leg by the inward extension of the lower leg toward the southeast corner. Divide by the inward extension of the upper leg, then subtract the height of the vertical leg. The remainder is the divisor. Subtract the inward extension of the lower leg toward the southeast corner from the inward extension of the lower leg toward the northeast corner. Multiply the result by the distance between the two squares. This is the dividend. Divide the dividend by the divisor to get the north-south length of the city.

To find the east-west width: Multiply the inward extension of the horizontal leg by the distance between the two squares. This is the dividend. Divide the dividend by the divisor to get the east-west width of the city.

Answer: The north-south length is *a*(=4/3) li, and the east-west width is *b*(=10/9) li.
"""

from fractions import Fraction

# 立句高 3 尺 5 寸
句高 = Fraction(3 * 10 + 5, 10)  # Convert to chi (3 chi 5 cun = 3.5 chi)

# 東南隅入下股 1 丈 2 尺
東南隅下股 = Fraction(1 * 10 + 2, 10)  # Convert to chi (1 zhang 2 chi = 12 chi)

# 東北隅入下股 1 丈 8 尺
東北隅下股 = Fraction(1 * 10 + 8, 10)  # Convert to chi (1 zhang 8 chi = 18 chi)

# 入橫句 5 尺
入橫句 = Fraction(5, 10)  # Convert to chi (5 chi)

# 矩間相去 4 丈
矩間 = Fraction(4 * 10, 10)  # Convert to chi (4 zhang = 40 chi)

# 上股 1 丈 7 尺 5 寸
上股 = Fraction(1 * 10 + 7 + 5 / 10, 10)  # Convert to chi (1 zhang 7 chi 5 cun = 17.5 chi)

# 求邑南北長
# 以句高乘東南隅入下股，如上股而一
南北法 = Fraction(句高 * 東南隅下股, 上股) - 句高

# 東北隅下股減東南隅下股
南北實 = (東北隅下股 - 東南隅下股) * 矩間

# 實如法而一
南北長 = Fraction(南北實, 南北法)  # 4/3 里

# 求邑東西廣
# 以入橫句乘矩間為實
東西實 = 入橫句 * 矩間

# 實如法而一
東西廣 = Fraction(東西實, 南北法)  # 10/9 里

a = 南北長  # 4/3 里
b = 東西廣  # 10/9 里
"""
Code error: both arguments should be Rational instances"""
