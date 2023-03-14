+++
title = '2023/03/13'
date = '2023/03/13'
publishDate = '2023/03/14'
archives = ['2023/03']
draft = false
math = true
+++

日中は仕事

牛乳の賞味期限が近づいていたので、今日の夕飯はクラムチャウダーにした。  
牛乳1パック分作ったので、しばらくはこれを食べ続けることになりそう。

夕飯後はyukicoderの問題を考えていた。  
日曜日に取り組んでWAが出ていた https://yukicoder.me/problems/no/2242 は結局ライブラリの不備だった。  
ダブリングで $\mathrm{dp}[v][k] = \text{頂点}v\text{から}2^k\text{先の頂点}$ を作るとして、必要な $k$ の最大値を求める部分を2冪でミスっていた。要は $\lceil \log_2{N} \rceil$ の計算間違い。  
こういうケースを入れていてくれてありがとうという気持ちに。

「今日は眠いし、もう一問だけ解いて日記を書いて寝るか」と思って、寝る準備をしてから https://yukicoder.me/problems/no/2243 を開いた。  
包除を使うと以下の式になる。
$$
\begin{aligned}
&\sum_{j=0}^N \frac{(-1)^j}{j!} \sum_{d=0}^{N-j} (d!)^{M-1}\frac{(j+d)!}{\prod_{k=1}^M (d-n_k)!}\\\\
\text{where }\\\\
&n_k = \\# \lbrace i \mid A_i = k \rbrace
\end{aligned}
$$
畳み込みで解けそうだな～と思って、しばらく考えていたら眠気が押し寄せてきてそのまま寝てしまった。
