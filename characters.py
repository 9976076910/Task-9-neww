import re


def main():
    password = 'Hike@123'
    regular = "^(?=.*[a-z])(?=.*[A-Z])(?=)(?=.*[@$!%*#?&])[A-Za-z@$!#%*?&]{6,20}$"

    # compiling regex
    pat = re.compile(regular)

    # searching regex
    mat = re.search(pat, password)

    # validating conditions
    if mat:
        print("Password is valid.")
    else:
        print("Password invalid !!")


# Driver Code
if __name__ == '__main__':
    main()
