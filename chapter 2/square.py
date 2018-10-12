def square(nums):
    for num in nums:
        yield (num * num)
 

my_nums = square([1, 2, 3, 4, 5])
print (next(my_nums))
print (next(my_nums))
print (next(my_nums))
print (next(my_nums))
print (next(my_nums))


# print next(square(nums)) 
# print next(square(nums))
# print next(square(nums))
# print next(square(nums))
# print next(square(nums))

