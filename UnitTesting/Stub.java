private class FooStub implements Foo
{
    public String bar()
    {
        return "bar";
    }
}

public class FooCollectionTest
{
    @Test
    public void it_should_return_joined_bars()
    {
        FooCollection sut = new FooCollection();
        sut.add(new FooStub);
        sut.add(new FooStub);
        assertEquals("barbar", sut.joined());
    }
}


Think of a Stub as a step up from a Dummy. 
It implements a required Interface, but instead of missing method bodies, it usually returns canned responses in order for you to make assertions on the output of the SUT