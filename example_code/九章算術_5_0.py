#今有穿地積一萬尺問爲堅壤各幾何
#術曰穿地四爲壤五爲堅三爲墟四以穿地求壤五之求堅三之皆四而一以壤求穿四之求堅三之皆五而一以堅求穿四之求壤五之皆三而一
#荅曰爲堅 a尺 爲壤 b尺

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

# 穿地四爲壤五爲堅三
穿地率 = 4
壤率 = 5
堅率 = 3

# 以穿地求壤五之
壤 = 5 * 穿地

# 求堅三之
堅 = 3 * 穿地

# 皆四而一
a = 堅 / 4
b = 壤 / 4
