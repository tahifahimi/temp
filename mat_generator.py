import random

SIZE = 50
RANGE = 5


def main():
    with open("data/M.txt", "w") as f:
        for i in range(SIZE):
            for j in range(SIZE):
                f.write(f"M,{i},{j},{random.randint(0, RANGE)}\n")

    with open("data/N.txt", "w") as f:
        for i in range(SIZE):
            for j in range(SIZE):
                f.write(f"N,{i},{j},{random.randint(0, RANGE)}\n")


if __name__ == '__main__':
    main()
