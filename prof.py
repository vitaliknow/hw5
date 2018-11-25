from timeit import default_timer
from inspect import isclass

def profile(obj):

	def wrape(func, cls = None):
		if cls is not None:
			name = f'{cls.__name__}.{func.__name__}'
		else:
			name = func.__name__
		
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			print(name, ' started')
			
			start_time = default_timer()
			to_return = func(*args, **kwargs)
			time = default_timer() - start_time
			
			print(f'{name} finished in {time} \n')
			return to_return
		return wrapper 


	if isclass(obj):
		for attr_name in obj.__dict__:
			attr = getattr(obj, attr_name)
			if callable(attr):
				setattr(obj, attr_name, wrape(attr, obj))
		return obj
		
	else:
		return wrape(obj)


@profile
def hello(q,e,w):
	print('qwerty')

@profile
class Test:

	def __init__(self, i = 3, j = 2):
		self.i = i
		self.k = j
	
	
	def sum(self):
		return self.i + self.k
	
if __name__ == "__main__":
	hello(2, 'w', 're')

	t1 = Test(10, 9)
	t1.sum()

	
	t2 = Test()
	t2.sum()
