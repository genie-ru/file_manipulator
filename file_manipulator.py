import sys
import os

def reverse_file(input_path, output_path):
    try:
        with open(input_path, 'r') as input_file:
            content = input_file.read()
        with open(output_path, 'w') as output_file:
            output_file.write(content[::-1])
        print(f"ファイルを逆順にして {output_path} に保存しました。")
    except IOError as e:
        print(f"エラー: ファイルの操作中に問題が発生しました。{e}")

def copy_file(input_path, output_path):
    try:
        with open(input_path, 'r') as input_file:
            content = input_file.read()
        with open(output_path, 'w') as output_file:
            output_file.write(content)
        print(f"ファイルを {output_path} にコピーしました。")
    except IOError as e:
        print(f"エラー: ファイルのコピー中に問題が発生しました。{e}")

def duplicate_contents(input_path, n):
    try:
        n = int(n)
        if n < 0:
            raise ValueError("nは正の整数である必要があります。")
        with open(input_path, 'r') as file:
            content = file.read()
        with open(input_path, 'w') as file:
            file.write(content * (n + 1))
        print(f"ファイルの内容を {n} 回複製しました。")
    except ValueError as e:
        print(f"エラー: 無効な入力です。{e}")
    except IOError as e:
        print(f"エラー: ファイルの操作中に問題が発生しました。{e}")

def replace_string(input_path, needle, new_string):
    try:
        with open(input_path, 'r') as file:
            content = file.read()
        content = content.replace(needle, new_string)
        with open(input_path, 'w') as file:
            file.write(content)
        print(f"'{needle}' を '{new_string}' に置換しました。")
    except IOError as e:
        print(f"エラー: ファイルの操作中に問題が発生しました。{e}")

def validate_file_path(file_path, should_exist=True):
    if should_exist and not os.path.exists(file_path):
        raise FileNotFoundError(f"ファイル {file_path} が見つかりません。")
    if not should_exist and os.path.exists(file_path):
        raise FileExistsError(f"ファイル {file_path} は既に存在します。")

def main():
    if len(sys.argv) < 3:
        print("使用法: python file_manipulator.py <command> <args>")
        sys.exit(1)

    command = sys.argv[1]

    try:
        if command == "reverse":
            if len(sys.argv) != 4:
                raise ValueError("reverse コマンドは2つの引数が必要です。")
            validate_file_path(sys.argv[2])
            validate_file_path(sys.argv[3], should_exist=False)
            reverse_file(sys.argv[2], sys.argv[3])
        elif command == "copy":
            if len(sys.argv) != 4:
                raise ValueError("copy コマンドは2つの引数が必要です。")
            validate_file_path(sys.argv[2])
            validate_file_path(sys.argv[3], should_exist=False)
            copy_file(sys.argv[2], sys.argv[3])
        elif command == "duplicate-contents":
            if len(sys.argv) != 4:
                raise ValueError("duplicate-contents コマンドは2つの引数が必要です。")
            validate_file_path(sys.argv[2])
            duplicate_contents(sys.argv[2], sys.argv[3])
        elif command == "replace-string":
            if len(sys.argv) != 5:
                raise ValueError("replace-string コマンドは3つの引数が必要です。")
            validate_file_path(sys.argv[2])
            replace_string(sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            print(f"不明なコマンド: {command}")
            sys.exit(1)
    except (ValueError, FileNotFoundError, FileExistsError) as e:
        print(f"エラー: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()