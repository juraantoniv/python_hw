
# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def decor(func):
    count = 0

    def inner(*a):
        nonlocal count
        count += 1
        func(*a)
        return count

    return inner

l:int = 5470304159688

str2:str = ''


@decor
def expanded_form(item_number: str):
    global str2
    st: str = str(item_number)
    for i in range(len(st)):
        number:str = st[i]
        if int(number) != 0:
            str1 = str(number) + (len(st) - i - 1) * '0'
            str2 += str1 + '+'
    return str2[:-1]



print(expanded_form(l))
print(expanded_form(l))
print(expanded_form(l))
print(expanded_form(l))




