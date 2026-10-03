students = ["yanet", "nati", "Melat", "rediet"]
for i in range(len(students)):
    print(i+1, students[i])
for i, student in enumerate(students):
    print(i+1, student)

students = [["student1", 20], ["student 2": 21], ["student3 ": 22]]
numbers = [1, 2,3,4,5]
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares)

number = int(input("how many numbers u want to enter: "))
num = []
for i in range(number):
    no = int(input(f"enter the number {i+1}"))
    num.append(no)
print(num)
print(f"the greatest number is ",max(num))
print(f"the smallest number is ",min(num))
even_num, odd_num =[],[]
for nums in num:
    if nums % 2 == 0:
        even_num.append(nums)
    else:
        odd_num.append(nums)
print(f"The even numbers u entered", even_num)
print(f"the odd numbers u entered", odd_num)



item = 5
shopping_cart = []
for i in range(item):
    items = input("enter the item u want to buy: ")
    shopping_cart.append(items)
print(shopping_cart)
rem_oval = input("Which item u want to remove: ")
shopping_cart.remove(rem_oval)
print(shopping_cart)
itemsadded = input("add another item u want to buy:")
shopping_cart.append(itemsadded)
print(shopping_cart)


num = int(input("how many scores: "))
scores = []
for i in range(num):
    score = int(input(f"enter score {i+1}"))
    scores.append(score)
print(scores)
total_score = sum(scores)
print(total_score)
avg_score = total_score/len(scores)
print(avg_score)
print(max(scores))
print(min(scores))
for score in scores:
    count_high = 0
    count_low= 0
    if score >= 50:
        count_high +=1
    else:
        count_low += 1
print(f"students that score above 50", count_high)   
print(f"students that score below 50", count_low) 


numbers = [4,7,4,2,7,9,2,1,9,5]
new_list = []
for num in numbers:
    if num not in new_list:
        new_list.append(num)
print(new_list)


