"""
今有大夫、不更、簪褭、上造、公士，凡五人，共出百錢。欲令高爵出少，以次漸多，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：置爵數各自為衰，而返衰之，副并為法。以百錢乘未并者各自為實。實如法得一錢。
荅曰：大夫出 a錢 。不更出 b錢 。簪褭出 c錢 。上造出 d錢 。公士出 e錢 。
"""

"""

"""

#----- content starts here -----

# 列置爵數，各自為衰
爵數 = [5, 4, 3, 2, 1]

# 返衰術：列置衰而令相乘，動者為不動者衰
返衰 = [1 / i for i in 爵數]

# 副并為法
法 = sum(返衰)

# 以百錢乘未并者各自為實
總錢 = 100
實 = [總錢 * i for i in 返衰]

# 實如法得一錢
a, b, c, d, e = [Fraction(i, 法) for i in 實]

# Outputs
a, b, c, d, e
#----- content ends here -----


"""

"""


"""
Code error: both arguments should be Rational instances"""
