def write01():
    # ファイルオブジェクトを生成
    # mode='a'は「追記モード」
    f = open("fruits.txt", mode="a")

    f.write("リンゴ")
    f.write("ミカン")
    f.write("メロン")

    # データが破損したりする場合があるので忘れない！
    f.close()
    # with使ってないからcloseする必要あり


if __name__ == "__main__":
    write01()
