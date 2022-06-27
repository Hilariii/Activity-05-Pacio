import cv2 as cv
import numpy as np
import sys
import time

filepath = "zh.jpg"

color = int(input("ENTER A NUMBER : \n[1]COLORED  [2]UNCHANGED    [3]GRAYSCALE\n= "))
if (color == 1):
		vcolumn = 1
elif (color == 2):
		vcolumn = -1
elif (color == 3):
		print("Grayscale is not available!")
		exit()
else:
		print("INVALID INPUT! 1 - 3 ONLY!")
		exit()

image = cv.imread(filepath,vcolumn)
cv.imshow("Zeus & Hades",image)
cv.waitKey(0)
cv.destroyAllWindows()

x = int(input("PROCEED?\n[1] EXIT\n[2] YES\nANSWER : "))
	
if (x==1):
	print("THANK YOU !")
	exit()
elif (x==2):
	num = 1
	while num < 2 :
		q = int (input("CHOOSE A NUMBER :\n[1] D - TYPE\n[2] SIZE PROPERTY\n[3] SHAPE\n[4] MODIFY\n[5] DIMENSION\n[6] EXIT\n= "))
		if (q == 1):
			print("D - TYPE : ",image.dtype)
			time.sleep(2)
		elif (q == 2):
			print("SIZE : ",image.size)
			time.sleep(2)
		elif (q == 3):
			print("IMAGE SHAPE : ",image.shape)
			time.sleep(2)
		elif (q == 4):
			print("PIXEL : ",image.shape,"\n [ROW , COLUMN , FLAG]")
			vrow = int (input("ROW : "))
			vcolumn = int (input("COLUMN : "))
			p = image[vrow,vcolumn]
			print ("PIXEL COLOR : ",p)
			px = int(input("WANT TO CHANGE THE COLOR ?\n[1] YES\n[2] NO\n="))
			if (px == 1):
				p = image[vrow,vcolumn]
				r = int(input("EDIT THE COLOR RED : "))
				g = int(input("EDIT THE COLOR GREEN : "))
				b = int(input("EDIT THE COLOR BLUE : "))
				image.itemset((vrow,vcolumn,0),r)
				image.itemset((vrow,vcolumn,1),g)
				image.itemset((vrow,vcolumn,2),b)
				print ("UPDATED COLOR OF THE PIXEL : ",p)
				time.sleep(3)
				cv.imshow("Zeus and Hades",image)
				cv.waitKey(0)
				cv.destroyAllWindows()
		elif (q == 5):
			print("DIMENSION\nMAXIMUM NUMBER OF PIXEL : ",image.shape,"\n[X START : X END , Y START : Y END]")
			xs = int(input("ENTER X START : "))
			xe = int(input("ENTER X END : "))
			ys = int(input("ENTER Y START : "))
			ye = int(input("ENTER Y END : "))

			roi = image[xs:xe,ys:ye]
			cv.imshow ("Zeus and Hades",roi)
			cv.waitKey(0)
			cv.destroyAllWindows()
			
		elif (q == 6):
			print("THANK YOU FOR USING THE SYSTEM !")
			exit()
	

else:
	print("TRY AGAIN !")
	exit()
