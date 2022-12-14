# Назовём натуральное число подходящим, если ровно два из его делителей
# входят в список (7, 13, 17, 19). Найдите все подходящие числа, принадлежащих
# отрезку [25 000; 35 000] В ответе запишите два целых числа, через пробел:
# сначала количество, затем сумму цифр всех найденных чисел.

def sumOfDigits(n):
    ans = 0
    while n > 0:
        ans += n % 10
        n //= 10
    return ans

cnt = ans = 0
for i in range(25000, 35000 + 1):
    k = 0
    if i % 7:
        k += 1
    if i % 13:
        k += 1
    if i % 17:
        k += 1
    if i % 19:
        k += 1
    if k == 2:
        cnt += 1
        ans += sumOfDigits(i)
print(cnt, ans)
