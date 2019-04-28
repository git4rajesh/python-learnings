def outside():
    msg = "Outside!"

    def inside():
        msg = "Inside!"
        print(msg)

    inside()
    print(msg)

outside()

# When we run outside, msg has the value "Inside!" in the inside
# function, but retains the old value in the outside function.