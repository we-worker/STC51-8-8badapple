'''
	读取文件夹里的图片数据，并按先一列列的排序来保存再code数组中。
	图片数据转为01的位图，而不是灰度图。
	最后再将数据保存到一个文件中
'''

from itertools import count
import matplotlib.image as mpimg 
path="C:\\Users\\Arc\\Videos\\badapple\\新建文件夹\\"


codes=[]
for k in range(2186):#2186
	print("------"+str(k)+"------")
	mat= mpimg.imread(path+'apple'+str(k)+'.bmp')
	for i in range(8):
		code=""
		for j in range(8):
			if(mat[j][i][0]==255):
				code+="0"
			else:
				code+="1"
		print(code)
		print(hex(int(code,2)))
		codes.append(hex(int(code,2)))



with open("C:\\Users\\Arc\\Videos\\badapple\\51codes.txt","w+") as f:
	counts=0
	string="unsigned char code"+str(counts)+"[]={"
	for i in range(len(codes)):
		string+=str(codes[i])
		if (i%(500*8)==(500*8-1)):
			f.write(string+"};\n")
			counts=counts+1
			string="unsigned char code"+str(counts)+"[]={"
		else:
			string+=","
	f.write(string+"};")

