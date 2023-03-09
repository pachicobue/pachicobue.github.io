+++
title = "Scanner (入力補助クラス)"
draft = false
+++

## 概要

入力を行うクラス  
入力した値を返すので `const` で受け取ったりできるのが利点。  
複数の入力を `tuple` にして返したり、vector配列で返したりできる。

## I/F

### コンストラクタ

```cpp
Scanner scanner(Istream& is = std::cin)
```

引数には入力元(デフォルトは標準入力)を与える。  
内部で `tie(nullptr)` と `sync_with_stdio(false)` を流す(これはやりすぎかも)。

グローバルに標準出力を使う Scanner を定義している。大体これを使えばよい。
```cpp
Scanner in;
```

### val

```cpp
(1) T scanner.val()
(2) T scanner.val(T offset)
```

(1) 型 `T` の入力を返す。  
(2) (1)の値から `offset` を引いた値を返す。

基本的に `T` は明示的に指定しなければならない。  
以下のように使う。

```cpp
const auto N = in.val<int>(); // 標準入力からint整数を入力
```

#### 制約

型 `T` について以下を両方要求する(後述の関数についても同様)。
- `operator>>` をサポートしている
- Default Constructive である

要するに以下をラップしているだけなので、これができない型はNG
```
T v;
is >> v;
return v;
```

### vec

```cpp
(1) Vec<T> scanner.vec(int n)
(2) Vec<T> scanner.vec(int n, T offset)
```

(1) 型 `T` の入力を $n$ 個受け取って vector配列を返す。  
(2) (1)の各要素から `offset` を引いた vector配列を返す。

以下のように使う。

```cpp
const auto as = in.vec<int>(N, 1); // 標準入力から 長さNのint配列を受け取り、各要素から1を引く
```

### vvec

```cpp
(1) Vec<Vec<T>> scanner.vvec(int m, int n)
(2) Vec<Vec<T>> scanner.vvec(int m, int n, T offset)
```

(1) 型 `T` の入力を $mn$ 個受け取って $m\times n$ の二次元vector配列を返す。  
(2) (1)の各要素から `offset` を引いた 二次元vector配列を返す。

### tup

```cpp
(1) Tup<Args...> scanner.tup()
(2) Tup<Args...> scanner.tup(Args... offsets)
```

(1) 任意型の入力を 任意個受け取って tupleにして返す。  
(2) (1)の各要素から 各々の`offset` を引いた tupleを返す。

以下のように使う。

```cpp
const auto [n,r,s] = in.tup<int,double,Str>();
const auto [u,v] = in.tup<int,int>(1,1);
```
