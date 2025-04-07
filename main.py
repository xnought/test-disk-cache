from diskcache import Cache, FanoutCache

cache = FanoutCache(".fanout")
# cache = Cache(".cache")


@cache.memoize(typed=True)
def factorial(n: int):
    return 1 if n <= 1 else n * factorial(n - 1)


def main():
    for i in range(100):
        print(factorial(i))


if __name__ == "__main__":
    main()
