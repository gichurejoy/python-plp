def read_and_write_file():
    input_filename = input("Enter the name of the file to read: ")

    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("✅ File read successfully.")

            modified_content = content.upper()

            output_filename = "modified_" + input_filename
            with open(output_filename, 'w') as outfile:
                outfile.write(modified_content)
                print(f"✅ Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    read_and_write_file()
