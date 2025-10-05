def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

nums = list(map(int,input().split()))
print(multiply_list(nums))