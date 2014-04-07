__author__ = 'andytertzakian'

##This project sorts a list of 5 numbers using a bubble sort.

##      ***THIS IS A WORK IN PROGRESS***

def bubbleSort():

	a = 0
	b = 0
	c = 0
	d = 0
	e = 0


print("Hello! Please enter five different numbers when prompted")

a = int(input("Please enter your first number: "))
b = int(input("Please enter your second number: "))
c = int(input("Please enter your third number: "))
d = int(input("Please enter your fourth number: "))
e = int(input("Please enter your fifth number: "))

##print(a, b, c, d, e)

my_list = [a, b, c, d, e]

##print(list.__len__())
print(list)

def bubble(bad_list):
	##for i in range(list.__len__()):
	##	for j in range(i+1, list.__len__()):
	##		if list[j] < list[j-1]:
	##			list[j], list[i] = list[i], list[j]
	##i = i+1
	length = bad_list.__len__() - 1
	sorted = False

	while not sorted :
		sorted = True
		for i in range(length):
			if bad_list[i] > bad_list[i+1]:
				sorted = False
				bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]
	print(bad_list)

bubble(my_list)