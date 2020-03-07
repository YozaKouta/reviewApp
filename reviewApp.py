# 関数の定義
def post_review():
    # 変数の定義
    post = {} #空の辞書の宣言

    # genre = "映画"
    # title = "時をかける少女"
    # review = "人生の最高傑作アニメ。\n\n青春厨としてはたまらない甘酸っぱい青春ストーリー。\n\nちあきのイケメンさは言うまでもない。\n\n人にお金を払ってでもみて欲しい作品。\n\n早く見たほうがいいよ。\n\nTime waits for no one."

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


def read_review():
    # まだ処理内容が決まっていない
    pass

def exception():
    print("入力した値は無効な値です")


# メニューの表示
print("レビュー数：0")
print("[0]レビューを書く")
print("[1]レビューを読む")
print("[2]アプリを終了する")
user_input = int(input())


if user_input == 0:
    post_review() # post_review関数の呼び出し
    
elif user_input == 1:
    read_review() # read_review関数の呼び出し

elif user_input == 2:
    exit

else:
    exception() # exception関数の呼び出し
    