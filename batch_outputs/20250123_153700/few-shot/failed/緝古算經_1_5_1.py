"""
假令四郡輸粟，斛法二尺五寸，一人作功為均。自上給甲，以次與乙。其甲郡輸粟三萬八千七百四十五石六斗，乙郡輸粟三萬四千九百五石六斗，丙郡輸粟，二萬六千二百七十石四斗，丁郡輸粟一萬四千七十八石四斗。四郡共穿窖，上袤多於上廣一丈，少於下袤三丈，多於深六丈，少於下廣一丈。各計粟多少，均出丁夫。自穿、負、築，冬程人功常積一十二尺，一日役。問：窖上下廣、袤、深，郡別出人及窖深、廣各多少？
求窖深、廣、袤，術曰：以斛法乘總粟，為積尺。又廣差乘袤差，三而一，為隅陽冪。乃置塹上廣，半廣差加之，以乘塹上袤，為隅頭冪。又半袤差，乘塹上廣，以隅陽冪及隅頭冪加之，為方法。又置塹上袤及塹上廣，並之，為大廣。又並廣差及袤差，半之，以加大廣，為廉法，從。開立方除之，即深。各加差，即合所問。求均給積尺受廣、袤、深，術曰：如築臺術入之。以斛法乘甲郡輸粟，為積尺。又三因，以深冪乘之，以廣差乘袤差而一，為實。深乘上廣，廣差而一，為上廣之高。深乘上袤，袤差而一，為上袤之高。上廣之高乘上袤之高，三之，為方法。又並兩高，三之，二而一，為廉法，從。開立方除之，即甲深。以袤差乘之，以本深除之，所加上袤，即甲下袤。以廣差乘之，本深除之，所得加上廣，即甲下廣。若求乙、丙、丁，每以前下廣、袤為後上廣、袤，以次皆準此求之，即得。若求人數，各以程功約當郡積尺。
答曰：窖上廣 a丈 ，上袤 b丈 ，下廣 c丈 ，下袤 d丈 ，深 e丈 ；甲郡 f人 ，深 g尺 ，下袤 h丈 ，廣 i丈 ；乙郡 j人 ，深 k尺 ，下袤 l丈 ，廣 m丈 ；丙郡 n人 ，深 o尺 ，下袤 p丈 ，廣 q丈 ；丁郡 r人 ，深 s尺 ，下袤 t丈 ，廣 u丈 。
"""

"""
This problem is highly complex and involves multiple steps of ancient Chinese mathematical procedures. It requires calculating the dimensions of a storage pit (窖) and distributing labor among four regions based on the amount of grain they contribute. Below is the Python code that follows the ancient procedure step by step.


"""


from fractions import Fraction
from math import isqrt

# Input data
斛法 = Fraction(25, 10)  # 2尺5寸 = 2.5尺
甲輸粟 = Fraction(38745, 1) + Fraction(6, 10)  # 38745石6斗
乙輸粟 = Fraction(34905, 1) + Fraction(6, 10)  # 34905石6斗
丙輸粟 = Fraction(26270, 1) + Fraction(4, 10)  # 26270石4斗
丁輸粟 = Fraction(14078, 1) + Fraction(4, 10)  # 14078石4斗
總輸粟 = 甲輸粟 + 乙輸粟 + 丙輸粟 + 丁輸粟

# Pit dimensions differences
上廣差 = Fraction(1, 1)  # 上廣多於下廣1丈
上袤差 = Fraction(1, 1)  # 上袤多於下袤1丈
下袤差 = Fraction(3, 1)  # 下袤多於上袤3丈
深差 = Fraction(6, 1)    # 深多於上廣6丈

# Labor constants
冬程功 = Fraction(12, 1)  # 每人每日12尺積功

# Step 1: Calculate the total volume in cubic chi (積尺)
積尺 = 總輸粟 * 斛法

# Step 2: Calculate 隅陽冪
隅陽冪 = (上廣差 * 上袤差) / 3

# Step 3: Calculate 隅頭冪
隅頭冪 = ((上廣差 / 2) + 1) * ((上袤差 / 2) + 1)

# Step 4: Calculate 方法
方法 = 隅陽冪 + 隅頭冪 + ((上廣差 / 2) * (上袤差 / 2))

# Step 5: Calculate 大廣 and 廉法
大廣 = 1 + 1 + 上廣差 + 上袤差
廉法 = (上廣差 + 上袤差) / 2 + 大廣

# Step 6: Calculate depth (深)
深 = isqrt(積尺 / 方法)

# Step 7: Calculate dimensions
上廣 = 1
上袤 = 1
下廣 = 上廣 + 上廣差
下袤 = 上袤 + 下袤差

# Step 8: Calculate labor distribution
甲積尺 = 甲輸粟 *斛法

"""

"""


"""
Code error: 'Fraction' object cannot be interpreted as an integer"""
