'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

'''
Questions:
    -How do we add integers to the list twice
    -How do you repeat process for all but one?

Process:
    -Create empty list
    -Loop through range and add each number to list
    -Repeat for all but one
'''


def single_number(arr):
    list = []
    for i in range(5):
        list.append(i)

    list = list * 2
    return list[:-1]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")