import csv
import json
import os

def read_csv(file_path):
    """
    CSVファイルを読み取り、その内容を辞書のリストで返す

    :引数 file_path: 文字列 - CSVファイルへのパス
    :戻り値: リスト - CSVの列を表す辞書のリスト
    """
    # ここに実装してください
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def csv_to_json(csv_data):
    """
    CSVデータ (辞書のリスト) を受け取り、それをJSON形式 (文字列) に変換する

    :引数 csv_data: リスト - 辞書のリストで表したCSVデータ
    :戻り値: 文字列 - JSON形式で表したデータ
    """
    # ここに実装してください
    return json.dumps(csv_data, ensure_ascii=False, indent=4)

def write_json(json_data, file_path):
    """
    JSONデータをファイルに書き込む

    :param json_data: 文字列 - 書き込むJSONデータ
    :param file_path: 文字列 - JSONファイルへのパス
    """
    # ここに実装してください
    with open(file_path, mode='w', encoding='utf-8') as file:
        file.write(json_data)

def read_json(file_path):
    """
    JSONファイルを読み取ってその内容を返す

    :引数 file_path: 文字列 - JSONファイルへのパス
    :戻り値: JSONファイルの内容
    """
    # ここに実装してください
    with open(file_path, mode='r', encoding='utf-8') as file:
        return json.load(file)

def json_to_csv(json_data):
    """
    JSONデータを受け取り (通常は辞書のリスト)、それをCSV形式 (文字列) に変換する

    :引数 json_data: JSONデータ
    :戻り値: 文字列 - CSV形式で表したデータ
    """
    # ここに実装してください
    if len(json_data) == 0:
        return "", []
    fieldnames = json_data[0].keys()
    csv_data = [fieldnames, *[row.values() for row in json_data]]
    return fieldnames, csv_data

def write_csv(csv_data, file_path):
    """
    CSVデータをファイルに書き込む

    :引数 csv_data: 文字列 - 書き込むCSVデータ
    :引数 file_path: 文字列 - CSVファイルへのパス
    """
    # ここに実装してください
    fieldnames, data = csv_data
    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(fieldnames)
        writer.writerows(data)

def validate_data(data, data_type):
    """
    データの整合性を確認する (例: CSVの列数に一貫性があること)

    :引数 data: 検証対象のデータ
    :引数 data_type: 文字列 - データ型 ('CSV' または 'JSON')
    :戻り値: bool - データが有効な場合はTrue、無効な場合はFalse
    """
    # ここに実装してください
    if data_type == 'CSV':
        fieldnames = data[0].keys()
        for row in data:
            if row.keys() != fieldnames:
                return False
    elif data_type == 'JSON':
        if not isinstance(data, list):
            return False
        if not all(isinstance(item, dict) for item in data):
            return False
    return True

def process_directory(directory_path):
    """
    指定されたディレクトリにあるすべてのCSVまたはJSONファイルを確認し、適切に変換する

    :引数 directory_path: 文字列 - 処理対象のディレクトリへのパス
    """
    # ここに実装してください
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if filename.endswith('.csv'):
            csv_data = read_csv(file_path)
            if validate_data(csv_data, 'CSV'):
                json_data = csv_to_json(csv_data)
                json_file_path = os.path.splitext(file_path)[0] + '.json'
                write_json(json_data, json_file_path)
        elif filename.endswith('.json'):
            json_data = read_json(file_path)
            if validate_data(json_data, 'JSON'):
                csv_data = json_to_csv(json_data)
                csv_file_path = os.path.splitext(file_path)[0] + '.csv'
                write_csv(csv_data, csv_file_path)

# スクリプトを実行するmain関数
def main():
    # 使用例
    try:
        directory = "."
        process_directory(directory)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

    print(os.getcwd())

