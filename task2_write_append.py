# Take user input
user_input = input("Enter a value: ")

# Write data to file
with open("output.txt", "w") as file:
    file.write("User entered: " + user_input + "\n")

# Append additional data
with open("output.txt", "a") as file:
    file.write("This is appended data.\n")

# Read and display final content
with open("output.txt", "r") as file:
    print("\nFinal content of output.txt:")
    print(file.read())
