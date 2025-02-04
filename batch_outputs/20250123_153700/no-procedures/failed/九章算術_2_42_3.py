"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

To solve this problem, we need to calculate the price per unit of silk based on the total cost and the total weight. The units of weight are given in **shi (石)**, **jun (鈞)**, **jin (斤)**, **liang (兩)**, and **zhu (銖)**. We will convert the total weight into a single unit (jin, for simplicity) and then calculate the price per unit weight.

---

### Problem Breakdown:
1. **Total money spent**: 13,970 (in qian, 錢).
2. **Total weight of silk**: 1 shi, 2 jun, 28 jin, 3 liang, 5 zhu.
   - 1 shi = 120 jin
   - 1 jun = 30 jin
   - 1 jin = 16 liang
   - 1 liang = 24 zhu
3. **Goal**: Calculate the price per **shi**, per **jun**, and per **jin** in qian (錢).

---

### Step 1: Convert Total Weight to Jin
We first convert the total weight into **jin**:
- 1 shi = 120 jin
- 2 jun = 2 × 30 = 60 jin
- 28 jin = 28 jin
- 3 liang = 3 ÷ 16 = 0.1875 jin
- 5 zhu = 5 ÷ (16 × 24) = 0.01302 jin

Total weight in jin:
\[
\text{Total weight} = 120 + 60 + 28 + 0.1875 + 0.01302 = 208.20052 \, \text{jin}
\]

---

### Step 2: Calculate Price Per Jin
The total cost is 13,970 qian. The price per jin is:
\[
\text{Price per jin} = \frac{\text{Total cost}}{\text{Total weight}} = \frac{13,970}{208.20052}
\]

Simplify:
\[
\text{Price per jin} \approx 67.1 \, \text{qian per jin}
\]

---

### Step 3: Calculate Prices for Shi, Jun, and Jin
- **Price per shi**: 1 shi = 120 jin
  \[
  \text{Price per shi} = 120 \times 67.1 = 8,052 \, \text{qian}
  \]

- **Price per jun**: 1 jun = 30 jin
  \[
  \text{Price per jun} = 30 \times 67.1 = 2,013 \, \text{qian}
  \]

- **Price per jin**: Already calculated as:
  \[
  \text{Price per jin} \approx 67.1 \, \text{qian}
  \]

---

### Final Answer:
- **a** (price per shi): 8,052 qian
- **b** (price per jin): 67.1 qian
- **c** (price per jun): 2,013 qian
- **d** (price per jin): 67.1 qian


"""
Code error: invalid character '×' (U+00D7) (<string>, line 20)"""
