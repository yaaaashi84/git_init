def main():
    # ファイルオブジェクトを生成
    with open(file="users.csv", mode="r") as f:
        text = f.read()
        # text = f.readlines()
        # 行ごとにリスト化してくれる
    users = text.split("\n")

    for user in users:
        name, age = user.split(",")

        print(f"Name: {name} Age: {age}")


if __name__ == "__main__":
    # read01()
    main()