private class FooDummy implements Foo
{
    public String bar() { return null; }
}

public class FooCollectionTest
{
    @Test
    public void it_should_maintain_a_count()
    {
        FooCollection sut = new FooCollection();
        sut.add(new FooDummy);
        sut.add(new FooDummy);
        assertEquals(2, sut.count());
    }
}


In this example, the SUT does not care about method bar(), it just cares that it received an object of type Foo, and it doesn't matter that bar() doesn't have a method body, because for this particular test we never call it.