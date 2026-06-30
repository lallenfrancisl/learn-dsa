# fibonacci series: 1 2 3 5 8 13 21
def fibonacci(n: int) -> list[int]:
    result = [1, 2]

    for i in range(1, n - 1):
        sum = result[i] + result[i - 1]
        result.append(sum)

    return result


if __name__ == "__main__":
    print(fibonacci(21))
