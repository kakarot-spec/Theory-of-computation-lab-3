#Write a program to implement a Turing  Machine for wcw where w ∈ {a,b}*. 
def print_tape_stack(tape, head, stack):
    tape_str = ' '.join(tape)
    head_str = '  ' * head + '^'
    print(f"Tape: {tape_str}")
    print(f"      {head_str}")
    print(f"Stack: {stack}\n")

def wcw_stack_tm(input_str):
    tape = list(input_str)
    if tape.count('c') != 1:
        print("Input must contain exactly one 'c' → reject")
        return False

    stack = []
    head = 0
    step = 1

    print("Initial Tape:")
    print_tape_stack(tape, head, stack)

    # Step 1: Push symbols before 'c' onto stack
    while head < len(tape) and tape[head] != 'c':
        stack.append(tape[head])
        print(f"Step {step}: Pushed '{tape[head]}' to stack")
        head += 1
        step += 1
        print_tape_stack(tape, head, stack)

    # Step 2: Skip 'c'
    if head < len(tape) and tape[head] == 'c':
        print(f"Step {step}: Skipping 'c'")
        head += 1
        step += 1
        print_tape_stack(tape, head, stack)

    # Step 3: Match remaining symbols with stack
    while head < len(tape):
        if not stack:
            print("Stack empty before finishing → reject")
            return False
        top = stack.pop()
        print(f"Step {step}: Popped '{top}' from stack, comparing with '{tape[head]}'")
        if tape[head] != top:
            print("Mismatch → reject")
            return False
        head += 1
        step += 1
        print_tape_stack(tape, min(head, len(tape)-1), stack)

    if stack:
        print("Stack not empty after processing → reject")
        return False

    print("Stack empty and all symbols matched → accept")
    return True


# --- Driver Program ---
while True:
    s = input("\nEnter a string over {a,b}* with a single 'c' in the middle: ").strip()
    if set(s) - {"a", "b", "c"}:
        print("Invalid input! Only 'a', 'b', and 'c' allowed.")
        continue

    accepted = wcw_stack_tm(s)
    print(f"\nResult: {'ACCEPT' if accepted else 'REJECT'}")

    cont = input("\nTry another? (y/n): ").strip().lower()
    if cont != 'y':
        break
