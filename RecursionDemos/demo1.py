dict1 = {
	'http://schemas.xmlsoap.org/soap/envelope/:Envelope': {
		'http://schemas.xmlsoap.org/soap/envelope/:Body': {
			'http://schemas.planview.com/PlanviewEnterprise/Services/ProjectService3/2012/08:ReadResponse': {
				'http://schemas.planview.com/PlanviewEnterprise/Services/ProjectService3/2012/08:ReadResult': {
					'GeneralErrorMessage': {
						'@xmlns': {
							'': 'http://schemas.planview.com/PlanviewEnterprise/Services/ProjectService3/2012/08',
							'a': 'http://schemas.planview.com/PlanviewEnterprise/OpenSuite/OpenSuiteResult/2010/01/01',
							's': 'http://schemas.xmlsoap.org/soap/envelope/',
							'i': 'http://www.w3.org/2001/XMLSchema-instance',
							'b': 'http://schemas.planview.com/PlanviewEnterprise/OpenSuite/OpenSuiteStatus/2010/01/01'
						},
						'@http://www.w3.org/2001/XMLSchema-instance:nil': 'true'
					},
					'Failures': None,
					'Successes': {
						'http://schemas.planview.com/PlanviewEnterprise/OpenSuite/OpenSuiteStatus/2010/01/01:OpenSuiteStatus': {
							'@xmlns': {
								'b': 'http://schemas.planview.com/PlanviewEnterprise/OpenSuite/OpenSuiteStatus/2010/01/01',
								'c': 'http://schemas.planview.com/PlanviewEnterprise/OpenSuite/ProjectStatus/2012/08'
							},
							'http://schemas.planview.com/PlanviewEnterprise/OpenSuite/OpenSuiteStatus/2010/01/01:SourceIndex': '0',
							'http://schemas.planview.com/PlanviewEnterprise/OpenSuite/OpenSuiteStatus/2010/01/01:Code': {
								'@http://www.w3.org/2001/XMLSchema-instance:nil': 'true'
							},
							'http://schemas.planview.com/PlanviewEnterprise/OpenSuite/OpenSuiteStatus/2010/01/01:ErrorMessage': {
								'@http://www.w3.org/2001/XMLSchema-instance:nil': 'true'
							},
							'@http://www.w3.org/2001/XMLSchema-instance:type': 'c:ProjectStatus2',
							'http://schemas.planview.com/PlanviewEnterprise/OpenSuite/ProjectStatus/2012/08:Dto': {
								'ActualFinishDate': {
									'@xmlns': {
										'd': 'http://schemas.planview.com/PlanviewEnterprise/OpenSuite/Dtos/ProjectDto2/2012/08'
									},
									'@http://www.w3.org/2001/XMLSchema-instance:nil': 'true'
								},
								'Place': '194',
								'Duration': '0',
								'WorkId': '0001727',
								'IsTicketable': 'false',
								'ScheduleFinishDate': {
									'@http://www.w3.org/2001/XMLSchema-instance:nil': 'true'
								},
								'ScheduleStartDate': {
									'@http://www.w3.org/2001/XMLSchema-instance:nil': 'true'
								},
								'CalendarKey': 'key://2/$Cal/STANDARD',
								'EnterProgress': 'false',
								'Description': 'Auto_None_2017-11-08_15:36:33_308117',
								'LifecycleAdminUserKey': 'key://3/pvmaster',
								'PercentComplete': '0',
								'ActualStartDate': {
									'@http://www.w3.org/2001/XMLSchema-instance:nil': 'true'
								},
								'IsMilestone': 'false',
								'FatherKey': 'key://2/$Plan/17',
								'EntryDate': '2017-11-08T15:36:34.843',
								'WorkStatusKey': 'key://2/Wbs20/WBS20$REQT',
								'Notes': {
									'@http://www.w3.org/2001/XMLSchema-instance:nil': 'true'
								},
								'Key': 'key://2/$Plan/26745'
							}
						}
					},
					'Warnings': None
				}
			}
		}
	}
}


def recurse_dict(src_key, dict1):
    for key, values in dict1.items():
        if src_key == key:
            return dict1[key]
