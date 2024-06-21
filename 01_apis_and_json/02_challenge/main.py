import requests
import json

API_URL = "https://jsonplaceholder.typicode.com/posts"
# １一覧表示、
def list_posts():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            # 文字列からpythonが使えるコード
            posts = response.json()
            for post in posts:
                print(f"ID{post['id']}: TITLE:{post['title']}")
        else:
            print(f"Error listing posts: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error listing posts: {e}")
# ２作成、
def create_post(title, body, user_id):
    try:
        new_post = {"title": title, "body": body, "userId": user_id}
        response = requests.post(API_URL, json=new_post)
        if response.status_code == 201:
            post = response.json()
            print(f"Post created: {post['id']}")
        else:
            print(f"Error creating post: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error creating post: {e}")
# ３更新、
def update_post(post_id, title=None, body=None):
    try:
        updated_post = {}
        if title:
            updated_post["title"] = title
        if body:
            updated_post["body"] = body
        response = requests.put(f"{API_URL}/{post_id}", json=updated_post)
        if response.status_code == 200:
            post = response.json()
            print(f"Post updated: {post['id']}")
        else:
            print(f"Error updating post: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error updating post: {e}")
# ４削除
def delete_post(post_id):
    try:
        response = requests.delete(f"{API_URL}/{post_id}")
        if response.status_code == 200 or response.status_code == 201:
            print(f"Post deleted: {post_id}")
        else:
            print(f"Error deleting post: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error deleting post: {e}")
# メイン
def main():
    # 無限ループ
    while True:
        print("\nWelcome to Blog Post CLI")
        print("1. List posts")
        print("2. Create post")
        print("3. Update post")
        print("4. Delete post")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            list_posts()
        elif choice == "2":
            title = input("Enter title: ")
            body = input("Enter body: ")
            user_id = input("Enter user ID: ")
            create_post(title, body, user_id)
        elif choice == "3":
            post_id = input("Enter post ID to update: ")
            title = input("Enter new title (leave blank to keep current): ")
            body = input("Enter new body (leave blank to keep current): ")
            update_post(post_id, title if title else None, body if body else None)
        elif choice == "4":
            post_id = input("Enter post ID to delete: ")
            delete_post(post_id)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
