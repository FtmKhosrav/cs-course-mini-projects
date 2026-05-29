def is_prime(x):
    if x < 2:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False

    return True


def prime_divisors(num):

    divisors = []

    for i in range(1, num // 2 + 1):

        if num % i == 0 and is_prime(i):
            divisors.append(i)

    return divisors


n = int(input())

total = 0

for number in range(1, n + 1):

    if number % 2 != 0:

        divisors = prime_divisors(number)

        if len(divisors) in divisors:
            total += number


if total == 0:
    print("NOT FOUND!")

else:
    print(int(str(total)[::-1]))
