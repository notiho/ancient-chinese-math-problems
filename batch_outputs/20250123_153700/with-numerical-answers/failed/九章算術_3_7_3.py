"""
今有大夫、不更、簪褭、上造、公士，凡五人，共出百錢。欲令高爵出少，以次漸多，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：置爵數各自為衰，而返衰之，副并為法。以百錢乘未并者各自為實。實如法得一錢。
荅曰：大夫出 a(=1200/137)錢 。不更出 b(=1500/137)錢 。簪褭出 c(=2000/137)錢 。上造出 d(=3000/137)錢 。公士出 e(=6000/137)錢 。
"""

"""
Suppose there is a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi [official titles of varying ranks], in total 5 people.
Together, they contribute 100 qian. It is desired that the higher-ranked officials contribute less, and the contributions increase gradually by rank.
Question: how much does each contribute?

The reverse-decreasing procedure says: Arrange the decreasing sequence and let them multiply with each other. The moving one becomes the non-moving one in the sequence.
The procedure says: Place the rank numbers, each becoming its own decreasing sequence, and reverse the sequence. Add the auxiliary values to form the divisor.
Multiply the 100 qian by the unadded values, each becoming its own dividend. Divide the dividends by the divisor to obtain the contribution of each.

The answer says: the Daifu contributes *a*(=1200/137) qian, the Bugeng contributes *b*(=1500/137) qian, the Zanniao contributes *c*(=2000/137) qian, the Shangzao contributes *d*(=3000/137) qian, and the Gongshi contributes *e*(=6000/137) qian.
"""

# 列置爵數，各自為衰
爵數 = [5, 4, 3, 2, 1]

# 返衰術：令相乘，動者為不動者衰
返衰 = [1, 1, 1, 1, 1]
for i in range(len(爵數)):
    for j in range(len(爵數)):
        if i != j:
            返衰[i] *= 爵數[j]

# 副并為法
法 = sum(返衰)

# 置百錢
總錢 = 100

# 以百錢乘未并者，各自為實
實 = [總錢 * x for x in 返衰]

# 實如法得一錢
a, b, c, d, e = [Fraction(x, 法) for x in 实] # 1200/137, 1500/137, 2000/137, 3000/137, 6000/137
"""
Code error: name '实' is not defined"""
