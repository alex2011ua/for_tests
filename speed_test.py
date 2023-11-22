import timeit
import random

def main():

    l = []
    for i in range(1000):
        l.append(random.randint(0, 1000000))
    d = dict.fromkeys(l)
    s = set(l)

    def iter_l():
        for i in l:
            pass
    def iter_d():
        for i in d:
            pass
    def iter_s():
        for i in s:
            pass

    print(timeit.timeit(iter_l))
    print(timeit.timeit(iter_d))
    print(timeit.timeit(iter_s))


if __name__ == "__main__":
    main()
