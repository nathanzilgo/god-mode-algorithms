# /*
#       * In this problem you have a nested array of strings.
#       * Lists of strings can be nested to an arbitrary depth.
#       * Print each element contained in the list, including all elements in nested lists.
#       * Each element should be printed on a new line with the element's index at the beginning of the line.
#       *
#       * Ex:
#       * 0: 1
#       * 1: 2
#       * 2: 3
#       * 3.0: blue
#       * 3.1: yellow
#       * 3.2: red
#       * 4: 5
#       * 5.2.0: biplane
#       * etc...
#       */

nested_array = [
    "1", "2", "3",
    ["blue", "yellow", "red"],
    "5",
    [
        "helicoptor", "blimp",
        [
            "biplane", "seaplane",
            ["B-52", "F-35", "A-12"]
        ]
    ],
    "7"
]

def solution():
    for x in range(len(nested_array)):
        if type(nested_array[x]) == list:
            aux(nested_array[x], str(x))
        else:
            print(f"{x}: {nested_array[x]}")

def aux(arr, prefix=""):
    for i, val in enumerate(arr):
        if type(val) == list:
            aux(val, f"{prefix}.{i}")
        else:
            print(f"{prefix}.{i}: {val}")


if __name__ == "__main__":
    solution()
