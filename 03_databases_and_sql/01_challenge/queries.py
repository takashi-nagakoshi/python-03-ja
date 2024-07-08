
# SQLとPython＋Chinookデータベース

import sqlite3

# chinook.dbデータベースに接続
conn = sqlite3.connect('../data/chinook.db')
db = conn.cursor()

# アーティストの数
def number_of_artists(db):
    query = "SELECT COUNT(ArtistId) FROM albums a;"  # ここにSQLクエリを書いてください
    db.execute(query)
    # rows = db.fetchall()
    # print(rows)
    results = db.fetchall()
    return results[0] if results else 0

# アーティストのリスト
def list_of_artists(db):
    query = "SELECT * FROM artists ORDER BY Name ASC"  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# 「愛」をテーマにしたアルバムのリスト
def albums_about_love(db):
    query = "SELECT * FROM Tracks WHERE Name LIKE '%love%' ORDER BY Name ASC;"  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# 指定された再生時間よりも長い楽曲数
def tracks_longer_than(db, duration):
    query = "SELECT COUNT(TrackId) FROM tracks WHERE Milliseconds > ?"  # ここにSQLクエリを書いてください
    db.execute(query,(duration,))
    results = db.fetchall()
    return results[0] if results else 0

# 最も楽曲数が多いジャンルのリスト
def genres_with_most_tracks(db):
    query = "SELECT GenreId , COUNT(*) FROM tracks t GROUP BY GenreId ORDER BY COUNT(*) DESC ;"  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

artist_count = number_of_artists(db)
print(artist_count) 
print(list_of_artists(db))
print(albums_about_love(db))

duration = 1000000
track_count = tracks_longer_than(db, duration)
print(track_count)  # ここで整数をプリント

print(genres_with_most_tracks(db))
# スクリプトの最後で必ずデータベース接続を閉じる
conn.close()

