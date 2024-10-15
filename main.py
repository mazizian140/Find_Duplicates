'''
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is
the smallest in lexicographical order
 among all possible results.
'''


def removeDuplicateLetters(s: str) -> str:
    last_occurrence = {char: idx for idx, char in enumerate(s)}  # Last occurrence of each character
    stack = []  # Stack to build the result
    seen = set()  # Set to track characters in the result

    for i, char in enumerate(s):
        if char in seen:
            continue  # Skip if the character is already in the result

        # Remove characters from the stack if the current character is smaller
        # and the character at the top of the stack appears later in the string
        while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
            seen.remove(stack.pop())  # Remove from seen and pop from stack

        stack.append(char)  # Add current character to the stack
        seen.add(char)  # Mark as seen

    return ''.join(stack)  # Return the result as a string


def main():
    # Input string example
    s = input("Enter a string: ")

    # Call the function and print the result
    result = removeDuplicateLetters(s)
    print("Result after removing duplicate letters:", result)


if __name__ == "__main__":
    main()