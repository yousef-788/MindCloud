# Keep asking until N and M are in the correct range
while True:
    n, m = map(int, input("Enter N and M (1-99): ").split())
    if 0 < n < 100 and 0 < m < 100:
        break
    print("Error: N and M must be between 1 and 99.")

# Read the matrix rows
matrix = [input() for _ in range(n)]

# Read characters column by column into one string
text = ""
for col in range(m):
    for row in range(n):
        text += matrix[row][col]

# Replace symbols between letters/numbers with a space
decoded = ""
for i in range(len(text)):
    if not text[i].isalnum():
        if i > 0 and i < len(text) - 1 and text[i-1].isalnum() and text[i+1].isalnum():
            decoded += " "
    else:
        decoded += text[i]

print(decoded)
