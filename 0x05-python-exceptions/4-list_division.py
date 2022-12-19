#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        for i in range(list_length):
            div = my_list_1[i] / my_list_2[i]
            i++
    except TypeError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")
    finally:
        print(div)
