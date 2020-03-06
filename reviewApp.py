# 変数の定義
# genre = "映画"
# title = "時をかける少女"
# review = "人生の最高傑作アニメ。\n\n青春厨としてはたまらない甘酸っぱい青春ストーリー。\n\nちあきのイケメンさは言うまでもない。\n\n人にお金を払ってでもみて欲しい作品。\n\n早く見たほうがいいよ。\n\nTime waits for no one."

print("ジャンルを入力してください：")
genre = input()
print("タイトルを入力してください：")
title = input()
print("感想を入力してください：")
review = input()
line = "\n---------------------------"

# レビューを表示
print("\nジャンル : " + genre + line)
print("タイトル : " + title + line)
print("感想 : \n" + review + line)