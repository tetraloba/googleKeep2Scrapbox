# googleKeep2Scrapbox
Google Keep から Scrapbox にデータを移行するためのスクリプト(Python)

# 説明 (ver0.0.0)
## 使用方法
1. [Google Keep のデータをエクスポート](https://support.google.com/keep/answer/10017039?hl=ja)し、zip形式でダウンロードする。  
1. zipを解凍し、Keepフォルダ(中にjsonファイルが入っている)をプロジェクト直下(main.pyと同じ階層)に置く。
1. スクリプトを実行する。
    ```bash
    python main.py
    ```
1. プロジェクト直下にscrapbox.jsonが生成されるので、それを[Scrapboxにインポート](https://scrapbox.io/help-jp/Import_Pages_%2F_Export_Pages)する。

なお、現状(ver0.0.0)ではtextContent(通常のメモ)にしか対応しておらず、チェックリストなどの形式には非対応(スキップされる)。また、画像なども全て無視される。