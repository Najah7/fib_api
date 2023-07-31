# speee_homework

# 目次
1. [課題1について](#課題１について)
    - [公開URL](#公開url)
    - [API仕様](#api仕様)
        - [エンドポイント](#エンドポイント)
        - [概要](#概要)
        - [メソッド](#メソッド)
        - [パラメータ](#パラメータ)
        - [リクエスト例(URL)](#リクエスト例url)
        - [レスポンス](#レスポンス)
        - [エラーレスポンス](#エラーレスポンス)
    - [テスト](#テスト)
        - [動作確認(サンプル)](#動作確認サンプル)
        - [テスト実行方法](#テスト実行方法)
2. [課題2について](#課題２について)
    - [説明文の配置場所](#説明文の配置場所)
    - [補足](#補足)
    

# 課題１について

## 公開URL
https://najah.pythonanywhere.com/fib

## API仕様

### エンドポイント
- `/fib`

### 概要
n番目のフィボナッチ数を返す

### メソッド
- GET


### パラメータ
- n: フィボナッチ数の番号

### リクエスト例(URL)
- https://najah.pythonanywhere.com/fib?n=50

### レスポンス
- 200 OK
```json
{
  "result": 12586269025
}
```

### エラーレスポンス
- 400 NG without n parameter
```json
{
    "message":"Missing query parameter 'n'. Please provide 'n' as a positive integer.",
    "status":400
}
```
- 400 NG, n is not positive integer
```json
{
    "message":"Invalid input. n must be a positive integer.",
    "status":400
}
```

※👆pythonanywhereの環境では、jsonの整形（改行はできなかった）

## テスト

### 動作確認(サンプル)
```bash
curl -X GET -H "Content-Type: application/json" "https://najah.pythonanywhere.com/fib?n=50"
```

### テスト実行方法
```bash
python -m unittest discover
```
👆注意点：testsディレクトリに移動しないでください。ルートで実行してください。

## 課題２について

### 説明文の配置場所
- [/report/v2_how_website_is_rendered.md]([https://github.com/Najah7/speee_homework/blob/main/report/how_website_is_rendered.md](https://github.com/Najah7/fib_api/blob/main/report/v2_how_website_is_rendered.md)https://github.com/Najah7/fib_api/blob/main/report/v2_how_website_is_rendered.md)

### 補足
親に対してという、テーマだったので、初心者や、知識がない人にもわかりやすいように、説明文を書きました。
