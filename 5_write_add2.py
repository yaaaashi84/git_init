def write02():
    # ファイルオブジェクトを生成
    f = open("fruits.txt", mode="a", encoding='utf-8')
    # printの出力先をファイルにすることもできる
    # (ファイル指定するとprintの中身がファイル生成される、指定無しなら普通にターミナルに出力)
    print("バナナ", file=f)

    # データが破損したりする場合があるので忘れない！
    f.close()


if __name__ == "__main__":
    # write02()
    write02()
