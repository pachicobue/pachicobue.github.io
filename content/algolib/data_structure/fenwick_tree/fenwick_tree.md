---
title: Fenwick Tree
documentation_of: data_structure/fenwick_tree/fenwick_tree.hpp
---

## 概要

要素数 $N$ の 数列 $A = \lbrack A _ 0, A _ 1, \dots , A _ {N-1} \rbrack$ について、以下の操作が $\mathrm{O}(\log N)$ でできる。

- 一点加算: $A _ i \leftarrow A _ i + x$
- 接頭辞総和取得:  $A _ 0 + A _ 1 + \dots + A _ {i-1}$

## I/F

### コンストラクタ

```cpp
Fenwick<T> fenwick(const Vec<T>& vs)
```

数列 $A$ を `vs` の内容で初期化する

#### 計算量

$\mathrm{O}(N)$

### add

```cpp
void fenwick.add(int i, const T& x)
```

$A _ i$ に $x$ を加算

#### 計算量

$\mathrm{O}(\log N)$

### sum

```
(1) T fenwick.sum(int i)
(2) T fenwick.sum(int l, int r)
```

(1) $A _ 0 + A _ 1 + \dots + A _ {i-1}$ を取得
(2) $A _ l + A _ {l+1} + \dots + A _ {r-1}$ を取得

##### 計算量

$\mathrm{O}(\log N)$

### maxRight

```
int fenwick.maxRight<F>(F f)
```

以下を両方満たす $0 \le r \le N$ を1つ返す
- $f(A _ 0 + A _ 1 + \dots + A _ {r-1}) = true$
- $f(A _ 0 + A _ 1 + \dots + A _ {r}) = false$

#### 制約

f(0) = True

#### 計算量

$\mathrm{O}(\log N)$

### operator<<

```cpp
std::cout << fenwick << std::endl
```

$A = \lbrack A _ 0, A _ 1, \dots, A _ {N-1} \rbrack$ を出力
