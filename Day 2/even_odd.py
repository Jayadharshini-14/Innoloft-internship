def sort_numbers(numbers):
    even=[]
    odd=[]
    for num in numbers:
        if num % 2 ==0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd
numbers=[12,7,5,18,23,10,25,8,16,31]
even_numbers, odd_numbers=sort_numbers(numbers)

print("Original list:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)