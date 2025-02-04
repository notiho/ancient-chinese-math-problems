"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
求龍尾堤廣、袤、高，術曰：以程功乘總人，為堤積。又六因之，為虛積。以少高乘少袤，為隅冪。以少上廣乘之，為鱉隅積。以減虛積，余，三約之，所得為實。並少高、袤，以少上廣乘之，為鱉從橫廉冪。三而一，加隅冪，為方法。又三除少上廣，以少袤、少高加之，為廉法，從。開立方除之，得下廣。加差，即高、廣、袤。求逐縣均給積尺受廣、袤，術曰：以程功乘當縣人，當積尺。各六因積尺。又乘袤冪。廣差乘高，為法。除之，為實。又三因末廣，以袤乘之，廣差而一，為都廉，從。開立方除之，即甲袤。以本高乘之，以本袤除之，即甲高。又以廣差乘甲袤，以本袤除之，所得加末廣，即甲上廣。其甲上廣即乙末廣，其甲高即垣高。求實與都廉，如前。又並甲上下廣，三之，乘甲高，又乘袤冪，以法除之，得垣方，從。開立方除之，即乙袤。余放此。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical method into Python code. The solution involves calculating the dimensions of the 龙尾堤 (Dragon Tail Embankment) and the contributions of the three counties (甲, 乙, 丙). The calculations involve using fractions to ensure precision.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
差 = Fraction(6)  # Difference between upper and lower widths (6 尺)
少高 = Fraction(12)  # Lower height (1 丈 2 尺 = 12 尺)
少袤 = Fraction(48)  # Lower length (4 丈 8 尺 = 48 尺)
甲人 = 2375  # People from 甲县
乙人 = 2378  # People from 乙县
丙人 = 5247  # People from 丙县
程功 = Fraction(19, 10)  # Work per person per day (1 尺 9 寸 8 分 = 1.98 尺)

# Total people
總人 = 甲人 + 乙人 + 丙人

# Step 1: Calculate the total embankment volume
堤積 = 程功 * 總人  # Total work volume
虛積 = 堤積 * 6  #虚积 = 堤积 × 6

# Step 2: Calculate 隅冪 and 鱉隅積
隅冪 = 少高 * 少袤  # 隅冪 = 少高 × 少袤
鱉隅積 = 隅冪 * 少高  # 鱉隅積 = 隅冪 × 少上廣

# Step 3: Calculate the real volume (實)
實 = (虛積 - 鱉隅積) / 3

# Step 4: Calculate 鱉從橫廉冪 and 方法
鱉從橫廉冪 = (少高 + 少袤) * 少高 * 少袤 / 3
方法 = 鱉從橫廉冪 + 隅冪

# Step 5: Calculate 廉法 and 下廣
廉法 = (少袤 + 少高 + 少袤) / 3
下廣 = (實 / 方法) ** Fraction#----- content ends here -----


"""

"""


"""
Code error: unsupported operand type(s) for ** or pow(): 'float' and 'ABCMeta'"""
