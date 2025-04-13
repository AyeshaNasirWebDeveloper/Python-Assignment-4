import math  # Import the math library so we can use the sqrt function

def main():
    ab = float(input("Enter the length of AB: ")) 
    ac = float(input("Enter the length of AC: "))  

    # Calculate the hypotenuse using the two sides
    bc = math.sqrt(ab**2 + ac**2)  # Applying Pythagorean theorem
    print("The length of BC (the hypotenuse) is: " + str(bc))  

if __name__ == '__main__':
    main()
