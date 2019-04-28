import os,sys

class DemoJoin:
	
	def __init__(self, num):
		self.rangenum = num

	def join_fun(self):
		joinned_str = ''.join([str(n) for n in range(self.rangenum)])
		return joinned_str
		
if __name__ == '__main__':
	#print(__file__)
	abspath_filename = os.path.abspath( __file__ )

	print('PATH:', abspath_filename)
	file_name = os.path.basename(abspath_filename)
	dir_name = os.path.dirname(abspath_filename)
	print(dir_name)
	print(file_name)
	new_path = os.path.join(dir_name,'..')
	os.chdir(new_path)
	print(os.getcwd())
	demo_join_obj = DemoJoin(6)
	#print(demo_join_obj.join_fun())
		
		
	
		
