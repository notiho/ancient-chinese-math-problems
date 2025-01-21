"""
今有金方一寸重一斤有金方六寸問重幾何
術曰置金寸數再乗之即得
答曰 a斤
"""

"""
Suppose there is a cube of gold with a side length of 1 cun, weighing 1 jin.
Now there is a cube of gold with a side length of 6 cun.
Question: how much does it weigh?

The procedure says: Place the side length of the gold cube, square it, and then multiply by itself again (i.e., cube it). This gives the weight.

Answer: *a* jin.
"""

# 金方一寸重一斤
unit_weight = 1  # 1 cun cube weighs 1 jin

# 金方六寸
side_length = 6  # side length in cun

# 置金寸數再乘之即得
a = side_length ** 3 * unit_weight  # cube the side length and multiply by unit weight
"""
"""
