import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    name = sys.argv[1]
    rollno = sys.argv[2]
    print("User provided input value:")
else:
    script_name = sys.argv[0]
    name = "Aditya"
    rollno = "270"
    print("No input given - using default values:")

print("Script Name: ", script_name)
print("Student Name: ", name)
print("Roll NUmber: ", rollno)
