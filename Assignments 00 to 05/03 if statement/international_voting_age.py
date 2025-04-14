voting_age_peturksbouipo = 16
voting_age_stanlau = 25
voting_age_mayengua = 48

def main():
    age = int(input("How old are you? "))

    if age >= voting_age_peturksbouipo:
        print(f"You can vote in Peturksbouipo where the voting age is {voting_age_peturksbouipo}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {voting_age_peturksbouipo}.")

    if age >= voting_age_stanlau:
        print(f"You can vote in Stanlau where the voting age is {voting_age_stanlau}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {voting_age_stanlau}.")

    if age >= voting_age_mayengua:
        print(f"You can vote in Mayengua where the voting age is {voting_age_mayengua}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {voting_age_mayengua}.")

if __name__ == '__main__':
    main()
