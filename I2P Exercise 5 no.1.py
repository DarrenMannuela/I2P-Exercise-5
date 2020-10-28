cars = {"Ford": "Bronco", "Nissan": "Terra", "Mitsubishi": "Xpander"}
Owned_cars = ["Nissan", "Mitsubishi"]


def remove_keys(my_dict: dict, key_list: list):
    text = ""
    for keys in range(len(key_list)):
        text = "{0}".format(key_list[keys])
        if text in my_dict:
            my_dict.pop(text)
    return my_dict


if __name__ == "__main__":
    print(remove_keys(cars, Owned_cars))