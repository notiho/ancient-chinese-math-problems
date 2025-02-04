"""
今有方堡壔方一丈六尺高一丈五尺問積幾何
術曰方自乘以高乘之即積尺
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a square fort with a side length of 1 zhang and 6 chi, and a height of 1 zhang and 5 chi.
Question: what is the volume in cubic chi?

The procedure says: Square the side length (multiply it by itself), then multiply it by the height. This gives the volume in cubic chi.

Answer: *a* cubic chi.
"""

# 方一丈六尺
方長 = 1 * 10 + 6  # Convert 1 zhang 6 chi to chi

# 高一丈五尺
高 = 1 * 10 + 5  # Convert 1 zhang 5 chi to chi

# 方自乘
方積 = 方長 * 方長

# 以高乘之
積 = 方積 * 高

# 即積尺
a = 積  # Volume in cubic chi#----- content ends here -----

"""
"""
