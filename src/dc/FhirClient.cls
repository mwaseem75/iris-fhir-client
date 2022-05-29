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
			write "Error while creating server ID2"
		}
	}
}

// Resigter server by using FhirServer persistent Class

ClassMethod RegisterServer(ServerName As %String, Endpoint As %String, ApiKey As %String = "", EndpointOAuth As %String = "") As %Integer
{
	//Create global fhirServer reference variable if not created
	if $DATA(^$GLOBAL("^ActiveFhirServer"))= 0 
	{
		Set ^ActiveFhirServer = 1
	}
	//Add New FhirServer
	set obj = ##class(dc.FhirServer).%New()
	set obj.ServerName = ServerName
	set obj.Endpoint = Endpoint
	set obj.ApiKey = ApiKey
	set obj.EndpointOAuth = EndpointOAuth
	set sts = obj.%Save()
	if sts = 1
	{
			write "FHIR Server registered successfully"
			
	}
	else
	{
			write "Error while registring FHIR Server"
	}
}

// Get Server List

ClassMethod ServerList() As %Integer
{

	//Print Servier List
	SET qry = "SELECT ID, ServerName, Endpoint FROM dc.FhirServer"
	SET tStatement = ##class(%SQL.Statement).%New()
	SET qStatus = tStatement.%Prepare(.qry)
    IF qStatus =1 {
             SET rsetD = tStatement.%Execute()
            
                    //DO rset.%Display()
    WRITE "------------------------------------------------------------------",!           
    WRITE "Registered FHIR Servers",!           
    WRITE "------------------------------------------------------------------",!  
    WHILE rsetD.%Next() {
	                    IF rsetD.%GetData(1)= ^ActiveFhirServer
    { 
        SET STS = "Active"
    }    
    ELSE
    {
	     SET STS = "Not Active"
	    }
             
              WRITE "ID", ?12,rsetD.%GetData(1),!
              WRITE "Name", ?12,rsetD.%GetData(2),!
              WRITE "EndPoint", ?12,rsetD.%GetData(3),!
              WRITE "ApiKey", ?12,rsetD.%GetData(4),!
              WRITE "EPOAuth2", ?12,rsetD.%GetData(5),!
              WRITE "ISActive", ?12,STS,!
             
              WRITE "------------------------------------------------------------------",!           
              
                                                
                        }
                 }
}

// Get Server List. Used in CSP application

ClassMethod GetServerList() As %String
{

	//Print Servier List
	SET qry = "SELECT ID, ServerName FROM dc.FhirServer"
	SET tStatement = ##class(%SQL.Statement).%New()
	SET qStatus = tStatement.%Prepare(.qry)
    IF qStatus =1 {
         SET rsetD = tStatement.%Execute()
            
             
   set dtbl  = ""
       WHILE rsetD.%Next() {
	IF rsetD.%GetData(1)= ^ActiveFhirServer
    { 
        SET STS = "Active"
    }    
    ELSE
    {
	     SET STS = "Not Active"
	    }
                       
            set dtbl = dtbl_"<tr><td>"_ rsetD.%GetData(1) _"</td><td>"_ rsetD.%GetData(2) _"</td><td>"_ STS _"</td></tr>"
                   
                                                
                        }
                        return dtbl
                 }
                 return ""
}

// Set Current FHIR Server

ClassMethod SetFhirServer(serverid As %Integer)
{
	Set obj = ##class(dc.FhirServer).%OpenId(^ActiveFhirServer)
	//If Server is already register then activate it
	if $isobject(obj)  
	{
		Set ^ActiveFhirServer = serverid
		Write "Server id "+serverid+" Activated Successfully"
	}
	ELSE
	{
		Write "FHIR Server with id "+serverid+" Not registered!"
	}
}

// Count Resource, Pass "ALL" in case of counting all the resources

ClassMethod CountResource(resource As %String) As %Integer
{
	//Get Active Server data based on Global Variable 
	Set obj = ##class(dc.FhirServer).%OpenId(^ActiveFhirServer)
	//If Url and ApiKey is defined
	if $isobject(obj)  
	{  
	    
	  try {
  		  //Importing python file 
          Set irisfhirclient = ##class(%SYS.Python).Import("irisfhirclient")
          
		} 
	  Catch err {
			Write "Error While importing irisfhirclient.py file" 	
			return 0  	
				}  
	  //invoking Method from python file
	  Set count = irisfhirclient.CountResource(resource,obj.Endpoint,obj.ApiKey)
	  return count
	}
	//Active Server data is not defined
  	else
  	{ 
  		Quit "Not able to get server Info.."
  	}
  	return count
}

// Count Patient Resources

ClassMethod CountResourcePatient(resource As %String, patientid As %String) As %Integer
{
	//Get Active Server data based on Global Variable 
	Set obj = ##class(dc.FhirServer).%OpenId(^ActiveFhirServer)
	//If Url and ApiKey is defined
	if $isobject(obj)  
	{  
	    
	  try {
  		  //Importing python file 
          Set irisfhirclient = ##class(%SYS.Python).Import("irisfhirclient")
          
		} 
	  Catch err {
			Write "Error While importing irisfhirclient.py file" 	
			return 0  	
				}  
	  //invoking Method from python file
	  Set count = irisfhirclient.CountResourcePatient(resource,patientid,obj.Endpoint,obj.ApiKey)
	  return count
	}
	//Active Server data is not defined
  	else
  	{ 
  		Quit "Not able to get server Info.."
  	}
  	return count
}

// Method invoked from CSP Application to get Resource HTML

ClassMethod GetResourceHTML(resource As %String) As %Status
{
	//Get Active Server data based on Global Variable 
	Set obj = ##class(dc.FhirServer).%OpenId(^ActiveFhirServer)
	//If Url and ApiKey is defined
	if $isobject(obj)  
	{  
	  //Call Embedded Python Function to get Number of Resources
	  Set irisfhirclient = ##class(%SYS.Python).Import("irisfhirclient")
	  Set data = irisfhirclient.GetResourceHTML(resource,obj.Endpoint,obj.ApiKey) 
	  

	}
	//Active Server data is not defined
  	else
  	{ 
  		Quit "Not able to get server Info.."
  	}
  	return data
}

// Get Resource List 

ClassMethod GetResource(resource As %String) As %Status
{
	//Get Active Server data based on Global Variable 
	Set obj = ##class(dc.FhirServer).%OpenId(^ActiveFhirServer)
	//If Url and ApiKey is defined
	if $isobject(obj)  
	{  
	  //Call Embedded Python Function to get Number of Resources
	  Set irisfhirclient = ##class(%SYS.Python).Import("irisfhirclient")
	  do irisfhirclient.GetResource(resource,obj.Endpoint,obj.ApiKey) 
	}
	//Active Server data is not defined
  	else
  	{ 
  		Quit "Not able to get server Info.."
  	}
  	Quit $$$OK
}

//  Get Patint Resources List 

ClassMethod GetPatientResources(resource As %String, patientId As %Integer) As %Status
{
	//Get Active Server data based on Global Variable 
	Set obj = ##class(dc.FhirServer).%OpenId(^ActiveFhirServer)
	//If Url and ApiKey is defined
	if $isobject(obj)  
	{  
	  //Call Embedded Python Function to get Number of Resources
	  Set irisfhirclient = ##class(%SYS.Python).Import("irisfhirclient")
	  do irisfhirclient.GetPatientResources(resource,patientId,obj.Endpoint,obj.ApiKey) 
	}
	//Active Server data is not defined
  	else
  	{ 
  		Quit "Not able to get server Info.."
  	}
  	Quit $$$OK
}

// Get patient data to be used in csp application

ClassMethod GetPatientResourcesHTML(resource As %String, patientId As %Integer) As %Status
{
	//Get Active Server data based on Global Variable 
	Set obj = ##class(dc.FhirServer).%OpenId(^ActiveFhirServer)
	//If Url and ApiKey is defined
	if $isobject(obj)  
	{  
	  //Call Embedded Python Function to get Number of Resources
	  Set irisfhirclient = ##class(%SYS.Python).Import("irisfhirclient")
	  set data = irisfhirclient.GetPatientResourcesHTML(resource,patientId,obj.Endpoint,obj.ApiKey) 
	}
	//Active Server data is not defined
  	else
  	{ 
  		Quit "Not able to get server Info.."
  	}
  	return data
}

// Function to get tables header row based on resource

ClassMethod GetHeaderRow(id As %Integer) As %String
{
    if id = 1 
	{
		//Patients Header
		SET hrow = "<th>ID</th><th>Family Name</th><th>Given Name</th><th>DOB</th><th>Gender</th>"
	}
	elseif id = 2
	{
		//Server Header
		SET hrow = "<th>ID</th><th>Server Name</th><th>Status</th>"
	}
	elseif id = 3
	{
		//Observation
	
		SET hrow = "<th>ID</th><th>Category</th><th>Codes</th><th>Value</th><th>UOM</th><th>Date</th>"
	}

    RETURN hrow
}

}
