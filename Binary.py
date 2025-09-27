def process_to10(the_base, num):
    # Convert each digit and calculate the base-10 value
    exponent = len(num) - 1
    total = 0
    for i in range(len(num)):
        # Calculate without modifying the original list
        total += int(num[i]) * the_base**exponent
        exponent -= 1
    return total

def processtranslate(wanted_base, num):
    """Convert base 10 integer `num` into list of digits in base `wanted_base`."""
    if num == 0:
        return [0]
    finalnum = []
    while num > 0:
        remainder = num % wanted_base
        finalnum.insert(0, remainder)  # prepend digit
        num //= wanted_base
    return finalnum

def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    elif output_base < 2:
        raise ValueError("output base must be >= 2")
    for d in digits:
        if not (0 <= d < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")
    
    # Convert digits to base-10
    middle = process_to10(input_base, digits)
    # Convert base-10 to output base
    return processtranslate(output_base, middle)

input_base = int(input("Enter input base: "))
digits_input = input("Enter digits: ")

if ',' in digits_input:
    digits = [int(d.strip()) for d in digits_input.split(',')]
else:
    digits = [int(d) for d in digits_input.strip()]

output_base = int(input("Enter output base: "))
print(rebase(input_base, digits, output_base))