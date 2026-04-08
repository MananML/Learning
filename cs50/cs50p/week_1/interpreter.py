
question = input("Expression: ")
x, y, z = question.split()
x, z = int(x), int(z)
add, sub, mult, div = x + z, x - z, x * z, x / z

match y:
    case "+":
        print(f"{add:.1f}")
    
    case "-":
        print(f"{sub:.1f}")

    case "*":
        print(f"{mult:.1f}")

    case "/":
        print(f"{div:.1f}")