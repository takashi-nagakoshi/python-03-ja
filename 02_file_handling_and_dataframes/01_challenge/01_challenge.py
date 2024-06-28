import os
from pathlib import Path

# ディレクトリ内のファイルを辞書にインポートする関数
def import_books_to_dict(directory):
    books_dict = {}
    for filename in os.listdir(directory):
        # print(filename)
        if filename.startswith('Chapter_'):
            continue  # 'Chapter_x.txt' ファイルはスキップ
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                books_dict[filename] = file.read()
    return books_dict

# 辞書の内容を1つのテキストファイルに保存する関数
def save_books_to_file(books_dict, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for filename, content in books_dict.items():
            file.write(f"=== {filename} ===\n")
            file.write(content)
            file.write("\n\n")

# ディレクトリを作成し、Chapter_x.txtファイルを移動する関数
def create_library_and_move_files(data_dir):
    library_dir = Path(data_dir) / 'library'
    library_dir.mkdir(exist_ok=True)
    
    for i in range(1, 11):
        chapter_file = Path(data_dir) / f'Chapter_{i}.txt'
        if chapter_file.exists():
            new_location = library_dir / chapter_file.name
            chapter_file.replace(new_location)
    
    return library_dir
# ファイルとサイズを一覧表示する関数
def list_files_and_sizes(directory):
    print(f"Files in {directory}:")
    for file_path in directory.iterdir():
        if file_path.is_file():
            size = file_path.stat().st_size
            print(f"{file_path.name}: {size} bytes")

# メイン関数
def main():
    # パスをraw文字列として指定
    data_dir = 'data/text_files'
    data_dir2 = 'data'
    output_file = 'combined_books.txt'

    # 書籍のファイルを辞書にインポート
    books_dict = import_books_to_dict(data_dir)

    # 辞書の内容を1つのテキストファイルに保存
    save_books_to_file(books_dict, output_file)
    print(f"Books combined and saved to {output_file}")

        # ディレクトリの作成とファイルの移動
    library_dir = create_library_and_move_files(data_dir)

    # ファイルとサイズの一覧表示
    list_files_and_sizes(library_dir)

if __name__ == "__main__":
    main()
