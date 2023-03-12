+++
title = "Bit Vector"
draft = false
math = true
+++

## 概要

簡潔データ構造の基本となるデータ構造  
長さ$N$ の $0/1$ 数列 $A = \lbrace A _ 0, A _ 1, \dots, A _ {N-1} \rbrace$ について、以下の操作を行う。

- rank: 先頭から $i$ 項目までの $1$ の個数を返す
- select: $i$ 番目の $1$ の場所を返す

時間計算量は以下の通り（理論的にはselectも定数時間にできるらしいが、正直机上の空論だと思っているので妥協）
- rank: $\mathrm{O}(1)$
- select: $\mathrm{O}(\log N)$

## I/F

### コンストラクタ

```cpp
BitVector bs(int N)
```

数列 $A$ を 長さ $N$ の 数列 $\lbrace 0, 0, \dots, 0\rbrace$ で初期化する

#### 計算量

$\mathrm{O}(N)$

### set

```cpp
void bs.set(int i)
```

$A _ i$ に $1$ を代入

#### 計算量

$\mathrm{O}(1)$

### reset

```cpp
void bs.reset(int i)
```

$A _ i$ に $0$ を代入

#### 計算量

$\mathrm{O}(1)$

### rank0

```cpp
int bs.rank0(int i)
```

$A _ 0, A _ 1, \dots, A _ {i-1}$ にある $0$ の個数

#### 計算量

$\mathrm{O}(1)$

但し、`set`, `reset` の呼出し後初めての実行は $\mathrm{O}(N)$ かかる

### rank1

```cpp
int bs.rank1(int i)
```

$A _ 0, A _ 1, \dots, A _ {i-1}$ にある $1$ の個数

#### 計算量

$\mathrm{O}(1)$

但し、`set`, `reset` の呼出し後初めての実行は $\mathrm{O}(N)$ かかる

### select0

```cpp
int bs.select0(int i)
```

$i$ 番目の $0$ の場所

#### 計算量

$\mathrm{O}(\log N)$

但し、`set`, `reset` の呼出し後初めての実行は $\mathrm{O}(N)$ かかる

### select1

```cpp
int bs.select1(int i)
```

$i$ 番目の $1$ の場所

#### 計算量

$\mathrm{O}(\log N)$

但し、`set`, `reset` の呼出し後初めての実行は $\mathrm{O}(N)$ かかる
