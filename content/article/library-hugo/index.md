+++
title = 'verification-helperを改造してHugoでライブラリページを作った話'
date = '2023/03/12'
publishDate = '2023/03/12'
archives = ['2023/03']
draft = false
+++

## あらすじ

- ライブラリのverify/documentationをkimiyukiさん作の最高ツール [verification-helper](https://github.com/online-judge-tools/verification-helper) でやっていた
- 大きな不満は無かったが、特にドキュメント周りを弄ってみたくなったので個人用に改造してみた
  - 完成物は完全オレオレ仕様で、配布などはしない

- 出来たもの
  - [verify/docツール](https://github.com/pachicobue/algolib/tree/main/tools/verify-doc)
  - [deploy先のサイト](https://github.com/pachicobue/pachicobue.github.io)

## 設計変更点

### verify機能

機能縮小して書き直しただけ

- 対象をC++のみに絞った
- UnitTestに対応( [本家issue](https://github.com/online-judge-tools/verification-helper/issues/233) )
  - これは本家にcontributeした方がいいかも

### doc機能

- verifyと機能分離した
  - （本家も同じかも）
  - verify結果のjsonを受け取って、ライブラリのステータスを得るだけ
- ドキュメントをライブラリとは別レポジトリで書けるようにした
  - 本家はfrontmatterにverify結果やCodeを追記したmarkdownを吐く
    - ライブラリと同じレポジトリでドキュメントを書く必要がある
  - jsonでverify結果やCodeを吐いて、それをドキュメントレポジトリで加工する設計にしてみた
    - hugoなら[jsonデータを参照する機能](https://gohugo.io/templates/data-templates/)が組み込みで存在する

### その他

- github actionパートをスクリプトから分離

## 感想

大したものを作れなかったので、あまり感想がない

- 書き始めた段階では、もっと汎用的に使える設計にできる気がしたが、蓋を開けると全然だった
- hugo, github action辺りと仲良くなれたのは良かった
- 本家のツールは本当にすごい
