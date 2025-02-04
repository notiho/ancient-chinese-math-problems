"""
今有大夫、不更、簪褭、上造、公士，凡五人，共出百錢。欲令高爵出少，以次漸多，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：置爵數各自為衰，而返衰之，副并為法。以百錢乘未并者各自為實。實如法得一錢。
荅曰：大夫出 a錢 。不更出 b錢 。簪褭出 c錢 。上造出 d錢 。公士出 e錢 。
"""

#----- content starts here -----
"""
Suppose there is a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi (official titles of varying ranks), in total 5 people.
Together, they contribute 100 qian. It is desired that the higher-ranked officials contribute less, and the lower-ranked officials contribute more, gradually increasing by rank.
Question: how much does each contribute?

The reverse-weighting procedure says: Arrange the weights (ranks) and let them multiply with each other. The moving one becomes the weight of the unmoving one.
The procedure says: Place the rank numbers, each becoming its own weight, and reverse-weight them. Add the auxiliary values, obtaining the divisor.
Multiply the 100 qian by the unreversed weights, each becoming its own dividend. Divide by the divisor to obtain the contribution in qian.

The answer says: the Daifu contributes *a* qian, the Bugeng contributes *b* qian, the Zanniao contributes *c* qian, the Shangzao contributes *d* qian, and the Gongshi contributes *e* qian.
"""

# 置爵數各自為衰
爵數 = [5, 4, 3, 2, 1]

# 返衰之，列置衰而令相乘，動者為不動者衰
返衰 = []
for i in range(len(爵數)):
    weight = 1
    for j in range(len(爵數)):
        if i != j:
            weight *= 爵數[j]
    返衰.append(weight)

# 副并為法
法 = sum(返衰)

# 以百錢乘未并者各自為實
總錢 = 100
實 = [總錢 * weight for weight in 返衰]

# 實如法得一錢
a, b, c, d, e = [Fraction(value, 法) for value in 实]#----- content ends here -----

"""
Code error: name '实' is not defined"""
