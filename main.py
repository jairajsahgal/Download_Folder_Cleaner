import os
import shutil
from subprocess import PIPE, run


user=os.popen('whoami').read().split()[0]



def xdman_cleanup(user):
	#Documents
	Documents=[]
	for i in os.listdir("/home/{u}/Downloads/Documents".format(u=user)):
		Documents.append(i)
	for i in Documents:
		shutil.move("/home/{u}/Downloads/Documents/{o}".format(u=user,o=i),"/home/{u}/Documents/{o}".format(u=user,o=i))
	#Music
	Music=[]
	for i in os.listdir("/home/{u}/Downloads/Music".format(u=user)):
		Music.append(i)
	for i in Music:
		shutil.move("/home/{u}/Downloads/Music/{o}".format(u=user,o=i),"/home/{u}/Music/{o}".format(u=user,o=i))
	#Videos
	Video=[]
	for i in os.listdir("/home/{u}/Downloads/Video".format(u=user)):
		Video.append(i)
	for i in Video:
		shutil.move("/home/{u}/Downloads/Video/{o}".format(u=user,o=i),"/home/{u}/Videos/{o}".format(u=user,o=i))

def check_xdm(user):
	result = run("which xdman", stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True).stdout
	if len(result)>0:
		xdman_cleanup(user)


def main_download_folder(user):
	files=[]
	for i in os.listdir("/home/{u}/Downloads".format(u=user)):
		if "." in i:
			files.append(i)
	for i in files:
		#Documents
		if os.path.splitext(i)[1] in [".pdf",".doc",".docx",".html",".txt",".ppt",".pptx",".htm",".xlsx",".csv",".py",".cpp",".c",".js"]:
			shutil.move('/home/{u}/Downloads/{o}'.format(o=i,u=user), '/home/{u}/Documents/{o}'.format(o=i,u=user))

		#Videos
		elif os.path.splitext(i)[1] in [".mp4",".mov",".wmv",".flv",".avi",".webm",".mkv"]:
			shutil.move('/home/{u}/Downloads/{o}'.format(o=i,u=user), '/home/{u}/Videos/{o}'.format(o=i,u=user))

		#Pictures
		elif os.path.splitext(i)[1] in [".jpeg",".gif",".png",".tiff",".psd",".eps",".ai",".indd",".raw"]:
			shutil.move("/home/{u}/Downloads/{o}".format(o=i,u=user),"/home/{u}/Pictures/{o}".format(o=i,u=user))

		#Music
		elif os.path.splitext(i)[1] in [".wav",".mp3"]:
			shutil.move("/home/{u}/Downloads/{o}".format(o=i,u=user),"/home/{u}/Music/{o}".format(o=i,u=user))

check_xdm(user)
main_download_folder(user)