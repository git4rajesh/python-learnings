http://howtodoinjava.com/design-patterns/structural/bridge-design-pattern/
http://wiki.c2.com/?BridgePattern
https://stackoverflow.com/questions/319728/when-do-you-use-the-bridge-pattern-how-is-it-different-from-adapter-pattern
http://www.journaldev.com/1491/bridge-design-pattern-java


                  ----Shape---
                  /            \
         Rectangle              Circle
        /         \            /      \
BlueRectangle  RedRectangle BlueCircle RedCircle


Refactor to:

          ----Shape---                        Color
         /            \                       /   \
Rectangle(Color)   Circle(Color)           Blue   Red