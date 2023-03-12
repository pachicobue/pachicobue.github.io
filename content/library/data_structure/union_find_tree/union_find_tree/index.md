+++
title = "Union Find Tree"
draft = false
math = true
showToc = true
+++

## 概要

$N$ 頂点の無向グラフ $G$ に対して、以下の操作がならし $\mathrm{O}(\alpha(N))$ でできる。

- 辺追加
- 連結性判定

## I/F

### コンストラクタ

```cpp
DSU dsu(int N)
```

グラフ $G$ を $N$ 頂点 $0$ 辺の無向グラフで初期化する

#### 計算量

$\mathrm{O}(N)$

### leader

```cpp
int seg.leader(int v)
```

$v$ が属する連結成分の代表元

#### 計算量

ならし $\mathrm{O}(\alpha(N))$

### merge

```cpp
bool seg.merge(int u, int v)
```

辺 $(u, v)$ を追加する。  
返り値は異なる連結成分を結んだかどうか

#### 計算量

ならし $\mathrm{O}(\alpha(N))$

### groups

```cpp
Vec<Vec<int>> seg.groups()
```

連結成分のリスト

#### 計算量

$\mathrm{O}(N)$
