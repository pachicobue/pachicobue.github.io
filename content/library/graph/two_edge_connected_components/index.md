+++
title = "二重辺連結成分分解"
draft = false
+++

## 概要

$V$頂点$E$辺 の無向グラフを $\mathrm{O}(V+E)$ 時間で二重辺連結成分に分解する。

## I/F

### コンストラクタ

```cpp
TwoEdgeConnectedComponent tecc(Graph<T> g)
```

グラフ $g$ を二重辺連結成分分解する。

#### 計算量

$\mathrm{O}(V+E)$

### operator[]

```cpp
int tecc[i]
```

頂点 $i$ の属する二重辺連結成分番号を返す。  
頂点 $i,j$ が同じ二重辺連結成分に属する $\Leftrightarrow$ `bcc[i] == bcc[j]`

#### 計算量

$\mathrm{O}(1)$

### cnum

```cpp
int tecc.cnum()
```

二重辺連結成分数

#### 計算量

$\mathrm{O}(1)$

### groups

```cpp
Vec<Vec<int>> tecc.groups()
```

二重辺連結成分のリスト

#### 計算量

$\mathrm{O}(V)$
