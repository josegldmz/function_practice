def hello():
    print('hello, welcome!')


def pack(food, snack, drinks):
    return [food, snack, drinks]

def eat_lunch(list):
    if len(list) == 0:
        print("my box is empty!")
    else:
        for i in range(len(list)):
            if i == 0:
                print("First I eat {list[1]}")
            else:
                print('Next, I eat {list[i]}')