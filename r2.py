#Python program to convert an integer to a string in any base.
def convert_to_base(n, base):
    if n == 0:
        return ''
    else:
        
        return convert_to_base(n // base, base) + str(n % base)

def main():
    
    num = int(input("Enter an integer: "))
    target_base = int(input("Enter the base to convert to: "))

    
    result = convert_to_base(num, target_base)

    
    print(f"The integer {num} in base {target_base} is: {result}")

if __name__ == "__main__":
    main()
