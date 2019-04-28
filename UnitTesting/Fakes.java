Fakes
1. Similar to a Stub being a step up from a Dummy, the simplest way to think of a Fake is as a step up from a Stub.
2. This means not only does it return values, but it also works just as a real Collaborator would. 
3. Usually a Fake has some sort of shortcut that means that they are unsuitable for production


 In short, a fake is a functional, but non-production version of the actual test resource. 
 It lacks the checks and balances found in resource, it uses simpler algorithms, and it seldom, if ever, stores or transports data.