+++
title = "Li Chao Tree"
draft = false
math = true
+++

## 概要

線分 $s _ i(x): y = a _ i x + b _ i (l _ i \le x \lt r _ i)$ の集合 $\mathcal{S}$ について以下の操作を $\mathrm{O}(\log N)$ で行う。

- 線分追加: $\mathcal{S} \leftarrow \mathcal{S} \cup \lbrace s:y=ax+b (l \le x \le r) \rbrace$
- 最小値取得: $\mathrm{argmin}_{l \in \mathcal{S}}\ l(x)$

## I/F

### コンストラクタ

```cpp
LiChaoTree<T, V> cht(T xmin, T xsup)
```

- `T`: $x$ 座標, 傾き, $y$ 切片の型
- `xmin`,`xsup`: クエリ $x$ 座標の上限下限($x _ {min} \le x \lt x _ {sup}$ を満たす)

以下 $X = x _ {sup} - x _ {min}$

#### 計算量

$\mathrm{O}(1)$

### addLine

```cpp
void cht.addLine(T a, T b)
```

$\mathcal{S}$ に直線 $l: y=ax+b$ を追加

#### 計算量

$\mathrm{O}(\log X)$

### addSeg

```cpp
void cht.addSeg(T a, T b, T xl, T xr)
```

$\mathcal{S}$ に線分 $s: y=ax+b (x _ l \le x \lt x _ r)$ を追加

#### 計算量

$\mathrm{O}(\log^2 X)$

### minLine

```cpp
Pair<bool,L> cht.minLine(T x)
```

$\mathrm{argmin}_{s \in \mathcal{S}}\ s(x)$ を取得  

- 返り値の`first`は $x$ 上に線分があるかどうか
- 返り値の`second`は (線分の傾き, 線分の$y$切片) のペア

#### 計算量

$\mathrm{O}(\log X)$
