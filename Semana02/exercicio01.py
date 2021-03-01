from massa_dados import list_spend_money


def spend_by_login(login):
    for i in list_spend_money:
        if login == i[1]:
            print(f"{i[0]} ({i[1]}) gastou {i[3]}")


def sum_by_login(login):
    sum = 0
    for i in list_spend_money:
        if login == i[1]:
            sum += float(i[3]) if i[3] != '' else 0
    return sum


if __name__ == "__main__":
    login = 'justin16'
    spend_by_login(login)
    print('A soma total é: ')
    print(sum_by_login(login))
