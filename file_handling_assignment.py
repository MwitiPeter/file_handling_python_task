# file_handling_assignment.py

# Step 1: Write to the file (initial content) with error handling
try:
    file_new = open("my_file.txt", "w")

    # Writing multiple lines to the file
    file_new.write("\nhello ")
    file_new.write("\niam ")
    file_new.write(str(20))  # Converting number to string before writing

    file_new.close()  # Closing the file after writing

except PermissionError:
    print("Error: You don't have permission to write to 'my_file.txt'.")
except Exception as e:
    print(f"An error occurred: {e}")

# Step 2: Append to the file with error handling
try:
    with open("my_file.txt", "a") as file:
        # Appending additional lines
        file.write("\nThis is an appended line 1.")
        file.write("\nThis is an appended line 2.")
        file.write("\nThis is an appended line 3.")

except FileNotFoundError:
    print("Error: 'my_file.txt' was not found.")
except PermissionError:
    print("Error: You don't have permission to append to 'my_file.txt'.")
except Exception as e:
    print(f"An error occurred: {e}")

# Step 3: Read from the file with error handling
try:
    with open("my_file.txt", "r") as file:
        # Reading the content of the file
        content = file.read()

    # Displaying the content on the console
    print("Contents of 'my_file.txt':")
    print(content)

except FileNotFoundError:
    print("Error: 'my_file.txt' was not found.")
except PermissionError:
    print("Error: You don't have permission to read 'my_file.txt'.")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("File handling operations completed.")
