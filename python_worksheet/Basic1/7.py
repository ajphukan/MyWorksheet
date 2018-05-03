'''
7. Write a Python program to accept a filename from the user and print the extension of that.
'''
fileName = input("Sample filename : ")
print("File extension : ", fileName.split('.')[-1])