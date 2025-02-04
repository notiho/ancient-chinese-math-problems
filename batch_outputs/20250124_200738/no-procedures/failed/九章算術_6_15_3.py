"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose a traveler's horse travels 300 li per day. The traveler forgets to bring their clothes, and after 1/3 of the day has passed, the host realizes it. 
The host takes the clothes and chases the traveler, catches up, gives the clothes, and returns home. 
When the host returns home, 3/4 of the day has passed.

Question: How far does the host's horse travel in one day if it does not rest?

Answer: The host's horse travels *a* li in one day.
"""

# 客馬日行 300 里
客馬日行 = 300

# 客馬每時行 (1 天 = 1 日 = 1 時辰)
客馬每時行 = 客馬日行 / 1

# 主人發現時間：日已三分之一
主人發現時間 = Fraction(1, 3)

# 主人返回時間：日四分之三
主人返回時間 = Fraction(3, 4)

# 主人用時追趕與返回
主人用時 = 主人返回時間 - 主人發現時間

# 主人馬速度比客馬快，設主人馬速度為 x 倍客馬速度
# 主人追趕與返回的總距離等於客馬在主人用時內行的距離
# 主人追趕與返回的總距離 = 主人馬速度 * 主人用時
主人馬速度 = Fraction(2, 1)#----- content ends here -----

"""
Missing variable in output: 'a'"""
