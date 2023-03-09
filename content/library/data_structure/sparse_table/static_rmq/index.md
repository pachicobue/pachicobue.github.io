+++
title = "静的数列のRMQ"
draft = false
+++

## 概要

全順序集合 $(T, <)$ が決まっている。  
要素数 $N$ の 数列 $A = \lbrack A _ 0, A _ 1, \dots , A _ {N-1}\rbrack$ について、以下の操作が $\mathrm{O}(1)$ でできる。

- 範囲min取得: $A _ l \dots A _ {r-1}$ の最小値

前計算も $\mathrm{O}(N)$ でできる点で、 [DisjointSparseTable](https://pachicobue.github.io/algolib/src/data_structure/ds_table.hpp) を使うより有利

### 参考

このデータ構造は https://noshi91.hatenablog.com/entry/2018/08/16/125415 で知りました。

## I/F

### コンストラクタ

```cpp
StaticRMQ<TotalOrd> rmq(const Vec<T>& vs)
```

数列 $A$ を `vs` の内容で初期化する

テンプレート引数`TotalOrd`は以下のようなフィールドを持つクラス

```cpp
struct Ord
{
    using T = u32;
    bool operator()(const T& x1, const T& x2) const
    {
        return x1 < x2;
    }
};
```

- `T`: 型
- `operator()(T x1, T x2)`: $x _ 1 < x _ 2$ 

#### 計算量

$\mathrm{O}(N)$

### fold

```cpp
T rmq.fold(int l, int r)
```

$A _ l \ast \dots \ast A _ {r-1}$ の取得

#### 計算量

$\mathrm{O}(1)$
