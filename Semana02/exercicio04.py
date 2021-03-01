from massa_dados import list_spend_money


def spend_by_login(login, limit=1000):
    sum = 0
    for i in list_spend_money:
        if sum >= limit:
            break
        if login == i[1]:
            print(f"{i[0]} ({i[1]}) gastou {i[3]}")
    return sum


def sum_by_login(login, limit=1000):
    sum = 0
    for i in list_spend_money:
        if sum >= limit:
            break
        if login == i[1]:
            sum += float(i[3]) if i[3] != '' else 0
    return sum


if __name__ == "__main__":
    login = 'justin16'
    spend_by_login(login, 1200)
    print('A soma total até 600: ')
    print(sum_by_login(login, 600))
    print('A soma total até 1200: ')
    print(sum_by_login(login, 1200))
