#Write  a  program  to  implement  a  Turing  Machine  for  even  length  palindrome  over  Σ  = {a,b}. 
def even_palindrome_stack_tm(input_str):
    n = len(input_str)
    
    # Check for invalid characters
    if set(input_str) - {"a", "b"}:
        print("Invalid input! Only 'a' and 'b' allowed.")
        return False
    
    # Check even length
    if n % 2 != 0:
        print("Input length is odd → reject")
        return False

    stack = []
    mid = n // 2
    print(f"Input string: {input_str}")
    print(f"Stack initially: {stack}\n")

    # Step 1: Push first half onto stack
    for i in range(mid):
        stack.append(input_str[i])
        print(f"Pushed '{input_str[i]}' onto stack → {stack}")

    # Step 2: Match second half with stack
    for i in range(mid, n):
        if not stack:
            print("Stack empty before matching finished → reject")
            return False
        top = stack.pop()
        print(f"Popped '{top}' from stack, comparing with '{input_str[i]}'")
        if top != input_str[i]:
            print("Mismatch → reject")
            return False
        print(f"Stack now: {stack}")

    print("Stack empty, all symbols matched → accept")
    return True


# --- Driver Program ---
while True:
    s = input("\nEnter an even-length palindrome over {a,b}: ").strip()
    accepted = even_palindrome_stack_tm(s)
    print(f"\nResult: {'ACCEPT' if accepted else 'REJECT'}")

    cont = input("\nTry another? (y/n): ").strip().lower()
    if cont != 'y':
        break
