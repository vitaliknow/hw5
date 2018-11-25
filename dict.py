import os
from collections.abc import MutableMapping

class Dict(MutableMapping):
	def __init__(self, dirPath):
		self._dirPath = dirPath
		os.makedirs(dirPath, exist_ok = True)
	
	def __getitem__(self, key):
		filePath = self._dirPath + '/' + key + '.txt'
		try:
			with open(filePath, 'r') as wFile:
				return wFile.read()
		except FileNotFoundError :
			return None
	
	def __setitem__(self, key, value):
		filePath = self._dirPath + '/' + key + '.txt'

		with open(filePath, 'w') as wFile:
			wFile.write(value)

	def __delitem__(self, key):
		key = key + '.txt'
		for fileName in os.listdir(self._dirPath):
			if key == fileName:
				filePath = self._dirPath + '/' + key
				os.remove(filePath)
				return
		raise KeyError(key)

	def __iter__(self):
		return iter(self.items())
	
	def __len__(self):
		return len(os.listdir(self.dirPath))



	def items(self):
		items_list = []
		for fileName in os.listdir(self._dirPath):
			filePath = self._dirPath + '/' + fileName
			with open(filePath, 'r') as rFile:
				fileName = fileName.split('.')[0]
				items_list.append((fileName, rFile.read()))
		return items_list
	
	def append(self, key, value):
		pair = (key, value)
		filePath = self._dirPath + '/' + pair[0] + '.txt'
		with open(filePath, 'w'):
			wFile.write(pair[1])
	
	def clear(self):
		for file in os.listdir(self._dirPath):
			filePath = self._dirPath + '/' + file
			os.remove(filePath)
	
	def keys(self):
		keys_list = []
		for fileName in os.listdir(self._dirPath):
			keys_list.append(fileName)
		return keys_list
	
	def value(self):
		values_list = []
		for fileName in os.listdir(self._dirPath):
			filePath = self._dirPath + '/' + fileName
			with open(filePath, 'r') as rFile:
				values_list.append(rFile.read())
		return values_list
	