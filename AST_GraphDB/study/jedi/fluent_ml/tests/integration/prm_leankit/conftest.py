import pytest

from automation.core.src import setup_helper
from automation.core.src.test_details import TestDetails
from automation.fluent_ml.src import helper
from automation.fluent_ml.tests.integration.prm_leankit import session
from automation.integration.src.constants_reader import ConstantsReader


@pytest.fixture(scope='session')
def set_cmdline_opts(request):
    """
    Picks cmdline args passed by the user from request.config and
    stores in a dict (cmd_opts)
    :param request: py.test request fixture
    :return: populated cmd_opts dict
    """
    cmd_opts = {}
    cmd_opts = setup_helper.common_cmd_opts_mapping(cmd_opts, request)
    cmd_opts = setup_helper.integ_cmd_opts_mapping(cmd_opts, request)
    return cmd_opts


@pytest.fixture(scope='session', autouse=True)
def populate_env_cert(set_cmdline_opts):
    cmd_opts = set_cmdline_opts
    setup_helper.pve_lk_cert_logger(cmd_opts)


@pytest.fixture(scope='session', autouse=True)
def populate_constants(set_cmdline_opts):
    cmd_opts = set_cmdline_opts
    ConstantsReader.get_pve_constants(cmd_opts['env'], cmd_opts['dsn'])
    ConstantsReader.get_lk_constants(cmd_opts['ext_env'], cmd_opts['ext_user'])


@pytest.fixture(scope="function", autouse=True)
def setup_zephyr():
    pass


@pytest.fixture(scope="function", autouse=True)
def set_ext_app(request):
    ext_app = request.config.getoption('--ext_app')
    TestDetails.ext_app = ext_app


# overriding the base fixture with no implementation
@pytest.fixture(scope="session", autouse=True)
def data_repository():
    pass


@pytest.fixture(scope='session', autouse=True)
def setup_session(request, data_repository):
    test_id = 'session_setup'
    doc_str = 'creating session level data'
    TestDetails.set(test_id, doc_str, scope='session')
    session_setup = getattr(session, 'session_setup', None)
    if session_setup:
        session_setup()
    yield
    TestDetails.test_id = test_id
    helper.teardown('session')


@pytest.fixture(scope='module', autouse=True)
def get_module_identifier(request):
    pass


@pytest.fixture(scope='module', autouse=True)
def setup_module(request):
    module_path = request.module.__name__
    module_name = module_path.split('.')[-1]
    test_id = '{}_setup'.format(module_name)
    doc_str = 'creating module level data'
    TestDetails.set(test_id, doc_str, scope='module')

    module_setup = getattr(request.module, 'module_setup', None)
    if module_setup:
        module_setup()
    yield
    TestDetails.test_id = test_id
    helper.teardown('module')


@pytest.fixture(scope='function', autouse=True)
def setup_function(request, initial_setup):
    yield
    helper.teardown('function')


@pytest.fixture(scope='function')
def initial_setup(request):
    pass
