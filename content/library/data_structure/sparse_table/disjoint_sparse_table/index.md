+++
title = "Disjoint Sparse Table"
draft = false
+++

## 概要

半群 $(T, \ast)$ 上の要素数 $N$ の 数列 $A = \lbrack A _ 0, A _ 1, \dots , A _ {N-1}\rbrack$ について、  
以下の操作が $\mathrm{O}(1)$ でできる。

- 範囲総積取得: $A _ l \ast \dots \ast A _ {r-1}$

前計算は $\mathrm{O}(N\log N)$ 必要

## I/F

### コンストラクタ

```cpp
DSTable<SemiGroup> dst(const Vec<T>& vs)
```

数列 $A$ を `vs` の内容で初期化する

#### 制約

テンプレート引数`SemiGroup`は以下のようなフィールドを持つクラス

- `T`:型
- `operator()(T x1, T x2)`: $x _ 1 \ast x _ 2$
  
```cpp
struct SemiGroup
{
    using T = int;
    T operator()(const T& x1, const T& x2) const { 
        return std::min(x1, x2); 
    }
};
```

#### 計算量

$\mathrm{O}(N\log N)$

### add

```cpp
void dst.add(int i, const T& x)
```

$A _ i$ に $x$ を加算

#### 計算量

$\mathrm{O}(\log N)$

### fold

```cpp
T dst.fold(int l, int r)
```

$A _ l \ast \dots \ast A _ {r-1}$ を取得

#### 計算量

$\mathrm{O}(1)$
