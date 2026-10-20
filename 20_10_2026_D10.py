# #1.Average of Three Numbers
# def calculate_average(n1,n2,n3):
#     avg = (n1+n2+n3)/3
#     return avg

# n1,n2,n3 = list(map(int, input("Enter the no:").split()))
# a = calculate_average(n1,n2,n3)
# print(round(a,1))

# #or
# def calculate_average(n1, n2, n3):
#     return (n1 + n2 + n3) / 3.0

# if __name__ == '__main__':
#     inputs = list(map(float, input().split()))
#     print(calculate_average(inputs[0], inputs[1], inputs[2]))

# #2.Product of Three Numbers
# def calculate_product(n1,n2,n3):
#     return n1*n2*n3

# nums = list(map(int,input("Enter the no:").split()))
# print(calculate_product(nums[0],nums[1],nums[2]))

# #3.Count Lines in a File
# def count_lines(filename):
#     with open(filename,"r") as f:
#         a = f.readlines()
#         return len(a)

# fname = input().strip()
# print(count_lines(fname))

# #4.Count Characters in a File
# def count_characters(filename):
#     with open(filename,"r") as f:
#         return len(f.read())

# f_name = input().strip()
# print(count_characters(f_name))

# #5.Lambda Function for Square
# x = int(input("Enter the no:"))
# a = lambda b:b**2
# print(a(x))

# #6.Lambda Even Check
# n = int(input("Enter the no:"))
# even = lambda x:x%2 == 0
# print(even(n))

# #7.Filter Positive Numbers
# nums = list(map(int,input().split()))
# pos = list(filter(lambda x:x>0,nums))
# print(pos)

# #8.Filter Words by Length
# stg = list(input().split())
# a = list(filter(lambda a: len(a)>=4, stg))
# print(a)

# #9. Exception Handling for Division

# try:
#     a,b = map(int,input().split())
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")
# except ValueError:
#     print("Error: Invalid input!")

# #10. File Not Found Exception
# try:
#     f = input("Filename:")
#     with open(f,"r") as a:
#         print(a.read())
# except FileNotFoundError:
#     print("Error: File does not exist!")

# #11.Enumerate with Custom Start
# words = input().split()
# a = enumerate(words,start=1)

# for idx, word in a:
#     print(f"{idx} : {word}")

# #12.Enumerate with Default Start
# words = input().split()
# for idx,val in enumerate(words):
#     print(f"{idx} - {val}")

# #13.Student Marks Processing from File
# def process_marks():
#     try:
#         fp = open("StudMarks.csv", "r+")
#         rec = fp.readlines()
#         print(rec)
#         fp.close()

#         l = []
#         for st in rec:
#             st = st.replace("\n", "")
#             lrec = st.split(",")
#             total = int(lrec[1]) + int(lrec[2]) + int(lrec[3])
#             l.append(f"{lrec[0]}, Total: {total}\n")

#         fp_out = open("outputfile.txt", "w+")
#         fp_out.writelines(l)
#         fp_out.close()
#         print("File Processed")
#     except Exception as e:
#         print("Error:", e)

# if __name__ == '__main__':
#     process_marks()

#14.Filter Passing Students by Subject 1
try:
    with open("StudMarks.csv","r+") as f:
        a = f.readlines()
        l = []
        for stud in a:
            stud.replace("\n","")
            a=stud.split(",")
            if int(a[1])>=50:
                l.append(a[0])
        print("File Processed")
        print(l)
except Exception as e:
    print("Error:",e)
