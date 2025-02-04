"""
假令四郡輸粟，斛法二尺五寸，一人作功為均。自上給甲，以次與乙。其甲郡輸粟三萬八千七百四十五石六斗，乙郡輸粟三萬四千九百五石六斗，丙郡輸粟，二萬六千二百七十石四斗，丁郡輸粟一萬四千七十八石四斗。四郡共穿窖，上袤多於上廣一丈，少於下袤三丈，多於深六丈，少於下廣一丈。各計粟多少，均出丁夫。自穿、負、築，冬程人功常積一十二尺，一日役。問：窖上下廣、袤、深，郡別出人及窖深、廣各多少？
求窖深、廣、袤，術曰：以斛法乘總粟，為積尺。又廣差乘袤差，三而一，為隅陽冪。乃置塹上廣，半廣差加之，以乘塹上袤，為隅頭冪。又半袤差，乘塹上廣，以隅陽冪及隅頭冪加之，為方法。又置塹上袤及塹上廣，並之，為大廣。又並廣差及袤差，半之，以加大廣，為廉法，從。開立方除之，即深。各加差，即合所問。求均給積尺受廣、袤、深，術曰：如築臺術入之。以斛法乘甲郡輸粟，為積尺。又三因，以深冪乘之，以廣差乘袤差而一，為實。深乘上廣，廣差而一，為上廣之高。深乘上袤，袤差而一，為上袤之高。上廣之高乘上袤之高，三之，為方法。又並兩高，三之，二而一，為廉法，從。開立方除之，即甲深。以袤差乘之，以本深除之，所加上袤，即甲下袤。以廣差乘之，本深除之，所得加上廣，即甲下廣。若求乙、丙、丁，每以前下廣、袤為後上廣、袤，以次皆準此求之，即得。若求人數，各以程功約當郡積尺。
答曰：窖上廣 a丈 ，上袤 b丈 ，下廣 c丈 ，下袤 d丈 ，深 e丈 ；甲郡 f人 ，深 g尺 ，下袤 h丈 ，廣 i丈 ；乙郡 j人 ，深 k尺 ，下袤 l丈 ，廣 m丈 ；丙郡 n人 ，深 o尺 ，下袤 p丈 ，廣 q丈 ；丁郡 r人 ，深 s尺 ，下袤 t丈 ，廣 u丈 。
"""

"""
This problem is highly complex and involves multiple steps of ancient Chinese mathematical procedures. I'll break it down step by step and encode the solution in Python. Let's proceed systematically.

---

### Step 1: Define the input data



---

### Step 2: Calculate the total 粟積尺 (volume in cubic 尺)



---

### Step 3: Calculate 窖 dimensions (深, 上廣, 上袤, 下廣, 下袤)



---

### Step 4: Calculate 郡別 dimensions and people required



---

### Step 5: Final output


"""


from fractions import Fraction

# Input data
斛法 = Fraction(25, 10)  # 2尺5寸 = 2.5尺
甲輸粟 = 38745 + Fraction(6, 10)  # 38745石6斗
乙輸粟 = 34905 + Fraction(6, 10)  # 34905石6斗
丙輸粟 = 26270 + Fraction(4, 10)  # 26270石4斗
丁輸粟 = 14078 + Fraction(4, 10)  # 14078石4斗

# Differences in dimensions
上袤差 = 1  # 多於上廣1丈
下袤差 = 3  # 少於下袤3丈
深差 = 6    # 多於深6丈
下廣差 = 1  # 少於下廣1丈

# Winter workload
冬程功 = 12  # 每人每日12尺

# Total 粟積尺
總粟 = 甲輸粟 + 乙輸粟 + 丙輸粟 + 丁輸粟
總積尺 = 總粟 * 斛法

# 隅陽冪
隅陽冪 = (上袤差 * 下袤差) / 3

# 隅頭冪
隅頭冪 = ((下廣差 / 2) + 1) * ((上袤差 / 2) + 1)

# 方法
方法 = 隅陽冪 + 隅頭冪

# 大廣
大廣 = 1 + 1  # 上廣 + 上袤

# 廉法
廉法 = (上袤差 + 下袤差) / 2 + 大廣

# 深
深 = (總積尺 / 方法) ** Fraction(1, 3)

# 上廣, 上袤, 下廣, 下袤
上廣 = 1
上袤 = 1
下廣 = 上廣 + 下廣差
下袤 = 上袤 + 下袤差

# 郡別積尺
甲積尺 = 甲輸粟 * 斛法
乙積尺 = 乙輸粟 * 斛法
丙積尺 = 丙輸粟 * 斛法
丁積尺 = 丁輸粟 * 斛法

# 郡別深, 廣, 袤
甲深 = (甲積尺 / 方法) ** Fraction(1, 3)
甲下袤 = 上袤 + (下袤差 * 甲深 / 深)
甲下廣 = 上廣 + (下廣差 * 甲深 / 深)

乙深 = (乙積尺 / 方法) ** Fraction(1, 3)
乙下袤 = 甲下袤 + (下袤差 * 乙深 / 深)
乙下廣 = 甲下廣 + (下廣差 * 乙深 / 深)

丙深 = (丙積尺 / 方法) ** Fraction(1, 3)
丙下袤 = 乙下袤 + (下袤差 * 丙深 / 深)
丙下廣 = 乙下廣 + (下廣差 * 丙深 / 深)

丁深 = (丁積尺 / 方法) ** Fraction(1, 3)
丁下袤 = 丙下袤 + (下袤差 * 丁深 / 深)
丁下廣 = 丙下廣 + (下廣差 * 丁深 / 深)

# 郡別人數
甲人 = 甲積尺 / 冬程功
乙人 = 乙積尺 / 冬程功
丙人 = 丙積尺 / 冬程功
丁人 = 丁積尺 / 冬程功

# 窖 dimensions
a = 上廣
b = 上袤
c = 下廣
d = 下袤
e = 深

# 郡別 results
f = 甲人
g = 甲深
h = 甲下袤
i = 甲下廣

j = 乙人
k = 乙深
l =乙下袤
m = 乙下廣

n = 丙人
o = 丙深
p = 丙下袤
q = 丙下廣

r = 丁人
s = 丁深
t = 丁下袤
u = 丁下廣


"""


---

### Final Answer:

窖上廣 `a` 丈，窖上袤 `b` 丈，窖下廣 `c` 丈，窖下袤 `d` 丈，窖深 `e` 丈；  
甲郡 `f` 人，深 `g` 尺，下袤 `h` 丈，廣 `i` 丈；  
乙郡 `j` 人，深 `k` 尺，下袤 `l` 丈，廣 `m` 丈；  
丙郡 `n` 人，深 `o` 尺，下袤 `p` 丈，廣 `q` 丈；  
丁郡 `r` 人，深 `s` 尺，下袤 `t` 丈，廣 `u` 丈。
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 1
Variable 'b' has wrong value. Expected: 9, Actual: 1
Variable 'c' has wrong value. Expected: 10, Actual: 2
Variable 'd' has wrong value. Expected: 12, Actual: 4
Variable 'e' has wrong value. Expected: 3, Actual: 44.42770024521407
Variable 'g' has wrong value. Expected: 12, Actual: 31.00461523110512
Variable 'h' has wrong value. Expected: 51/5, Actual: 3.093600280454201
Variable 'i' has wrong value. Expected: 44/5, Actual: 1.6978667601514004
Variable 'k' has wrong value. Expected: 9, Actual: 29.944512820317456
Variable 'l' has wrong value. Expected: 111/10, Actual: 5.1156166793478075
Variable 'm' has wrong value. Expected: 47/5, Actual: 2.3718722264492693
Variable 'o' has wrong value. Expected: 6, Actual: 27.237951635795945
Variable 'p' has wrong value. Expected: 117/10, Actual: 6.95487134381112
Variable 'q' has wrong value. Expected: 49/5, Actual: 2.9849571146037066
Variable 's' has wrong value. Expected: 3, Actual: 22.12432261471568
Variable 't' has wrong value. Expected: 12, Actual: 8.448825959463255
Variable 'u' has wrong value. Expected: 10, Actual: 3.4829419864877513"""
