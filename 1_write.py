def main():
    f = open(file='users.csv', mode='w', encoding='utf-8')
    # mode='w'にすると、実行するたびに上書きされる

    f.write('Bob,79\n')
    f.write('Tom,59')

    print("close前", f.closed)
    f.close()
    print("close後", f.closed)


if __name__ == '__main__':
    main()