def hello():
    return "Hello World!"


def practice():  # lint on save 켰는데 왜 저장해도 안고쳐주지..
    return "on sparkplus"


if __name__ == "__main__":  # pragma: no cover
    ret = hello()
    ret2 = practice()
    print(ret, ret2)