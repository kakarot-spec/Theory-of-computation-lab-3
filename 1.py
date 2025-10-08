# Write a program to implement a Turing  Machine for anbncn where n>=1. 

def tm_anbncn_stack_record(input_string):
    stack = []  # Initial empty stack
    n = len(input_string)

    # Check for invalid characters first
    if any(ch not in 'abc' for ch in input_string):
        print("Invalid character detected. Rejecting.")
        print("Final Stack (rejected):", stack)
        return False

    print("Initial Stack:", stack)

    # Count a's
    count_a = 0
    i = 0
    while i < n and input_string[i] == 'a':
        stack.append('a')
        count_a += 1
        i += 1
    print(f"Counted a's: {count_a}, Stack remains:", stack)

    # Count b's
    count_b = 0
    while i < n and input_string[i] == 'b':
        stack.append('b')
        count_b += 1
        i += 1
    print(f"Counted b's: {count_b}, Stack remains:", stack)

    # Count c's
    count_c = 0
    while i < n and input_string[i] == 'c':
        stack.append('c')
        count_c += 1
        i += 1
    print(f"Counted c's: {count_c}, Stack remains:", stack)

    # Final check
    if count_a == count_b == count_c >= 1 and i == n:
        print("Final Stack:", stack)
        return True
    else:
        print("Final Stack (rejected):", stack)
        return False


if __name__ == "__main__":
    while True:
        s = input("\nEnter a string of a^n b^n c^n (n>=1): ").strip()
        result = tm_anbncn_stack_record(s)
        print(f"\nFinal result: {'ACCEPT' if result else 'REJECT'}")

        choice = input("\nTry another? (y/n): ").strip().lower()
        if choice != 'y':
            break
