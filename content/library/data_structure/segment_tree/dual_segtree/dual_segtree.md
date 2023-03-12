+++
title = "Dual Segment Tree"
draft = false
math = true
+++

## 概要

作用素モノイド $(F, \circ, \mathrm{id})$ が決まっている。  
要素数 $N$ の 作用素列 $G = \lbrack G _ 0, G _ 1, \dots, G _ {N-1}\rbrack$ について、以下の操作が $\mathrm{O}(\log N)$ でできる。

- 範囲作用: $G _ i \leftarrow f \circ G _ i \quad (i \in \lbrack l, r) )$
- 一点取得: $G _ i$
- 一点更新: $G _ i \leftarrow f$


## I/F

### コンストラクタ

```cpp
DualSeg<OpMonoid> seg(const Vec<F>& vs)
```

作用素列 $G$ を `vs` の内容で初期化する

#### 制約

テンプレート引数`OpMonoid`は以下のようなフィールドを持つクラス

- `F`:型
- `operator()(F f1, F f2)`: $f _ 1 \circ f _ 2$
- `id()`: 単位元 $\mathrm{id}$

```cpp
struct OpMonoid
{
    using F = int;
    F operator()(const F& f1, const F& f2) const { 
        return f1 + f2;
    }
    static constexpr F id() { return F{0}; }
};
```

#### 計算量

- $\mathrm{O}(N)$

### get

```cpp
F seg.get(int i)
```

$G _ i$ の取得

#### 計算量

- $\mathrm{O}(\log N)$

### set

```cpp
void seg.set(int i, const F& f)
```

$G _ i \leftarrow f$ を行う

#### 計算量

- $\mathrm{O}(\log N)$

### act

```cpp
void seg.act(int l, int r, const F& f)
```

$G _ i \leftarrow f \circ G _ i \quad (i \in \lbrack l, r) )$ を行う

#### 計算量

- $\mathrm{O}(\log N)$

### operator<<

```cpp
std::cout << seg << std::endl
```

$G = \lbrack G _ 0, G _ 1, \dots, G _ {N-1} \rbrack$ を出力
