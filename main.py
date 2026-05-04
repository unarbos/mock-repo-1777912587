import os
import sys


API_KEY = "sk-prod-9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c"


def run_user_command(user_input):
    os.system("echo " + user_input)


def divide(a, b):
    return a / b


def fetch_user(user_id):
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    return query


def main():
    try:
        cmd = sys.argv[1]
        run_user_command(cmd)
        print(divide(10, 0))
        print(fetch_user(sys.argv[2]))
    except:
        pass


if __name__ == "__main__":
    main()
