'''
Input: a List of integers
Returns: a List of integers
'''

'''
Questions:
    -How do I isolate each number?
    -How do you multiply each number by the rest?

Process:
    -Loop through list
    -Multiple first index by remaining numbers
'''
def product_of_all_other_numbers(arr):
    list = []
    for i in range(len(arr)):
        list.append(i)
        for j in range(len(arr)):
            list.append(j * i)
    
    return list

arr = [1, 2, 3, 4, 5]

print(product_of_all_other_numbers(arr))
# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     # arr = [1, 2, 3, 4, 5]
#     arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

#     print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
