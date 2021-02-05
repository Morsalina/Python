from numpy import *
print("About first matrix")

print("enter the number of rows :", end="")
r = int(input())
print("enter the number of columns :",end="")
c = int(input())

print("enter the entries separated by space")

entries = list(map(int, input().split()))

matrix1 = array(entries).reshape(r, c)
print(matrix1)
print("About second Matrix ")
r1 = int(input("Enter the number of rows :"))
c1 = int(input("enter the number of columns :"))
element = list(map(int, input().split()))
matrix2 = array(element).reshape(r1, c1)
print(matrix2)

print("Sum of those two matrices")

matrix3 = matrix1+matrix2
print(matrix3)







