"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰：一千七萬四千五百八十五尺六寸。
秋程人功三百尺，問︰用徒幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a人 功。內少 b尺 。
"""

#----- content starts here -----
### 第一部分：計算渠積
# 上廣一丈八尺
上廣 = 1 * 10 + 8  # 將丈轉為尺

# 下廣三尺六寸
下廣 = 3 + Fraction(6, 10)  # 將寸轉為尺

# 深一丈八尺
深 = 1 * 10 + 8  # 將丈轉為尺

# 袤五萬一千八百二十四尺
袤 = 51824

# 并渠上下廣而半之
平均廣 = (上廣 + 下廣) / 2

# 以深乘之為法
法 = 平均廣 * 深

# 積幾何
積 = 法 * 袤

# 積結果
積結果 = Fraction(積, 1)  # 確保積為分數形式，便於後續計算

### 第二部分：計算用徒數
# 秋程人功三百尺
人功 = 300

# 用徒幾何
a = 積結果 // 人功  # 計算完整人數
b = 積結果 % 人功  # 計算剩餘尺數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 33582, Actual: 33581
Variable 'b' has wrong value. Expected: 72/5, Actual: 1428/5"""
