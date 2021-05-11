# l= open('text1.txt','x')

# # chèn điểm vào file.txt
a= open('text1.txt','a')
a.write(str(11))
a.write('\n')

a.close()


#xuất điểm lớn nhất ra
a= open('text1.txt','r')
best_point=20
for i in a.readlines():
    if int(i) > int(best_point):
        print("best point is: "+str(best_point))
    else:
        print("simple")
# xoá file.txt
# import os
# if os.path.exists("text1.txt"):
#         os.remove("text1.txt")
