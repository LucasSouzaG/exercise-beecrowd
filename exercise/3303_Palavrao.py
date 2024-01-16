while True:
    try:
        palavra = input()

        if len(list(palavra)) >= 10:
            print('palavrao')
        else:
            print('palavrinha')
    except EOFError:
        break