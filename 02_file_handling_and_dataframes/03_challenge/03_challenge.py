# ここにコードを書いてください
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

# 1. データセットのロード
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target

# 1. データの概要
print("データの最初の5行:")
print(iris_df.head())

# 2. データのスクリーニングと検証
# 欠損値の確認
print("\n欠損値の確認:")
print(iris_df.isnull().sum())
# データ型の確認
print("\n各列のデータ型:")
print(iris_df.dtypes)
# 3. 基本的な分析と基本統計量
basic_stats = iris_df.describe().T
print("\n基本統計量:")
print(basic_stats)

# 基本統計量のDataFrameを新規作成し、CSVとして保存
basic_stats.reset_index(inplace=True)
basic_stats.rename(columns={'index': 'feature'}, inplace=True)
basic_stats.to_csv('basic_stats.csv', index=False)

# 4. 特徴量エンジニアリング
iris_df['sepal_area'] = iris_df['sepal length (cm)'] * iris_df['sepal width (cm)']
iris_df['petal_area'] = iris_df['petal length (cm)'] * iris_df['petal width (cm)']

# 新しい特徴量の基本統計量を計算し、統計情報のDataFrameに追加
new_stats = iris_df[['sepal_area', 'petal_area']].describe().T
new_stats.reset_index(inplace=True)
new_stats.rename(columns={'index': 'feature'}, inplace=True)
new_stats.to_csv('new_features_stats.csv', index=False)

# 5. データのフィルタリング
def filter_data(df, column, threshold):
    """
    指定した列の値がしきい値を下回る行を除外する
    :param df: DataFrame
    :param column: 文字列 - 列名
    :param threshold: 数値 - しきい値
    :return: フィルタリングされたDataFrame
    """
    return df[df[column] >= threshold]

# 例: ガクの面積が15以上の行のみを含むデータフレームを取得
filtered_df = filter_data(iris_df, 'sepal_area', 15)
print("\nフィルタリング後のデータの最初の5行:")
print(filtered_df.head())

# 6. データのエクスポート
# 元のデータフレームをCSVとして保存
iris_df.to_csv('iris_data_with_areas.csv', index=False)

# フィルタリングされたデータフレームをCSVとして保存
filtered_df.to_csv('filtered_iris_data.csv', index=False)