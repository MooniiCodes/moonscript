import base64
import sys
import os



print("Moonscript Script compiler")

if sys.argv[1] == "-c":
    with open(sys.argv[2], "rb") as file:
        file_content = file.read()
    encoded_content = base64.b64encode(file_content)
    encoded_string = encoded_content.decode('utf-8')
    print("File data: " + encoded_string)
    file_path = sys.argv[3]
    try:
        with open(file_path, 'x') as file:
            file.write(encoded_string)
        print(f"Compiled {sys.argv[2]} into {sys.argv[3]}.")
    except FileExistsError:
        print(f"Script '{file_path}' already exists.")

elif sys.argv[1] == "-dc":
    with open(sys.argv[2], "rb") as file:
        file_content = file.read()
    decoded_content = base64.b64decode(file_content)
    decoded_string = decoded_content.decode('utf-8')
    print("File data: " + decoded_string)
    file_path = sys.argv[3]
    try:
        with open(file_path, 'x') as file:
            file.write(decoded_string)
        print(f"Decompiled {sys.argv[2]} into {sys.argv[3]}.")
    except FileExistsError:
        print(f"Script '{file_path}' already exists.")