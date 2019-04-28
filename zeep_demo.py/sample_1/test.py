import zeep


client = zeep.Client(wsdl='http://poc41.pvcloud.com/planview/services/LoginService.svc?wsdl')

print(client)
client.s
# cert = client.service.Login('PVE', 'jharris ', 'poc6')
# print(cert)

# client2 = zeep.Client(wsdl='http://localhost/planview/services/AttributeService.svc?wsdl')
# binding = client2.bind('AttributeService', 'BasicHttpBinding_IAttributeService2')
# #client2.wsdl.dump()
# client2.transport.session.headers.update({'Cookie':'LoginCert=' + cert})
#
#
# element1 = client2.get_element('ns2:EntityAttributeDto2')
# dto = element1(EntityKey='key://2/$Plan/16250')
#
# element2 = client2.get_element('ns2:ArrayOfEntityAttributeDto2')
# attributeDtoList = element2(EntityAttributeDto2=dto)
#
# response = binding.ReadAll(attributeDtoList)
# print (response)
