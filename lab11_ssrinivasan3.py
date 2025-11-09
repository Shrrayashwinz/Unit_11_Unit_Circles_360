"""
Program Name: lab11_ssrinivasan3.py

Author: Shrrayash Srinivasan

Purpose: 1.	Create a function that takes a numeric input representing the degrees of a rotation and adjusts it to remove 
unnecessary rotations if more than a full rotation is entered.  For example, an input of 100 should just return 100, but an 
input of 460 should return 100 to eliminate the full 360-degree rotation

Date: November 4, 2025

"""

def degree_rotation(degrees):

    try: 
        degrees = int(degrees)
        return degrees % 360
    
    except (TypeError, ValueError):
        print("\nIt needs to be numerical\n")
        return None

def main():
    print("You are now in the rotation calendar. Let's get started!")
    while True:
        number_str = (input("Enter a number:"))
        degrees = degree_rotation(number_str)

        number = int(number_str)


        if number < 360 and number >= 0:
            print("This number:", number, "is within the 360 degrees range; no need to simplify it!")
        
        elif number >= 360 or number < 0:
            print("This number:", number, "is equalvalent to", degrees, "when the rotations are used")   
            
        else:
            print("Please give an actual number.")

if __name__ == "__main__": 
    main()



        




    




