"""
今有立木繫索其末委地三尺引索卻行去本八尺而索盡問索長幾何
術曰以去本自乘令如委數而一所得加委地數而半之即索長
荅曰 a丈 
"""

#----- content starts here -----
"""
Suppose there is a standing tree with a rope tied to its top. The end of the rope touches the ground 3 chi away from the base of the tree.
Pulling the rope, one walks 8 chi away from the base of the tree until the rope is fully stretched.
Question: how long is the rope?

The procedure says: Multiply the distance from the base by itself, making it equal to the distance where the rope touches the ground, and divide by 1.
Add the number of chi where the rope touches the ground, and halve the result. This gives the length of the rope.

The answer says: *a* zhang.
"""

# 委地三尺
委地 = 3

# 去本八尺
去本 = 8

# 以去本自乘
去本平方 = 去本 * 去本

# 令如委數而一
所得 = Fraction(去本平方, 委地)

# 所得加委地數
加委地 = 所得 + 委地

# 而半之
索長 = Fraction(加委地, 2)

# Convert to 丈 (1 丈 = 10 尺)
a = Fraction(索長, 10)#----- content ends here -----

"""
"""
