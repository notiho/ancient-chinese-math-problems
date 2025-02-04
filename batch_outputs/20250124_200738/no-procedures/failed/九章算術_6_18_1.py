"""
今有竹九節，下三節容四升，上四節容三升。問︰中間二節欲均容各多少？
荅曰：下初， a升 ，次 b升 ，次 c升 ，次 d升 ，次 e升 ，次 f升 ，次 g升 ，次 h升 ，次 i升 。
"""

#----- content starts here -----
"""
Suppose there is a bamboo with 9 nodes. The bottom 3 nodes can hold 4 sheng each, and the top 4 nodes can hold 3 sheng each.
Question: how much should the middle 2 nodes hold if the total volume is evenly distributed?

Answer: The bottom 3 nodes hold *a*, *b*, and *c* sheng, the middle 2 nodes hold *d* and *e* sheng, and the top 4 nodes hold *f*, *g*, *h*, and *i* sheng.
"""

# Total nodes
total_nodes = 9

# Bottom 3 nodes
bottom_nodes = 3
bottom_volume = 4  # Each bottom node holds 4 sheng

# Top 4 nodes
top_nodes = 4
top_volume = 3  # Each top node holds 3 sheng

# Middle 2 nodes
middle_nodes = 2

# Total volume
total_volume = (bottom_nodes * bottom_volume) + (top_nodes * top_volume)

# Remaining volume for middle nodes
remaining_volume = total_volume - (bottom_nodes * bottom_volume) - (top_nodes * top_volume)

# Distribute the remaining volume evenly across the middle nodes
middle_volume = Fraction(remaining_volume, middle_nodes)

# Assign volumes to each node
a = b = c = bottom_volume  # Bottom 3 nodes
d = e = middle_volume  # Middle 2 nodes
f = g = h = i = top_volume  # Top 4 nodes

# Results
a, b, c, d, e, f, g, h, i#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 95/66, Actual: 4
Variable 'b' has wrong value. Expected: 4/3, Actual: 4
Variable 'c' has wrong value. Expected: 27/22, Actual: 4
Variable 'd' has wrong value. Expected: 37/33, Actual: 0
Variable 'e' has wrong value. Expected: 67/66, Actual: 0
Variable 'f' has wrong value. Expected: 10/11, Actual: 3
Variable 'g' has wrong value. Expected: 53/66, Actual: 3
Variable 'h' has wrong value. Expected: 23/33, Actual: 3
Variable 'i' has wrong value. Expected: 13/22, Actual: 3"""
