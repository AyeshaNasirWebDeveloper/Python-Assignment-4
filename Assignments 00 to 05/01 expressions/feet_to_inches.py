INCHES_IN_FOOT = 12  # Conversion factor. There are 12 inches for 1 foot.

def main():
    feet = float(input("Enter number of feet: ")) 
    inches = feet * INCHES_IN_FOOT  
    print("That is", inches, "inches!")

if __name__ == '__main__':
    main()
