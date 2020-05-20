'''
Input: a List of integers
Returns: a List of integers
'''

'''
Questions:
    -How do you remove items from list?
    -How do you isolate non itegers?

Process:
    -Loop through list
    -remove 0s
'''

def moving_zeroes(arr):
    arr = [x for x in arr if int(x)]

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")