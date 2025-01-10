#今有穿地積一萬尺。問︰為堅、壤各幾何？
#術曰：穿地四，為壤五，為堅三，為墟四。以穿地求壤，五之；求堅，三之，皆四而一。以壤求穿，四之；求堅，三之，皆五而一。以堅求穿，四之；求壤，五之，皆三而一。
#荅曰：為堅 a尺 。為壤 b尺 。

"""
Suppose there is 10000 chi of dug out earth.
Question: how much solid earth and loose earth does it make respectively?

The procedure says: 4 [units of] dug out earth make 5 [units of] solid earth, and make 3 [units of] loose earth.
When seeking [the amount of] loose earth using dug out earth, multiply it by 5.
When seeking [the amount of] solid earth, multiply it by 3.
In each case, divide by 4.
When seeking dug out [earth] using loose earth, multiply it by 4.
When seeking solid earth, multiply it by 3.
In each case, divide by 5.
When seeking dug out [earth] using solid earth, multiply it by 4.
When seeking loose earth, multiply it by 5.
In each case, divide by 3.

Answer: it makes *a* chi of solid earth, and it makes *b* chi of loose earth.
"""

# 穿地積一萬尺
穿地 = 10000

# 穿地四，為壤五，為堅三
穿地率 = 4
壤率 = 5
堅率 = 3

# 以穿地求壤，五之
壤 = 5 * 穿地

# 求堅，三之
堅 = 3 * 穿地

# 皆四而一
a = 堅 / 4
b = 壤 / 4
