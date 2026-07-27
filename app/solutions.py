SOLUTIONS = [

# ==========================================
# BASIC QUESTIONS (1-10)
# ==========================================

{
    "problem_id": 1,
    "language": "python",
    "code": 'print("Hello World")'
},

{
    "problem_id": 2,
    "language": "python",
    "code": '''
a, b = map(int, input().split())
print(a + b)
'''
},

{
    "problem_id": 3,
    "language": "python",
    "code": '''
a, b = map(int, input().split())
print(a - b)
'''
},

{
    "problem_id": 4,
    "language": "python",
    "code": '''
a, b = map(int, input().split())
print(a * b)
'''
},

{
    "problem_id": 5,
    "language": "python",
    "code": '''
n = int(input())
print("Even" if n % 2 == 0 else "Odd")
'''
},

{
    "problem_id": 6,
    "language": "python",
    "code": '''
a, b, c = map(int, input().split())
print(max(a, b, c))
'''
},

{
    "problem_id": 7,
    "language": "python",
    "code": '''
year = int(input())

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")
'''
},

{
    "problem_id": 8,
    "language": "python",
    "code": '''
n = int(input())

fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)
'''
},

{
    "problem_id": 9,
    "language": "python",
    "code": '''
n = input()
print(n[::-1])
'''
},

{
    "problem_id": 10,
    "language": "python",
    "code": '''
n = input()
print(sum(map(int, n)))
'''
},

# ==========================================
# INTERMEDIATE QUESTIONS (11-20)
# ==========================================

{
    "problem_id": 11,
    "language": "python",
    "code": '''
n = input()
print("True" if n == n[::-1] else "False")
'''
},

{
    "problem_id": 12,
    "language": "python",
    "code": '''
n = int(input())

if n < 2:
    print("Not Prime")
else:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
'''
},

{
    "problem_id": 13,
    "language": "python",
    "code": '''
s = input().lower()

count = 0

for ch in s:
    if ch in "aeiou":
        count += 1

print(count)
'''
},

{
    "problem_id": 14,
    "language": "python",
    "code": '''
a, b = input().split()

print(
    "True"
    if sorted(a) == sorted(b)
    else "False"
)
'''
},

{
    "problem_id": 15,
    "language": "python",
    "code": '''
import math

a, b = map(int, input().split())

print(math.gcd(a, b))
'''
},

{
    "problem_id": 16,
    "language": "python",
    "code": '''
import math

a, b = map(int, input().split())

print((a * b) // math.gcd(a, b))
'''
},

{
    "problem_id": 17,
    "language": "python",
    "code": '''
n = int(input())

a, b = 0, 1

ans = []

for _ in range(n):
    ans.append(str(a))
    a, b = b, a + b

print(" ".join(ans))
'''
},

{
    "problem_id": 18,
    "language": "python",
    "code": '''
from collections import Counter

s = input()

freq = Counter(s)

result = []

for ch in sorted(freq):
    result.append(f"{ch}:{freq[ch]}")

print(" ".join(result))
'''
},

{
    "problem_id": 19,
    "language": "python",
    "code": '''
a1, a2 = map(int, input().split())
a3, a4 = map(int, input().split())

b1, b2 = map(int, input().split())
b3, b4 = map(int, input().split())

print(a1+b1, a2+b2)
print(a3+b3, a4+b4)
'''
},

{
    "problem_id": 20,
    "language": "python",
    "code": '''
n = int(input())

for i in range(1, n+1):
    print("*" * i)
'''
},

# ==========================================
# DSA QUESTIONS (21-30)
# ==========================================


{
    "problem_id": 21,
    "language": "python",
    "code": """
nums = list(map(int, input().split()))
target = int(input())

d = {}

for i, num in enumerate(nums):
    if target - num in d:
        print(d[target-num], i)
        break
    d[num] = i
"""
},

{
    "problem_id": 22,
    "language": "python",
    "code": """
arr = list(map(int, input().split()))
target = int(input())

left, right = 0, len(arr) - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        print(mid)
        break

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1
else:
    print(-1)
"""
},

{
    "problem_id": 23,
    "language": "python",
    "code": """
arr = list(map(int, input().split()))

current = arr[0]
maximum = arr[0]

for num in arr[1:]:
    current = max(num, current + num)
    maximum = max(maximum, current)

print(maximum)
"""
},

{
    "problem_id": 24,
    "language": "python",
    "code": """
s = input()

stack = []
pairs = {')':'(', ']':'[', '}':'{'}

for ch in s:

    if ch in '([{':
        stack.append(ch)

    elif not stack or stack.pop() != pairs[ch]:
        print("False")
        break
else:
    print("True" if not stack else "False")
"""
},

{
    "problem_id": 25,
    "language": "python",
    "code": """
a = list(map(int, input().split()))
b = list(map(int, input().split()))

merged = sorted(a + b)

print(*merged)
"""
},

{
    "problem_id": 26,
    "language": "python",
    "code": """
nums = input().split()

for num in nums:
    print(num, end=" ")
"""
},

{
    "problem_id": 27,
    "language": "python",
    "code": """
nums = input().split()

nums.reverse()

print(*nums)
"""
},

{
    "problem_id": 28,
    "language": "python",
    "code": """
tree = list(map(int, input().split()))

def inorder(index):

    if index >= len(tree):
        return []

    return (
        inorder(2 * index + 1)
        + [tree[index]]
        + inorder(2 * index + 2)
    )

print(*inorder(0))
"""
},

{
    "problem_id": 29,
    "language": "python",
    "code": """
n = int(input())

parent = list(range(n))

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

cycle = False

while True:

    try:
        u, v = map(int, input().split())

        pu = find(u)
        pv = find(v)

        if pu == pv:
            cycle = True

        parent[pu] = pv

    except:
        break

print("True" if cycle else "False")
"""
},

{
    "problem_id": 30,
    "language": "python",
    "code": """
import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))
    graph[v].append((u, w))

source = int(input())

dist = [float('inf')] * n
dist[source] = 0

pq = [(0, source)]

while pq:

    d, node = heapq.heappop(pq)

    if d > dist[node]:
        continue

    for nxt, wt in graph[node]:

        nd = d + wt

        if nd < dist[nxt]:
            dist[nxt] = nd
            heapq.heappush(pq, (nd, nxt))

print(*dist)
"""
}
]