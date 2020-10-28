
def accept_login(users: dict, username, password):
    if username in users:
        if users[username] == password:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    people = {"John": "H3l0", "Regina": "B0l4", "David": "Quut0n"}
    name = input("Username:")
    pswd = input("Password:")
    print(accept_login(people, name, pswd))