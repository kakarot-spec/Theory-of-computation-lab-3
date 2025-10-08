# Write  a  program  to  implement  a  Turing  Machine  for  odd  length  palindrome  over  Σ  = {a,b}.

def tm_odd_palindrome_stack_simple(input_string):
    n = len(input_string)
    stack = []

    # Invalid characters check
    if any(ch not in 'ab' for ch in input_string):
        print("Invalid character detected. Rejecting.")
        print("Final Stack (rejected):", stack)
        return False

    if n % 2 == 0:
        print("Even length input. Rejecting.")
        print("Final Stack (rejected):", stack)
        return False

    print("Initial Stack:", stack)
    mid = n // 2
    pointer = 0

    # Step 1: Push first half onto stack
    while pointer < mid:
        stack.append(input_string[pointer])
        pointer += 1
        print("Stack after push:", stack)

    # Step 2: Skip middle character
    print(f"Skipping middle character '{input_string[mid]}'")
    pointer += 1

    # Step 3: Match second half
    while pointer < n:
        top = stack.pop() if stack else None
        print(f"Popped '{top}', comparing with '{input_string[pointer]}'")
        if top != input_string[pointer]:
            print("Mismatch. Rejecting.")
            print("Final Stack (rejected):", stack)
            return False
        pointer += 1
        print("Stack now:", stack)

    print("Final Stack (empty, accepted):", stack)
    return True


if __name__ == "__main__":
    while True:
        s = input("\nEnter an odd-length palindrome over {a,b}: ").strip()
        result = tm_odd_palindrome_stack_simple(s)
        print(f"\nFinal result: {'ACCEPT' if result else 'REJECT'}")

        choice = input("\nTry another? (y/n): ").strip().lower()
        if choice != 'y':
            break
