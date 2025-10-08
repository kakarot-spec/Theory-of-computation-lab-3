#Write a program to implement a Turing  Machine for string of odd length over Σ = {0,1}
def print_tape_stack(tape, head, stack):
    """Print tape with head and stack"""
    tape_str = ' '.join(tape)
    head_str = '  ' * head + '^'
    print(f"Tape: {tape_str}")
    print(f"      {head_str}")
    print(f"Stack: {stack}\n")

def odd_length_stack_tm(input_str):
    tape = list(input_str)
    head = 0
    symbols = {"0", "1"}
    stack = []
    step = 1

    # Input validation
    if set(tape) - symbols:
        print("Invalid input! Only '0' and '1' allowed.")
        return False

    print("Initial Tape:")
    print_tape_stack(tape, head, stack)

    # Move head across the tape, push symbols onto stack
    while head < len(tape):
        print(f"Step {step}: Reading '{tape[head]}' at position {head}")
        stack.append(tape[head])
        print(f"Pushed '{tape[head]}' to stack")
        head += 1
        step += 1
        print_tape_stack(tape, min(head, len(tape)-1), stack)

    # Check if the string length is odd
    if len(tape) % 2 != 0:
        print("Length is odd → accept")
        return True
    else:
        print("Length is even → reject")
        return False


# --- Driver Program ---
while True:
    s = input("\nEnter a string over {0,1}: ").strip()
    accepted = odd_length_stack_tm(s)
    print(f"\nResult: {'ACCEPT' if accepted else 'REJECT'}")

    cont = input("\nTry another? (y/n): ").strip().lower()
    if cont != 'y':
        break
