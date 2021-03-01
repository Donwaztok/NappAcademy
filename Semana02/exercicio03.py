from massa_dados import list_spend_money


def spend_by_subname(name):
    for i in list_spend_money:
        if name in i[0]:
            print(f"{i[0]} ({i[1]}) gastou {i[3]}")


def sum_by_subname(name):
    sum = 0
    for i in list_spend_money:
        if name in i[0]:
            sum += float(i[3]) if i[3] != '' else 0
    return sum


if __name__ == "__main__":
    name = 'Brown'
    spend_by_subname(name)
    print('A soma total é: ')
    print(sum_by_subname(name))
