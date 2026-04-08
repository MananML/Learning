
user_input = input("File name: ").lower().strip()

if user_input.count(".") == 1:
    file_name, extension = user_input.split(".")

elif user_input.count(".") > 1:
    extension = user_input.split(".")[-1]

else:
    extension = user_input

match extension:
    
    case "gif" | "png":
        print(f"image/{extension}")

    case "jpg" | "jpeg":
        print("image/jpeg")

    case "pdf" | "zip":
        print(f"application/{extension}")
    
    case "txt":
        print("text/plain") 

    case _:
        print("application/octet-stream")