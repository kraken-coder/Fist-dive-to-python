my_file = open('file.txt', "w")

#  get info of file
# print("Name", my_file.name)

#  write to file
my_file.write('i love pyrhon')
my_file.write('and javascript')
my_file.close()

# append to file
my_file = open("file.txt", "a")
my_file.write('and PHP')
my_file.close()

#  read file
my_file = open('file.txt', "r+")
text = my_file.read(100)
print(text)