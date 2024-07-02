# File Manipulator

```
File Manipulator は、ファイルの内容を操作するための簡単な Python スクリプトです。このツールを使用することで、ファイルの内容を逆順にする、ファイルをコピーする、ファイルの内容を複製する、そしてファイル内の文字列を置換するなどの操作を簡単に行うことができます。
```

## 機能

```
File Manipulator は以下の4つの主要な機能を提供します：

1. ファイルの内容を逆順にする
2. ファイルをコピーする
3. ファイルの内容を複製する
4. ファイル内の文字列を置換する
```

## 使用方法

```
スクリプトは、コマンドライン引数を使用して操作します。基本的な使用方法は以下の通りです：

python file_manipulator.py <command> <args>
```

各コマンドの詳細な使用方法は以下の通りです：

### 1. reverse

```
入力ファイルの内容を逆順にして、新しいファイルに保存します。

python file_manipulator.py reverse <input_path> <output_path>

- <input_path>: 入力ファイルのパス
- <output_path>: 出力ファイルのパス
```

### 2. copy

```
ファイルをコピーします。

python file_manipulator.py copy <input_path> <output_path>

- <input_path>: コピー元ファイルのパス
- <output_path>: コピー先ファイルのパス
```

### 3. duplicate-contents

```
ファイルの内容を指定された回数だけ複製します。

python file_manipulator.py duplicate-contents <input_path> <n>

- <input_path>: 操作対象のファイルパス
- <n>: 複製する回数（正の整数）
```

### 4. replace-string

```
ファイル内の特定の文字列を新しい文字列に置換します。

python file_manipulator.py replace-string <input_path> <needle> <new_string>

- <input_path>: 操作対象のファイルパス
- <needle>: 置換対象の文字列
- <new_string>: 置換後の新しい文字列
```

## エラーハンドリング

```
File Manipulator は、無効な入力や存在しないファイルパスなどのエラーを適切に処理し、ユーザーにわかりやすいエラーメッセージを表示します。
```

## 注意事項

```
- ファイルの操作を行う前に、重要なファイルのバックアップを取ることをおすすめします。
- 大きなファイルを扱う場合、操作に時間がかかる場合があります。
```

## ライセンス

```
このプロジェクトは [MIT ライセンス](https://opensource.org/licenses/MIT) の下で公開されています。
```# file_manipulator
