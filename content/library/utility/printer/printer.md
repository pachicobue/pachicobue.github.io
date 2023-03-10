+++
title = "Printer (出力補助クラス)"
draft = false
math = true
shwoToc = true
+++

## 概要

出力を行うクラス  
「複数の値を空白区切りで出力して末尾改行」みたいのをラップしている。

## I/F

### コンストラクタ

```cpp
Printer printer(Ostream& os = std::cout)
```

引数には出力先(デフォルトは標準出力)を与える。  
内部で `std::fixed` と `std::setprecision(15)` を流す(これはやりすぎかも)。

グローバルに標準出力を使う Printer を定義している。大体これを使えばよい。
```cpp
Printer out;
```

### operator()

```cpp
int printer(Args... args)
```

`args` を空白区切りで出力。 末尾の改行は **行わない**。  
引数は任意個受け取れ、 `operator<<` をサポートする型なら何でも受け取れる。  

返り値が `int` なので、標準出力してmain関数を終了したい場合に以下のように書ける。
```cpp
int main()
{
    if (~~~) {
        return out("Yes"); // Yesと出力して終了(ただし改行はしない)
    }
    ...
}
```

#### 制約

出力する型について以下のどちらかを要求する(後述の関数も同様)
- `operator<<` をサポートしている
- または `Vec<T>`, `Vec<Vec<T>>` である(かつ `T` が上を満たす)

### ln()

```cpp
int printer.ln(Args... args)
```

`args` を空白区切りで出力。 末尾の改行を行う。  
引数は任意個受け取れ、 `operator<<` をサポートする型なら何でも受け取れる。  

基本的にはこれを使う。

### el()

```cpp
int printer.el(Args... args)
```

`args` を空白区切りで出力。 末尾の改行を行う。  
改行に `std::endl` を使う点が `ln()` との違い。インタラクティブで使う。  
引数は任意個受け取れ、 `operator<<` をサポートする型なら何でも受け取れる。  

### vectorの出力

vector配列について「要素を空白区切りで出力＋末尾改行」をするのは若干面倒。  
`Printer` はvector配列を「空白区切りで出力」しているので、上記出力は以下のように書ける。

```cpp
Vec<int> vs{1,2,3,4};
out.ln(vs); // "1 2 3 4" が末尾改行付きで出力される
```

使い道は多くないが、二次元vector配列は「長方形型に出力」する。

```cpp
Vec<Vec<int>> vss{ {1,2,3}, {4,5,6} };
out.ln(vss); /* "1 2 3
                 4 5 6" が末尾改行付きで出力される */
```
