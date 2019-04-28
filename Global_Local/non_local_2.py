# Preventing that behaviour is where the nonlocal keyword comes in.


def outside():
    msg = "Outside!"

    def inside():
        nonlocal msg
        msg = "Inside!"
        print(msg)

    inside()
    print(msg)

outside()

# 2. Now, by adding nonlocal msg to the top of inside, Python knows that when it sees an assignment to msg, it should assign to the variable from the outer scope instead of declaring a new variable that shadows its name.