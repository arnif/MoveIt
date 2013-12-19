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
					os.chdir(foo)
					isItHere = os.listdir(".")
					for l in isItHere:
						matchObj = re.search(fileName, l, re.IGNORECASE)
						if matchObj:
							shutil.move(l, goHere)
							os.chdir("../")
							shutil.rmtree(foo)

				else:
					if matchFile:
						# move that shit (foo to goHere)
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