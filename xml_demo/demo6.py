from lxml import etree as ET
from lxml.builder import E
from lxml.builder import ElementMaker

A = E.a
I = E.i
B = E.b

E1 = ElementMaker(namespace="http://schemas.xmlsoap.org/soap/envelope/",
                  nsmap={'soapenv': "http://schemas.xmlsoap.org/soap/envelope/"})

E2 = ElementMaker(namespace="http://schemas.planview.com/PlanviewEnterprise/Services/TaskService3/2012/08",
                  nsmap={'ns': "http://schemas.planview.com/PlanviewEnterprise/Services/TaskService3/2012/08"})

E3 = ElementMaker(namespace="http://schemas.planview.com/PlanviewEnterprise/OpenSuite/Dtos/TaskDto2/2012/08",
                  nsmap={'ns1': "http://schemas.planview.com/PlanviewEnterprise/OpenSuite/Dtos/TaskDto2/2012/08"})



def CLASS(v):
    # atrib_prefix = r'http://www.w3.org/2001/XMLSchema-instance:'
    # atrib = atrib_prefix + 'class'

    atrib = 'class'
    param = 'http://www.w3.org/2001/XMLSchema:' + v
    return {atrib: param}

page = (
    E.html(
        E.head(
            E.title("This is a sample document")
        ),
        E.body(
            E.h1("Hello!", CLASS("title")),
            E.p("This is a paragraph with ", B("bold"), " text in it!"),
            E.p("This is another paragraph, with a ",
                A("link", href="http://www.python.org"), "."),
            E.p("Here are some reservered characters: <spam&egg>."),
            ET.XML("<p>And finally, here is an embedded XHTML fragment.</p>"),
        )
    )
)

print (ET.tostring(page))

