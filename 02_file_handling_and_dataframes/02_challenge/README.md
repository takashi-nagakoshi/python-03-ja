## チャレンジ2: **データ変換のツールキット**

**目的**: CSV形式とJSON形式の間でデータを変換する機能を備えたPythonモジュールを開発します。データの整合性を確保し、ディレクトリ内のファイル処理を自動化してください。提供されている "sample.csv" ファイルと "sample.json" ファイルを使用してください (テストで使用します)。

### **タスク**

1. **CSVを読み取る**
    - 関数: **`read_csv(file_path)`**
    - 説明: CSVファイルを読み取り、その内容を辞書のリストとして返します。
2. **CSVからJSONに変換する**
    - 関数: **`csv_to_json(csv_data)`**
    - 説明: CSVデータ (辞書のリスト) を受け取り、JSON形式 (文字列) に変換します。
3. **JSONに書き込む**
    - 関数: **`write_json(json_data, file_path)`**
    - 説明: JSONデータをファイルに書き込みます。
4. **JSONを読み取る**
    - 関数: **`read_json(file_path)`**
    - 説明: JSONファイルを読み取り、その内容をデータ (一般には辞書型のリスト) として返します。
5. **JSONからCSVへの変換**
    - 関数: **`json_to_csv(json_data)`**
    - 説明: JSONデータ (一般には辞書のリスト) を受け取り、CSV形式 (文字列) に変換します。
6. **CSVへの書き込み**
    - 関数: **`write_csv(csv_data, file_path)`**
    - 説明: CSVデータをファイルに書き込みます。
7. **データ検証**
    - 関数: **`validate_data(data, data_type)`**
    - 説明: データの整合性をチェックします (例: CSVの列数が一貫している)。**`data_type`** はCSVまたはJSONです。
8. **ファイル処理の自動化**
    - 関数: **`process_directory(directory_path)`**
    - 説明: 特定のディレクトリ内のすべてのCSVファイルとJSONファイルを識別し、適切に変換します。
9. **ログ記録とエラー処理**
    - 処理の流れを追跡するためのログ記録と、例外を管理するためのエラー処理を実装します。