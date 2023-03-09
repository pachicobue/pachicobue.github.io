+++
title = "Sliding Window Aggregation(Deque)"
draft = false
+++

## 概要

半群 $(T, \ast)$ 上の数列 $A = \lbrack A _ 0, A _ 1, \dots , A _ {n-1}\rbrack$ について、  
以下の操作が $\mathrm{O}(1)$ でできる。

- 総積取得: $A _ 0 \ast \dots \ast A _ {n-1}$
- 先頭挿入: $A \leftarrow \lbrack v, A _ 0, \dots, A _ {n-1} \rbrack$
- 末尾挿入: $A \leftarrow \lbrack A _ 0, \dots, A _ {n-1}, v \rbrack$
- 先頭削除: $A \leftarrow \lbrack A _ 1, \dots, A _ {n-1} \rbrack$
- 末尾削除: $A \leftarrow \lbrack A _ 0, \dots, A _ {n-2} \rbrack$

## I/F

### コンストラクタ

```cpp
SWAG<SemiGroup> swag()
```

数列 $A$ を空数列で初期化する

テンプレート引数`SemiGroup`は以下のようなフィールドを持つクラス

- `T`:型
- `operator()(T x1, T x2)`: $x_1 \ast x_2$

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

$\mathrm{O}(1)$

### foldAll

```cpp
T rmq.foldAll()
```

$A _ 0 \ast \dots \ast A _ {N-1}$ の取得

#### 計算量

$\mathrm{O}(1)$

### pushBack

```cpp
void swag.pushBack(const T& v)
```

数列$A$ の末尾に $v$ を挿入する

#### 計算量

$\mathrm{O}(1)$

### pushFront

```cpp
void swag.pushFront(const T& v)
```

数列$A$ の先頭に $v$ を挿入する

#### 計算量

$\mathrm{O}(1)$

### popBack

```cpp
void swag.pushBack(const T& v)
```

数列$A$ の末尾を削除する

#### 計算量

ならし $\mathrm{O}(1)$

### popFront

```cpp
void swag.pushFront(const T& v)
```

数列$A$ の先頭を削除する

#### 計算量

ならし $\mathrm{O}(1)$
