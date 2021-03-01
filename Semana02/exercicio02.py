from massa_dados import list_spend_money


def spend_by_gender(gender):
    for i in list_spend_money:
        if gender == i[2]:
            print(f"{i[0]} ({i[2]}) gastou {i[3]}")


def sum_by_gender(gender):
    sum = 0
    for i in list_spend_money:
        if gender == i[2]:
            sum += float(i[3]) if i[3] != '' else 0
    return sum


if __name__ == "__main__":
    gender = 'M'
    spend_by_gender(gender)
    print('A soma total é: ')
    print(sum_by_gender(gender))
