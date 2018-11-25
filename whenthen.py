
def whenthen(func):
	class WhenThen:
		def __init__(self, func):
			self._func = func
			self._whenList = []
			self._thenList = []
		
		def __call__(self, *args, **kwargs):
			if len(self._whenList) != len(self._thenList):
				raise SyntaxError
			for i, when_func in enumerate(self._whenList):
				if when_func(*args, **kwargs) == True:
					return self._thenList[i](*args, **kwargs)
				else:
					return self._func(*args, **kwargs)
		
		def when(self, func):
			if len(self._whenList) != len(self._thenList):
				raise SyntaxError
			self._whenList.append(func)
			return self
		
		def then(self, func):
			if len(self._whenList) != (len(self._thenList) + 1):
				raise SyntaxError
			self._thenList.append(func)
			return self
	
	return WhenThen(func)

@whenthen
def fract(x):
    return x * fract(x - 1)


@fract.when
def fract(x):
    return x == 0


@fract.then
def fract(x):
    return 1


@fract.when
def fract(x):
    return x > 5


@fract.then
def fract(x):
    return x * (x - 1) * (x - 2) * (x - 3) * (x - 4) * fract(x - 5)


if __name__ == '__main__':
	print(fract(0))