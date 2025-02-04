"""
今有長安、洛陽相去九百里，車輪一匝一丈八尺。欲自洛陽至長安。問：輪匝幾何？
答曰： a 匝。
"""

#----- content starts here -----
"""
Suppose the distance between Chang'an and Luoyang is 900 li. A cartwheel makes one full revolution (circumference) of 1 zhang and 8 chi.  
Question: How many revolutions does the wheel make to travel from Luoyang to Chang'an?

Answer: *a* revolutions.
"""

# 長安、洛陽相去九百里
distance = 900  # in li

# 1 li = 180 zhang
distance_in_zhang = distance * 180

# 車輪一匝一丈八尺
wheel_circumference = 1 * 10 + 8  # 1 zhang = 10 chi, so 1 zhang 8 chi = 18 chi

# 計算輪匝數
a = Fraction(distance_in_zhang * 10, wheel_circumference)  # Convert zhang to chi for consistency

a  # Output the number of revolutions#----- content ends here -----

"""
"""
