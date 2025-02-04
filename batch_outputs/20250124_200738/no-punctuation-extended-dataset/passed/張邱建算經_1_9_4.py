"""
今有甲日行疾於乙日行二十五里而甲發洛陽七日至鄴乙發鄴九日至洛陽問鄴洛陽相去㡬何
術曰以甲乙所至日數相乗又以甲日行疾里數乗之為實以甲至日減乙至日數餘為法實如法而一
答曰 a里
"""

#----- content starts here -----
"""
Suppose person A travels 25 li faster per day than person B. 
Person A departs from Luoyang and takes 7 days to reach Ye, while person B departs from Ye and takes 9 days to reach Luoyang.
Question: What is the distance between Ye and Luoyang?

The procedure says: Multiply the number of days each person takes to reach their destination.
Then multiply this by the number of li by which A travels faster per day, obtaining the dividend.
Subtract the number of days A takes from the number of days B takes, obtaining the divisor.
Divide the dividend by the divisor, obtaining the distance.

Answer: *a* li.
"""

# 甲日行疾於乙日行二十五里
甲日行疾里數 = 25

# 甲發洛陽七日至鄴
甲至日數 = 7

# 乙發鄴九日至洛陽
乙至日數 = 9

# 以甲乙所至日數相乘
日數乘積 = 甲至日數 * 乙至日數

# 又以甲日行疾里數乘之，為實
實 = 日數乘積 * 甲日行疾里數

# 以甲至日減乙至日數，餘為法
法 = 乙至日數 - 甲至日數

# 實如法而一
a = Fraction(實, 法)#----- content ends here -----

"""
"""
