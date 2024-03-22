def task_1(x):
    return x ** 2

def task_2(x):
    return x ** 3

def task_3(x):
    return x ** 4

def main(x):
    yield task_1(x)
    yield task_2(x)
    return task_3(x)

if __name__ == "__main__":
    for i in main(5):
        print(i)
