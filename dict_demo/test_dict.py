PRJ_SOAP_ACTION = 'http://schemas.planview.com/PlanviewEnterprise/Services/ProjectService3/2012/08/IProjectService3/'
import os

PAYLOAD_PATH = os.path.abspath((os.path.dirname(__file__)))

map_project_action = {'create': {'soap_action': PRJ_SOAP_ACTION + 'create',
                                 'payload': PAYLOAD_PATH + '%(slash)s%(folder)s%(slash)s%(file)s'
                                                           % {'slash': '\\', 'folder': 'projects',
                                                              'file': 'create.xml'}},
                      'delete': {'soap_action': PRJ_SOAP_ACTION + 'delete',
                                 'payload': PAYLOAD_PATH + '%(slash)s%(folder)s%(slash)s%(file)s'
                                                           % {'slash': '\\', 'folder': 'projects',
                                                              'file': 'delete.xml'}},
                      'read': {'soap_action': PRJ_SOAP_ACTION + 'read',
                               'payload': PAYLOAD_PATH + '%(slash)s%(folder)s%(slash)s%(file)s'
                                                         % {'slash': '\\', 'folder': 'projects', 'file': 'read.xml'}},
                      'update': {'soap_action': PRJ_SOAP_ACTION + 'update',
                                 'payload': PAYLOAD_PATH + '%(slash)s%(folder)s%(slash)s%(file)s'
                                                           % {'slash': '\\', 'folder': 'projects',
                                                              'file': 'update.xml'}},
                      }

print(map_project_action['create']['payload'])

print(map_project_action['update']['soap_action'])
