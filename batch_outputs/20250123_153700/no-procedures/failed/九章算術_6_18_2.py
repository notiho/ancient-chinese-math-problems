"""
今有竹九節，下三節容四升，上四節容三升。問︰中間二節欲均容各多少？
荅曰：下初， a升 ，次 b升 ，次 c升 ，次 d升 ，次 e升 ，次 f升 ，次 g升 ，次 h升 ，次 i升 。
"""

"""
Suppose there is a bamboo with 9 nodes. The bottom 3 nodes can hold 4 sheng each, and the top 4 nodes can hold 3 sheng each.
Question: how much should the middle 2 nodes hold to make the distribution even?

Answer: The bottom nodes hold *a*, *b*, *c* sheng, the middle nodes hold *d*, *e* sheng, and the top nodes hold *f*, *g*, *h*, *i* sheng.
"""

# Bottom 3 nodes
bottom_nodes = 3
bottom_capacity = 4

# Top 4 nodes
top_nodes = 4
top_capacity = 3

# Total nodes
total_nodes = 9

# Middle 2 nodes
middle_nodes = 2

# Total capacity of the bamboo
total_capacity = (bottom_nodes * bottom_capacity) + (top_nodes * top_capacity)

# Remaining capacity for the middle nodes
middle_capacity = total_capacity - (bottom_nodes * bottom_capacity) - (top_nodes * top_capacity)

# Capacity per middle node
middle_node_capacity = Fraction(middle_capacity, middle_nodes)

# Assign capacities to each node
a = bottom_capacity
b = bottom_capacity
c = bottom_capacity
d = middle_node_capacity
e = middle_node_capacity
f = top_capacity
g = top_capacity
h = top_capacity
i = top_capacity

# Final values
a, b, c, d, e, f, g, h, i
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
