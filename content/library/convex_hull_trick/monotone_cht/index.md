+++
title = "単調性のある Convex Hull Trick"
draft = false
+++

## 概要

直線 $l _ i(x): y = a _ i x + b _ i$ の集合 $\mathcal{L}$ について以下の操作を ならし$\mathrm{O}(1)$ で行う。

- 直線追加: $\mathcal{L} \leftarrow \mathcal{L} \cup \lbrace l:y=ax+b \rbrace$
- 最小値取得: $\mathrm{argmin}_{l \in \mathcal{L}}\ l(x)$

但し、クエリについて以下の制約が満たされているとする。  
- 1つ目のクエリでの 直線の傾き $a$ は広義単調減少
- 2つ目のクエリでの 座標 $x$ は広義単調増加

## I/F

### コンストラクタ

```cpp
MonotonicCHT<T> cht()
```

- `T`: $x$ 座標, 傾き, $y$切片の型

#### 計算量

$\mathrm{O}(1)$

### addLine

```cpp
void cht.addLine(T a, T b)
```

$\mathcal{L}$ に直線 $l: y=ax+b$ を追加

#### 計算量

$\mathrm{O}(1)$

### minLine

```cpp
L cht.minLine(const T x)
```

$\mathrm{argmin}_{l \in \mathcal{L}}\ l(x)$ を取得

- 返り値は (線分の傾き, 線分の$y$切片)

#### 計算量

ならし $\mathrm{O}(1)$

