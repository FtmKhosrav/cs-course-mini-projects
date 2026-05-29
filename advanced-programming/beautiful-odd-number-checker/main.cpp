def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def count_prime_divisors(n):
    count = 0

    for d in range(1, n + 1):
        if n % d == 0 and is_prime(d):
            count += 1

    return count


n = int(input())

total = 0

for number in range(1, n + 1):

    prime_divisor_count = count_prime_divisors(number)

    if (
        prime_divisor_count > 0
        and is_prime(prime_divisor_count)
        and number % prime_divisor_count == 0
    ):
        total += number

if total == 0:
    print("NOT FOUND!")

else:
    reversed_number = int(str(total)[::-1])
    print(reversed_number)
