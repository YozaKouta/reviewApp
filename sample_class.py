class Review:
    review_count = 0
    
    @classmethod
    def get_review_count(cls):
        return cls.review_count
    
    def __init__(self):
        print("Reviewクラスのインスタンスが生成されました")
        print("ジャンルを入力してください")
        self.genre = input()
        print("タイトルを入力してください")
        self.title = input()
        print("感想を入力してください")
        self.impression = input()
        Review.review_count += 1
        
    def show_review(self):
        line = "\n------------------------------"
        print("ジャンル：" + self.genre + line)
        print("タイトル：" + self.title + line)
        print("感想：" + self.impression + line)

while True:
    # メニューの表示
    print("書いたレビュー数："+ str(Review.get_review_count()))
    print("[0]レビューを書く")
    print("[1]アプリを終了する")
    user_input = int(input())

    if user_input == 0:
        review = Review() # Reviewクラスのインスタンスを生成
        review.show_review()
    elif user_input == 1:
        exit()  # ここでプログラムが終わる
    else:
        print("入力した値は無効です")