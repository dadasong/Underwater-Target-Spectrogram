#-*- coding:utf-8 -*-
from PIL import Image
import os
import glob

def cov(path,path2):
	count=1
	s0="out"
	f=glob.glob(path)
	for i in f:
		
		print(i)
		s=str(count)+s0
		s3=s+".bmp"
		# path_de=path2+i
		# print(path_de)
		im=Image.open(i)
		print(path2+s3)
		(x,y)=im.size
		x_s=300
		y_s=300
		out=im.resize((x_s,y_s))
		out.save(path2+s3)
		try:
			if(i):
				os.remove(i)
		except:
			pass
		count+=1


if __name__ == "__main__":
	#cov("C:/Users/Administrator/Desktop/RF spectrogram/diver/*.bmp","C:/Users/Administrator/Desktop/RF spectrogram/diver/")
	cov("C:/Users/Administrator/Desktop/RF spectrogram/diver_p/*.bmp","C:/Users/Administrator/Desktop/RF spectrogram/diver_p/")
	cov("C:/Users/Administrator/Desktop/RF spectrogram/no_target/*.bmp","C:/Users/Administrator/Desktop/RF spectrogram/no_target/")
	cov("C:/Users/Administrator/Desktop/RF spectrogram/no_target_p/*.bmp","C:/Users/Administrator/Desktop/RF spectrogram/no_target_p/")
	cov("C:/Users/Administrator/Desktop/RF spectrogram/oxygen_cylinder/*.bmp","C:/Users/Administrator/Desktop/RF spectrogram/oxygen_cylinder/")
	cov("C:/Users/Administrator/Desktop/RF spectrogram/oxygen_cylinder_p/*.bmp","C:/Users/Administrator/Desktop/RF spectrogram/oxygen_cylinder_p/")