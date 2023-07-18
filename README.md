# ゲーム のタイトル
* コインゲッター

## 実行環境の必要条件
* python >= 3.10.9
* pygame >= 2.1

## ゲームの概要
* 上から落ちてくるコインを集めてスコアを稼ぐ

## ゲームの実装
###共通基本機能
<<<<<<< HEAD
* playerとplayerの移動
* 普通のコイン（スコア、落下速度など）
* スコア

### 担当追加機能

* スーパーコインと防壁　（魯珺生）
* 残り時間表示　（小松）
* 背景画像を入れる　（竹下）
* playerを画像に変更　（山田）
* 爆弾機能実装（王）

* super_coin(魯珺生担当)：集めたら普通のコインの2倍のスコアをもらえる。普通のコインより集めしにくい。
* 防壁(魯珺生担当)：tabを押すとplayerの上に防壁が現れる。コインは防壁にぶつかると消える。

=======
* ほげほげ
* ふがふが
* ぴよぴよ
* Time機能（担当：マナト）：時間の管理を行うクラスの追加、Timeが0になったら強制終了する機能

### ToDo
- [ ] ほげほげ機能
- [ ] ふがふが関数内の変数名の統一
- [ ] ゲームオーバー時の文字の表示

### メモ
* 防壁は追加機能「爆弾」に合わせるために作った機能です
* コインの機能
* 爆弾を追加
* 爆弾と突き当ったら、ゲーム終了 

### ToDo
- [ ] 爆弾の機能
* クラス内の変数は，すべて，「get_変数名」という名前のメソッドを介してアクセスするように設計してある
* すべてのクラスに関係する関数は，クラスの外で定義してある
