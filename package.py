#!/usr/bin/env python
# Package maintenance tool

import os, sys, argparse, zipfile, tarfile

class Parser():
 def RunParser(self):
 	arguments = argparse.ArgumentParser(description='Package maintenance tool')
 	arguments.add_argument('-zip', help='Creates a ZIP package', action='store_true')
 	arguments.add_argument('-tar', help='Creates a TAR package', action='store_true')
 	arguments.add_argument('-v', help='Version informations', action='store_true')

 	parser = arguments.parse_args()
 	if parser.zip:
 		zip = ZIP()
 		zip.CreateArchive()
 	elif parser.tar:
 		tar = TAR()
 		tar.CreateArchive()
 	elif parser.v:
 		print("Package maintenance tool 1.0 (r001)")
 	else:
 		print("ERR: invalid argument!")

class ZIP():
	def CreateArchive(self):
		zf = zipfile.ZipFile("iVim-release.zip", "w")
		for root, dirs, files in os.walk("theme/"):
			for file in files:
				zf.write(os.path.join(root, file))

class TAR():
	def CreateArchive(self):
		with tarfile.open('iVim-release.tar.gz', "w:gz") as tar:
			tar.add("theme/iVim.tmTheme", arcname=os.path.basename("iVim.tmTheme"))
			tar.add("theme/iVim (colored comments).tmTheme", arcname=os.path.basename("iVim (colored comments).tmTheme"))

if __name__ == '__main__':
	parser = Parser()
	parser.RunParser()