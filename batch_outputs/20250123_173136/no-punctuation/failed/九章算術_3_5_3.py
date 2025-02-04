"""
今有稟粟大夫不更簪裹上造公士凡五人一十五斗今有大夫一人後來亦當稟五斗倉無粟欲以衰出之問各幾何
術曰各置所稟粟斛斗數爵次均之以為列衰副并而加後來大夫亦五斗得二十以為法以五斗乘未并者各自為實實如法得一斗
荅曰大夫出 a斗 不更出 b斗 簪褭出 c斗 上造出 d斗 公士出 e斗 
"""

"""
Suppose there are 5 people: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi. 
They have a total of 15 dou of millet to distribute. 
Now, an additional Daifu arrives later and also needs to receive 5 dou of millet. 
The granary is empty, so the millet must be taken proportionally from the original 5 people according to their ranks.

The procedure says: Place the millet amounts (in hu and dou) that each rank originally receives in a line. 
Equalize them according to their ranks, forming a sequence of decreasing weights. 
Add the amount for the newly arrived Daifu (5 dou), obtaining 20 as the divisor. 
Multiply 5 dou by the uncombined weights, forming the dividends. 
Divide the dividends by the divisor, obtaining the amount of millet each person must give up.

Answer: the Daifu gives up *a* dou, the Bugeng gives up *b* dou, the Zanniao gives up *c* dou, the Shangzao gives up *d* dou, and the Gongshi gives up *e* dou.
"""

# 各置所稟粟斛斗數爵次均之以為列
爵數 = [5, 4, 3, 2, 1]  # 爵次 weights for Daifu, Bugeng, Zanniao, Shangzao, Gongshi

# 後來大夫亦五斗
後來大夫 = 5

# 副并而加後來大夫亦五斗得二十以為法
法 = sum(爵數) + 後來大夫

# 以五斗乘未并者
實 = [後來大夫 * i for i in 爵數]

# 各自為實，實如法得一斗
a, b, c, d, e = [Fraction(i, 法) for i in 実]
"""
Code error: name '実' is not defined"""
