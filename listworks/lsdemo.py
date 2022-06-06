# employee_names=["rahul","sabir","surej","ratheesh"]

# for name in employee_names:
#     print(name)
#
# for i in range(0,len(employee_names)):
#     print(employee_names[i])


numbers=[12,13,14,15,16,17,18]



# sum=0
# for n in numbers:
#     sum+=n
# print(sum)




# print(sum(numbers))

# for num in numbers:
#     if num>15:
#         print(num+1)
#     elif num<15:
#         print(num-1)
#     elif num==15:
#         print(num)

# print count of numbers where numbers in range of 14-18
count=0
# for num in numbers:
#     if num >=14 and num<=18:
#        count+=1
# print(count)
#
#

for num in numbers:
    if num in range(14,19):
        count+=1
print(count)


numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]

#
# p_count_sum
# n_count_sum

# p_count=0
# z_count=0
# n_count=0
#
# for n in numbers:
#     if n >0:
#         p_count+=1
#     elif n <0:
#         n_count+=1
#     elif n==0:
#         z_count+=1
# print(f"+ve count{p_count},neg count {n_count},zerocount{z_count}")
#




# compnay="luminar"
# location="kakkanad"
# status="open"
# closes=9
# luminar located at kakkanad current status open will close by 9
# print(compnay+"loacted at"+location+"current status "+status+"will close by"+closes)
# print(f"{compnay} located at {location} current status {status} will close by {closes}")