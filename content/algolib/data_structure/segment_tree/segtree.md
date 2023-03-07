---
title: Segment Tree
documentation_of: data_structure/segment_tree/segtree.hpp
---

## 概要

値モノイド $(T, \ast, e)$ が決まっている。  
要素数 $N$ の 数列 $A = \lbrack A _ 0, A _ 1, \dots , A _ {N-1}\rbrack$ について、以下の操作が $\mathrm{O}(\log N)$ でできる。

- 範囲総積取得: $A _ l \ast \dots \ast A _ {r-1}$
- 一点更新: $A _ i \leftarrow x$


## I/F

### コンストラクタ

```cpp
SegTree<MergeMonoid> seg(const Vec<T>& vs)
```

数列 $A$ を `vs` の内容で初期化する

テンプレート引数`MergeMonoid`は以下のようなフィールドを持つクラス

```cpp
struct MergeMonoid
{
    using T = int;
    T operator()(const T& x1, const T& x2) const { return std::min(x1, x2); }
    static constexpr T e() { return INF<T>; }
};
```

- `T`: 作用素型
- `operator()(T x1, T x2)`: $x _ 1 \ast x _ 2$ 
- `e()`: 単位元

#### 計算量

$\mathrm{O}(N)$

### get

```cpp
T seg.get(int i)
```

$A _ i$ の取得

#### 計算量

$\mathrm{O}(1)$

### set

```cpp
void seg.set(int i, const T& x)
```

$A _ i$ に $x$ を代入する

#### 計算量

$\mathrm{O}(\log N)$

### fold

```cpp
T seg.fold(int l, int r)
```

$A _ l \ast \dots \ast A _ {r-1}$ の取得

#### 計算量

$\mathrm{O}(\log N)$

### operator<<

```cpp
std::cout << seg << std::endl
```
