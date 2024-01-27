def fatorial(number:int):
    if number == 0:
        return 1
    else:
        return number * fatorial(number - 1)

while True:
    try:
        m_n = input()

        print(fatorial(int(m_n.split()[0])) + fatorial(int(m_n.split()[1])))

    except EOFError:
        break