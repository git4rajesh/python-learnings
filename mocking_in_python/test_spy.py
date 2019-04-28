import mock

class ClassUnderTest():
    def lower_1(self):
        print('lower_1')

    def lower_2(self):
        print('lower_2')

    def higher(self):
        self.lower_1()
        self.lower_2()



def test_ClassUnderTest():
    sut = ClassUnderTest()
    spy = mock.Mock(spec=sut)
    print('>>>>', spy.__class__)

    # test call
    ClassUnderTest.higher(spy)

    # Assert that lower_1 was called before lower_2
    assert spy.mock_calls == [mock.call.lower_1(), mock.call.lower_2()]


test_ClassUnderTest()