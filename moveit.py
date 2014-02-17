#!/usr/bin/python
import re
import os
import json
import shutil

json_data = open('locations.json')
data = json.load(json_data)
path = '.'
files = os.listdir(path)


def main():
	count = 0
	for i in data['tvshows']:
		show = data['tvshows'][count]['name']
		goHere = data['tvshows'][count]['location']
		reggie = createRegex(show)

		# matcha dotid vid eitthvad i files arrayinu
		for foo in files:
			matchObj = re.search( reggie, foo, re.IGNORECASE)
			if matchObj:
				fileName = reggie + ".*(.mp4|.mkv|.avi)"
				
				matchFile = re.search(fileName, foo, re.IGNORECASE)
				

				if os.path.isdir(foo):
					# get the file from the folder and remove it
					print "FOLDER " + foo
					os.chdir(foo)
					isItHere = os.listdir(".")
					rarFile = reggie + ".*(.rar)"

					for l in isItHere:
						rarMatch = re.search(rarFile, l, re.IGNORECASE)
						matchObj = re.search(fileName, l, re.IGNORECASE)

						if rarMatch:
							print "UNRAR " + l
							os.system("unrar x -e " + l)
							os.system("rm " + l)
							isItHere = os.listdir(".")
							for b in isItHere:
								matchObj = re.search(fileName, b, re.IGNORECASE)
								if matchObj:
									shutil.move(b, goHere)
									os.chdir("../")
									shutil.rmtree(foo)
							

						elif matchObj:
							print l + " goes " + goHere
							shutil.move(l, goHere)
							os.chdir("../")
							shutil.rmtree(foo)

				else:
					if matchFile:
						# move that shit (foo to goHere)
						print foo + " goes " + goHere
						shutil.move(foo, goHere)
				
				
		count = count + 1


def createRegex(show):

	arr = show.replace(show[:1],"^.")
	arr = arr.split(" ")
	first = arr[0] + ".*"
	# fileEnd = ".*(.mp4|.mkv|.avi)"
	fileEnd = ".*."

	#replace rest first char with ".*."
	newArr = []
	for i in arr:
		newString  = i.replace(i[:1], ".*.")
		newArr.append(newString)

	newArr[0] = first
	newArr.append(fileEnd)
	returnThis = "".join(newArr)

	return returnThis


main()
json_data.close()
