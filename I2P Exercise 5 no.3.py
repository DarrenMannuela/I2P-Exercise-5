def find_value(my_dict: dict, val):
    same_mark = []
    for subject, mark in my_dict.items():
        if val == mark:
            same_mark.append(subject)
    return same_mark


if __name__ == "__main__":
    grades = {"Maths": 89, "English": 65, "Chemistry": 89, "Physics": 65, "Biology": 91}
    value = int(input("What mark do you want to find:"))
    print(find_value(grades, value))
