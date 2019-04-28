PyTest:
======

1. hooks:
		def pytest_addoption(parser):
		def pytest_ignore_collect(path, config):
		def pytest_collection_modifyitems(config, items):
		
		Does all hooks should be placed in conftest.py?
		Use of request, config, parser etc.
		
		request.getfixturevalue('set_cmdline_opts').get('app')
			- get a value from another fixture via request object
		
		
		
2. fixtures:
		@pytest.fixture(scope='session')
		@pytest.fixture(scope='session', autouse=True)
		
		Fixtures and Scopes and autouse
	
	
3. Mark:
	@pytest.mark.slow


Pytest default plugin reference

try using config instead of request.
Do all methods in conftest have access to these two objects.

What happens if we try to access :
db = request.config.getoption('--db') Where --db was not set.

5. class CommonEnv: and tables to support Innotas.
	SELECT_COMMON_ENV_DETAILS
	
	
6. When to use yield ?


conftest.py
setup_helper.py
dispatcher.py
session_data.py




Qns:
===
1. How to run?

pytest_ignore_collect:
	2. path.fnmatch('*/ui/*')
	pytest_ignore_collect () when is it called & how.
3. CommonEnv class and CommonIntegLogger class
	- Can it accomodate pve later?
	- Supports Innotas but would require new env to have user has the unique property.
	
4. How does yield work in the fixture for setup_session


5. In dispatcher.py
def _get_feature_action_handle()
if 'via_ui' in data and data['via_ui']: ( data having this and is there a case where only key is available without a value)


6. def _get_action_artifact_class(action_artifact):
	if len(splitted) < 2:
	
	
6b. Will mandate the namining convention of all Feature files in one way. To be documented.


i. dispatcher.perform_setup(request, scope)  ---> based on scope calls  a. session_setup b. module_setup c. function_setup
ii. session_setup:
		    a. checks for session_data based on folder_name.
			b. calls _iterate_artifact_operation()
			
iii. _iterate_artifact_operation()
		a. Iterates for each artifact in setup data and calls UI/API feature.
		b. calls _get_feature_action_handle()
		
iv. _get_feature_action_handle():
		a. calls get_feature_method_handle() based on ui or non-ui flag.
		b. returns feature_method
		
v. get_feature_method_handle():
		a. _get_action_artifact_class() : splits based on keys and returns action, artifact, class.
		b. _get_feature_path() : dict having path for each feature file.
		
vi. _get_action_artifact_class() : splits based on keys and returns action, artifact, class.


vii. ConstructDS class:
		construct_data_store.py:
			self.product = product got from feature files.
			self.artifact = artifact
			
			
			APP = 'pve' and ARTIFACT = 'project'
			
			These naming conventions are important for DataStore as 'automation\core\datastore' contains pve.yml files needed for construct_data_store.py
			
			b. Can we change the camel case in pve.yml files.
			
			c. self.data_store[artifact] = local_store in data_store.py:
					project is the artifact for both pve and innotas , so gets stored under one key is it?
			

viii. xmltodict usage.
		Why do we do:
			def converter(resp):      
			  temp = json.dumps(parsed_dict)
			  temp1 = json.loads(temp)

				Also rename the method name.

				
ix. extract_value() in construct_data_store.py
		Recursively iterates in a JSON and finds the value for the key currently being searched for. Handles nested dict/list structures.
		(Candidate for unit test)
		
		
x. if 'via_ui' in response: in generate_data_store(). When do we get this in response.


xi. method generate_data_store is a candidate for unit test as we have conditions like:

		        if self.product == 'innotas':
                    attribute_id = self.get_innotas_id_for_key(key)
                    temp[identifier][key] = self.extract_innotas_value(attribute_id, resp_json)
                else:
                    temp[identifier][key] = self.extract_value(key, resp_json)
					
					
xii. FIELD_MAPPING for Innotas: are they fixed values for all environments.

xiii. extract_innotas_value() to be tested using a data to understand the logic.