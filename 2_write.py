def main():
    # 元々のコードはコメントアウト

    with open(file='users.csv', mode='w', encoding='utf-8') as f:
        f.write('Bob,79\n')
        f.write('Tom,59')
        print('close前', f.closed)

    print('close後', f.closed)


if __name__ == '__main__':
    main()