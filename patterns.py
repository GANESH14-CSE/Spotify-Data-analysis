# -------------------------------------
# 🔸 1. Ascending Number Triangle
# -------------------------------------
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# -------------------------------------
# 🔸 2. Descending Number Triangle
# -------------------------------------
n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# -------------------------------------
# 🔸 3. Right-Shifted Number Pattern
# -------------------------------------
n = 5
for i in range(0, n):
    print(" " * i, end="")
    for j in range(i+1, n+1):
        print(j, end="")
    print()

# -------------------------------------
# 🔸 4. Centered Reverse Number Triangle
# -------------------------------------
n = 5
for i in range(1, n+1):
    for space in range(n - i):
        print(" ", end="")
    for num in range(i, 0, -1):
        print(num, end="")
    print()

# -------------------------------------
# 🔸 5. Reverse Left-Aligned Number Triangle
# -------------------------------------
n = 5
for i in range(n):
    p = 1
    for j in range(n - i):
        print(p, end="")
        p += 1
    print()

# -------------------------------------
# 🔸 6. Diagonal Increasing Start Number Pattern
# -------------------------------------
n = 5
for i in range(n):
    for j in range(1 + 1, i + n):
        print(j, end=' ')
    print()

# -------------------------------------
# 🔸 7. Binary Alternating Triangle (Left-Aligned)
# -------------------------------------
n = 5
for i in range(1, n+1):
    for j in range(i):
        print((j+1)%2, end='')
    print()

# -------------------------------------
# 🔸 8. Alternating Binary Row Pattern (Based on Row Index)
# -------------------------------------
n = 5
for i in range(1, n+1):
    if i %2==0:
        print('0' * i)
    else:
        print('1' * i)

# -------------------------------------
# 🔸 9. Curly Brace Pattern (Custom Symbol)
# -------------------------------------
n = 2
for i in range(1, n+1):
    if i==1:
        print("{}")
    elif i==2:
        print("{} {{}}")

# -------------------------------------
# 🔸 10. Alphabet Triangle (Ascending Left-Aligned)
# -------------------------------------
n = 5
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j), end='')
    print()

# -------------------------------------
# 🔸 11. Alphabet Reverse Triangle
# -------------------------------------
n = 5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(chr(65+j-1), end='')
    print()

# -------------------------------------
# 🔸 12. Right-Angled Star Triangle (Increasing)
# -------------------------------------
n = 5
for i in range(1,n+1):
    print('*' * i)

# -------------------------------------
# 🔸 13. Right-Angled Star Triangle (Decreasing)
# -------------------------------------
n = 5
for i in range(n,0,-1):
    print('*' * i)

# -------------------------------------
# 🔸 14. Right-Aligned Star Triangle
# -------------------------------------
n = 5
for i in range(1,n+1):
    print(' ' * (n - i) + '*' * i)

# -------------------------------------
# 🔸 15. Left-Aligned Star Triangle with Spaces
# -------------------------------------
n = 5
for i in range(n,0,-1):
    print(' ' * (n-i) + '*' * i)

# -------------------------------------
# 🔸 16. Hourglass Star Pattern
# -------------------------------------
n = 5
for i in range(n,0,-1):
    print(' ' *(n-i) + '*' * (2*i-1))
for i in range(2, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

# -------------------------------------
# 🔸 17. Lower Half of Diamond / Pyramid Only
# -------------------------------------
n = 5
for i in range(2,n+1):
    print(' ' * (n-i) + '*' *(2*i-1))

# -------------------------------------
# 🔸 18. Full Diamond Star Pattern
# -------------------------------------
n = 5
for i in range(1,n+1):
    print(' ' * (n-i) + '*' * (2*i-1))
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

# -------------------------------------
# 🔸 19. Binary Alternating Triangle (Same as 7)
# -------------------------------------
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j % 2, end='')
    print()# Spotify-Data-analysis
