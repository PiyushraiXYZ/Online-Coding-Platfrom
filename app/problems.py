PROBLEMS = [

# ==========================================

# BASIC QUESTIONS (1-10)

# ==========================================

{
"id": 1,
"level": "Basic",
"title": "Print Hello World",
"description": "Print Hello World",
"test_cases": [{"input": "", "output": "Hello World"}]
},

{
"id": 2,
"level": "Basic",
"title": "Add Two Numbers",
"description": "Input two integers and print their sum.",
"test_cases": [
{"input": "2 3", "output": "5"},
{"input": "10 20", "output": "30"}
]
},

{
"id": 3,
"level": "Basic",
"title": "Subtract Two Numbers",
"description": "Input two integers and print their difference.",
"test_cases": [
{"input": "10 5", "output": "5"},
{"input": "20 8", "output": "12"}
]
},

{
"id": 4,
"level": "Basic",
"title": "Multiply Two Numbers",
"description": "Input two integers and print their product.",
"test_cases": [
{"input": "2 5", "output": "10"},
{"input": "7 8", "output": "56"}
]
},

{
"id": 5,
"level": "Basic",
"title": "Even Or Odd",
"description": "Determine whether a number is even or odd.",
"test_cases": [
{"input": "4", "output": "Even"},
{"input": "7", "output": "Odd"}
]
},

{
"id": 6,
"level": "Basic",
"title": "Find Largest Number",
"description": "Find the largest among three numbers.",
"test_cases": [
{"input": "5 8 3", "output": "8"}
]
},

{
"id": 7,
"level": "Basic",
"title": "Leap Year",
"description": "Check whether a year is leap year.",
"test_cases": [
{"input": "2024", "output": "Leap Year"},
{"input": "2023", "output": "Not Leap Year"}
]
},

{
"id": 8,
"level": "Basic",
"title": "Factorial",
"description": "Print factorial of a number.",
"test_cases": [
{"input": "5", "output": "120"}
]
},

{
"id": 9,
"level": "Basic",
"title": "Reverse Number",
"description": "Reverse the digits of a number.",
"test_cases": [
{"input": "1234", "output": "4321"}
]
},

{
"id": 10,
"level": "Basic",
"title": "Sum Of Digits",
"description": "Calculate sum of digits.",
"test_cases": [
{"input": "123", "output": "6"}
]
},

# ==========================================

# INTERMEDIATE QUESTIONS (11-20)

# ==========================================

{
"id": 11,
"level": "Intermediate",
"title": "Palindrome Number",
"description": "Check if a number is palindrome.",
"test_cases": [
{"input": "121", "output": "True"},
{"input": "123", "output": "False"}
]
},

{
"id": 12,
"level": "Intermediate",
"title": "Prime Number",
"description": "Check whether a number is prime.",
"test_cases": [
{"input": "13", "output": "Prime"},
{"input": "12", "output": "Not Prime"}
]
},

{
"id": 13,
"level": "Intermediate",
"title": "Count Vowels",
"description": "Count vowels in a string.",
"test_cases": [
{"input": "hello", "output": "2"}
]
},

{
"id": 14,
"level": "Intermediate",
"title": "Anagram Check",
"description": "Check if two strings are anagrams.",
"test_cases": [
{"input": "listen silent", "output": "True"}
]
},

{
"id": 15,
"level": "Intermediate",
"title": "GCD Of Two Numbers",
"description": "Find GCD.",
"test_cases": [
{"input": "12 18", "output": "6"}
]
},

{
"id": 16,
"level": "Intermediate",
"title": "LCM Of Two Numbers",
"description": "Find LCM.",
"test_cases": [
{"input": "12 18", "output": "36"}
]
},

{
"id": 17,
"level": "Intermediate",
"title": "Fibonacci Series",
"description": "Print Fibonacci sequence up to N terms.",
"test_cases": [
{"input": "5", "output": "0 1 1 2 3"}
]
},

{
"id": 18,
"level": "Intermediate",
"title": "Frequency Of Characters",
"description": "Count character frequency.",
"test_cases": [
{"input": "hello", "output": "h:1 e:1 l:2 o:1"}
]
},

{
"id": 19,
"level": "Intermediate",
"title": "Matrix Addition",
"description": "Add two matrices.",
"test_cases": []
},

{
"id": 20,
"level": "Intermediate",
"title": "Pattern Printing",
"description": "Print star pattern.",
"test_cases": []
},

# ==========================================

# DSA QUESTIONS (21-30)

# ==========================================

{
  "id": 21,
  "level": "DSA",
  "title": "Two Sum",
  "description": "Find indices of two numbers whose sum equals target.",
  "test_cases": [
    {
      "input": "[2,7,11,15]\n9",
      "output": "[0,1]"
    },
    {
      "input": "[3,2,4]\n6",
      "output": "[1,2]"
    },
    {
      "input": "[3,3]\n6",
      "output": "[0,1]"
    }
  ]
},

{
  "id": 22,
  "level": "DSA",
  "title": "Binary Search",
  "description": "Implement Binary Search.",
  "test_cases": [
    {
      "input": "[1,2,3,4,5]\n3",
      "output": "2"
    },
    {
      "input": "[1,2,3,4,5]\n6",
      "output": "-1"
    },
    {
      "input": "[10,20,30,40,50]\n10",
      "output": "0"
    }
  ]
},

{
  "id": 23,
  "level": "DSA",
  "title": "Maximum Subarray",
  "description": "Find maximum subarray sum.",
  "test_cases": [
    {
      "input": "[-2,1,-3,4,-1,2,1,-5,4]",
      "output": "6"
    },
    {
      "input": "[1]",
      "output": "1"
    },
    {
      "input": "[5,4,-1,7,8]",
      "output": "23"
    }
  ]
},

{
  "id": 24,
  "level": "DSA",
  "title": "Valid Parentheses",
  "description": "Check balanced brackets.",
  "test_cases": [
    {
      "input": "()",
      "output": "true"
    },
    {
      "input": "()[]{}",
      "output": "true"
    },
    {
      "input": "(]",
      "output": "false"
    },
    {
      "input": "([)]",
      "output": "false"
    },
    {
      "input": "{[]}",
      "output": "true"
    }
  ]
},

{
  "id": 25,
  "level": "DSA",
  "title": "Merge Sorted Arrays",
  "description": "Merge two sorted arrays.",
  "test_cases": [
    {
      "input": "[1,2,3]\n[2,5,6]",
      "output": "[1,2,2,3,5,6]"
    },
    {
      "input": "[1]\n[]",
      "output": "[1]"
    },
    {
      "input": "[]\n[1]",
      "output": "[1]"
    },
    {
      "input": "[1,4,7]\n[2,3,6]",
      "output": "[1,2,3,4,6,7]"
    }
  ]
}


]


{
"id": 26,
"level": "DSA",
"title": "Linked List Traversal",
"description": "Traverse a linked list.",
"test_cases": [
    {"input": "1 2 3 4", "output": "1 2 3 4"},
    {"input": "10 20", "output": "10 20"},
    {"input": "5", "output": "5"}
]
},

{
"id": 27,
"level": "DSA",
"title": "Reverse Linked List",
"description": "Reverse a linked list.",
"test_cases": [
    {"input": "1 2 3 4", "output": "4 3 2 1"},
    {"input": "10 20", "output": "20 10"},
    {"input": "5", "output": "5"}
]
},

{
"id": 28,
"level": "DSA",
"title": "Tree Traversal",
"description": "Perform inorder traversal.",
"test_cases": [
    {"input": "1 2 3", "output": "2 1 3"},
    {"input": "4 2 6 1 3 5 7", "output": "1 2 3 4 5 6 7"},
    {"input": "1", "output": "1"}
]
},

{
"id": 29,
"level": "DSA",
"title": "Detect Cycle In Graph",
"description": "Check if graph contains cycle.",
"test_cases": [
    {"input": "3\n0 1\n1 2\n2 0", "output": "True"},
    {"input": "3\n0 1\n1 2", "output": "False"},
    {"input": "4\n0 1\n1 2\n2 3\n3 0", "output": "True"}
]
},

{
"id": 30,
"level": "DSA",
"title": "Shortest Path",
"description": "Implement Dijkstra Algorithm.",
"test_cases": [
    {"input": "5 6\n0 1 4\n0 2 1\n2 1 2\n1 3 1\n2 3 5\n3 4 3\n0", "output": "0 3 1 4 7"},
    {"input": "3 3\n0 1 1\n1 2 2\n0 2 5\n0", "output": "0 1 3"},
    {"input": "4 4\n0 1 10\n0 2 6\n2 3 2\n1 3 4\n0", "output": "0 10 6 8"}
]
}
