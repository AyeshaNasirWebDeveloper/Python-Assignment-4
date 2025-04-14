ADULT_AGE = 18

def check_adult_status(age):
    if age >= ADULT_AGE:
        return True
    return False

def main():
    person_age = int(input("How old is this person?: "))
    is_adult = check_adult_status(person_age)
    print(is_adult)

if __name__ == "__main__":
    main()
