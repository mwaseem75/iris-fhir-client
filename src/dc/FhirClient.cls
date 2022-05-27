Class dc.FhirClient Extends %SwizzleObject
{

// Create records in FHIRServer and initate Global Variable to hold current server ID

ClassMethod Init() As %Integer
{
	if $DATA(^$GLOBAL("^ActiveFhirServer"))= 0 
	{
		Set ^ActiveFhirServer = 1
	}
	//if server id 1 is not already created then create server with ID 1
	Set obj = ##class(dc.FhirServer).%OpenId(1)
	if $isobject(obj) = 0
	{
		set obj = ##class(dc.FhirServer).%New()
		set obj.ServerName = "InterSystem FHIR Accelerator Service"
		set obj.Endpoint = "https://fhir.83z8498j30i6.static-test-account.isccloud.io"
		set obj.ApiKey = "CDqtU2GjQUaICOC65Ilgv1LHQIEDr4Vn12nnlmMY"
		set obj.EndpointOAuth = "https://fhirauth.83z8498j30i6.static-test-account.isccloud.io/oauth2"
		set sts = obj.%Save()
		if sts '= 1
		{
			write "Error while creating server ID1"
		}
	} 
	//if server id 1 is not already created then create server with ID 1
	Set obj = ##class(dc.FhirServer).%OpenId(2)
	if $isobject(obj) = 0
	{
		set obj = ##class(dc.FhirServer).%New()
		set obj.ServerName = "SmartHealthIT Open FHIR Server"
		set obj.Endpoint = "https://r4.smarthealthit.org"
	
		set sts = obj.%Save()
		if sts '= 1
		{
			write "Error while creating server ID1"
		}
	}
}

ClassMethod test()
{
  Set sc = $$$OK
  Set sm = ##class(%SYS.Python).Import("sample")
  write sm.hello()
  Return sc
}

ClassMethod GetTotalRecords() As %Integer
{
	return 0
}

ClassMethod GetTotalRecordsd(resource As %String) As %Integer
{
	return 5
}

// Set Current FHIR Server

ClassMethod SetFhirServer(serverid As %Integer)
{
	Set ^ActiveFhirServer = serverid
}

// 1-Count Resource, Pass "ALL" in case of counting all the resources

ClassMethod ResourceCount(resource As %String) As %Integer
{
	
	
	//Get Active Server data based on Global Variable 
	Set obj = ##class(dc.FhirServer).%OpenId(^ActiveFhirServer)
	//If Url and ApiKey is defined
	if $isobject(obj)  
	{  
	  //Call Embedded Python Function to get Number of Resources
	  
	  try {
  //SOAP request code
 
          Set irisfhirclient = ##class(%SYS.Python).Import("irisfhirclient")
          
} Catch err {
	w "Error" 
	  w err.Name
	  return 0
}  
	  w "Connected Fine"
	  return 44
	  Set count = irisfhirclient.ResourceCount(resource,obj.Endpoint,obj.ApiKey)
	  
	  return count
	}
	//Active Server data is not defined
  	else
  	{ 
  		Quit "Not able to get server Info.."
  	}
  	return count
}

// Used in HTML

ClassMethod GetResourceList(resource As %String) As %Status
{
	//Get Active Server data based on Global Variable 
	Set obj = ##class(dc.FhirServer).%OpenId(^ActiveFhirServer)
	//If Url and ApiKey is defined
	if $isobject(obj)  
	{  
	  //Call Embedded Python Function to get Number of Resources
	  Set irisfhirclient = ##class(%SYS.Python).Import("irisfhirclient")
	  Set data = irisfhirclient.ResourceListHTML(resource,obj.Endpoint,obj.ApiKey) 
	}
	//Active Server data is not defined
  	else
  	{ 
  		Quit "Not able to get server Info.."
  	}
  	return data
}

// 2- Get Resource List 

ClassMethod ResourceList(resource As %String) As %Status
{
	//Get Active Server data based on Global Variable 
	Set obj = ##class(dc.FhirServer).%OpenId(^ActiveFhirServer)
	//If Url and ApiKey is defined
	if $isobject(obj)  
	{  
	  //Call Embedded Python Function to get Number of Resources
	  Set irisfhirclient = ##class(%SYS.Python).Import("irisfhirclient")
	  do irisfhirclient.ResourceList(resource,obj.Endpoint,obj.ApiKey) 
	}
	//Active Server data is not defined
  	else
  	{ 
  		Quit "Not able to get server Info.."
  	}
  	Quit $$$OK
}

// 2- Get Patint Resources List 

ClassMethod ResourceListPatient(resource As %String, patientId As %Integer) As %Status
{
	//Get Active Server data based on Global Variable 
	Set obj = ##class(dc.FhirServer).%OpenId(^ActiveFhirServer)
	//If Url and ApiKey is defined
	if $isobject(obj)  
	{  
	  //Call Embedded Python Function to get Number of Resources
	  Set irisfhirclient = ##class(%SYS.Python).Import("irisfhirclient")
	  do irisfhirclient.ResourceListPatient(resource,patientId,obj.Endpoint,obj.ApiKey) 
	}
	//Active Server data is not defined
  	else
  	{ 
  		Quit "Not able to get server Info.."
  	}
  	Quit $$$OK
}

// Get Resources List

ClassMethod PrintResourceList(resource As %String)
{
	Set irisfhirclient = ##class(%SYS.Python).Import("irisfhirclient")
  	do irisfhirclient.PrintResourceList(resource)
}

ClassMethod SaveOrg() [ Language = python ]
{
	
	from fhirpy import SyncFHIRClient
		
	client = SyncFHIRClient(url = "http://localhost:52773/csp/healthshare/samples/fhir/r4", extra_headers={"x-api-key":"CDqtU2GjQUaICOC65Ilgv1LHQIEDr4Vn12nnlmMY"})
	organization = client.resource(
        'Organization',
        name='beda.software',
        active=False
    );
	organization.save()
}

// Create New Resource

ClassMethod CreateResource(resource As %String) [ Language = python ]
{
	import os,sys
	from fhirpy import SyncFHIRClient
	from json import dump

	client = SyncFHIRClient(url = "http://localhost:52773/csp/healthshare/samples/fhir/r4", extra_headers={"Content-Type":"application/fhir+json","x-api-key":"CDqtU2GjQUaICOC65Ilgv1LHQIEDr4Vn12nnlmMY"})
	patient = client.resource(resource)
	patient['name'] = [
    {
        'given': ['John'],
        'family': 'Thompson',
        'use': 'official',
        'prefix': ['Mr.']
    }
	]  
	patient['birthDate'] = '1985-05-05'
	patient.save()
}

ClassMethod CreateObservation(resource As %String) [ Language = python ]
{
	import os,sys
	from fhirpy import SyncFHIRClient
	from json import dump

	client = SyncFHIRClient(url = "http://localhost:52773/csp/healthshare/samples/fhir/r4", extra_headers={"Content-Type":"application/fhir+json","x-api-key":"CDqtU2GjQUaICOC65Ilgv1LHQIEDr4Vn12nnlmMY"})
	observation = client.resource(
    'Observation',
    status='preliminary',
    category=[{
        'coding': [{
            'system': 'http://hl7.org/fhir/observation-category',
            'code': 'vital-signs'
        }]
    }],
    code={
        'coding': [{
            'system': 'http://loinc.org',
            'code': '8310-5'
        }]
    })
	observation['effectiveDateTime'] = '2018-10-20'
	observation['valueQuantity'] = {
    'system': 'http://unitsofmeasure.org',
    'value': 96.8,
    'code': 'degF'
	}
	
	patient = client.resources('Patient').search(name=['John', 'Thompson']).first()
	observation['subject'] = patient.to_reference()
	observation.save()
	dump(observation, sys.stdout, indent=2)
}

// Function to get tables header row based on resource

ClassMethod GetHeaderRow(id As %Integer) As %String
{
    SET hrow = "<th>ID</th><th>Family Name</th><th>Given Name</th><th>DOB</th><th>Gender</th>"
    RETURN hrow
}

ClassMethod GetTableData(id As %Integer) As %String
{
    SET hrow = "<td>ID</td><td>Family Name</td><td>Given Name</td><td>DOB</td><td>Gender</td>"
    RETURN hrow
}

}
