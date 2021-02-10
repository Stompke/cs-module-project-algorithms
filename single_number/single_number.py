'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    arr.sort()
    i = 0
    while i <= len(arr):
        print('\nhere')
        print(arr[i])
        print(arr[i+1])
        if(arr[i+1] != arr[i]):
            print('doesnt match!')
            return arr[i]
        i += 2


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 9, 0, 0,2]

    print(f"The odd-number-out is {single_number(arr)}")