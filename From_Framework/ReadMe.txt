Python programing>

1. Calling a method of super which has same signature as in Child class.

class TestStage1(TestStep):

	def setup_step(self, id):
        super(TestStage1, self).setup_step(id)  (Parent class setup_step, which has DBWrapper will be called)
		
		
class TestStep:
	def setup_step(self, id):
        DBWrapper.move_results_to_history(id)
		
		
2. Class Member used:

class SetupWork(TestStep):
    is_run_once = False
  
    def __init__(self, pve_env, pve_dsn, pve_db, rally_env, rally_user, integ_env, all_rally_time=False, has_cert=False):
	
	Here is_run_once is declared outside init. So this is not an instance member but a class member. This member gets shared among all instances.
	
3. Pickle an Object and writing to a filesystem:

			self.file = os.path.dirname(__file__) + '//' + 'temp_work_obj_pickle'
            file_handle = open(self.file, 'wb')
            pickle.dump(self, file_handle)
            file_handle.close()
			
3b. Reading a pickled Object from filesystem:

		@staticmethod
		def get_work_details():
        pickle_file_path = os.path.dirname(__file__) + '//..//tests//time//temp_work_obj_pickle'
        file_handle = open(pickle_file_path, 'rb')
        work_obj = pickle.load(file_handle)
        file_handle.close()
        return work_obj
		
		
			
3. Calling a function at the program exit:
			
			atexit.register(self.teardown_step)
			
4. virtualenv env

5. wheel file creation.