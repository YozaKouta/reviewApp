# 関数の定義
def post_review(): # レビューの投稿
    # 変数の定義
    post = {} #空の辞書の宣言

    # genre = "映画"
    # title = "時をかける少女"
    # review = "人生の最高傑作アニメ。"

    print("ジャンルを入力してください：")
    post["genre"] = input()
    print("タイトルを入力してください：")
    post["title"] = input()
    print("感想を入力してください：")
    post["review"] = input()
    line = "\n---------------------------"

    # レビューを表示
    print("\nジャンル : " + post["genre"] + line)
    print("タイトル : " + post["title"] + line)
    print("感想 : \n" + post["review"] + line)
    
    # リストオブジェクトに追加
    posts.append(post)

def read_review():
    # enumerate関数によって要素と一緒に要素の順番を取り出す。
    for (number, post) in enumerate(posts):
        print("[" + str(number) + "]：" + post['title'] +"のレビュー")
    
    print("見たいレビューの番号を入力してください：")
    user_input = int(input())
    post = posts[user_input]
    
    line = "\n---------------------------"
    # レビューを表示
    print("\nジャンル : " + post["genre"] + line)
    print("タイトル : " + post["title"] + line)
    print("感想 : \n" + post["review"] + line)

def exception():
    # エラー処理
    print("入力した値は無効な値です")

posts = []      # 複数のレビューを持つリストオブジェクト

while True:
    # メニューの表示
    print("レビュー数："+ str(len(posts)))
    print("[0]レビューを書く")
    print("[1]レビューを読む")
    print("[2]アプリを終了する")
    user_input = int(input())

    if user_input == 0:
        post_review() # post_review関数の呼び出し
    elif user_input == 1:
        read_review() # read_review関数の呼び出し
    elif user_input == 2:
        exit()  # ここでプログラムが終わる
    else:
        exception() # exception関数の呼び出し