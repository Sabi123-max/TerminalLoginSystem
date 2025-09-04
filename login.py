import sys
import json
def main():
    try:
        ch = int(input("Please enter 1.for login\n,"
              "2.For Register:\n"))
        condition(ch)
    except ValueError:
        print("Please enter 1 or 2")




def values():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    return username, password
def read():
    with open("password.json","r") as passw:
        try:
            reader = json.load(passw)
            return reader
        except json.decoder.JSONDecodeError:
            x = {}
            return x


def condition(ch):
    if ch == 1:
        while True:
            user, password = values()
            x = read()
            if user not in x:
                print("Username doesn't exist")
                print("Please register by typing your username and password")
                user, password = values()
                print(user, password)
                x = read()
                x.update({user: password})
                with open("password.json", "w") as passw:
                    json.dump(x, passw, indent=4)
                    break
            else:
                for s in x:
                    if s == user:
                        if x[s] == password:
                            print("Login Successful")
                            sys.exit()
                        else:
                            print("Login Failed,password is wrong")
    elif ch == 2:
        user, password = values()
        print(user,password)
        x = read()
        if user in x:
            print("user already exist use a different name")
        else:
            x.update({user: password})
            with open("password.json","w") as passw:
                json.dump(x,passw,indent=4)
    else:
        print("Please enter 1 or 2")

if __name__ == '__main__':
    main()