# f=open("DEMO2.txt","w")
# print(f.read)
# print(f.readline())
#f.write("CALMA")
#f.write("DESTROY")



#f=open("demo.txt")
# print(f.read())
# print(f.readline())
# print(f.readlines())


#f1=open("test.txt","w")
# f1.write("Hello Gaurav")
# f1.close()
# f1 = open("files2.txt", "r")
# print (f1.read())

# f2=open("demo.txt","a")
# f2.write("Hello Gaurav")
# f2.close()

# f2 = open("demo.txt", "r")
# print (f2.read(2))



# f1.write("JOHNNY SINS")

# for i in f:
#     for j in range(0,10):
#         print(i[j])
# for i in f:
#     f1.write(i)
# f1=open("test.txt","r")
# print(f1.read())






# f=open("demo.txt","r")
# print(f.read(10))
# print(f.tell())  





f=open("img.jpg","rb")
f1=open("img_copy.jpg","wb")
# print(f.read())

for i in f:
    f1.write(i)