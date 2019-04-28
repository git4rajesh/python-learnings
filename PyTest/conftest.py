import pytest


@pytest.fixture(scope="session", autouse=True)
def callattr_ahead_of_alltests(request):
    print ("callattr_ahead_of_alltests called")
    session = request.node
    for item in session.items:
        print(item.name)
        print(item.__doc__)
