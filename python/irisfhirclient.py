import sys,json
from fhirpy import SyncFHIRClient
from json import dump
from tabulate import tabulate
import requests

resources = ["Patient", "Observation", "Appointment","Procedure","Practitioner"]
contentType = "application/fhir+json"

# 1-Count Number of Resources
def CountResource(resource,url,api_key):
    #Init headers
    headers={"Content-Type":contentType,"x-api-key":api_key}
    #Add / at the end of endpoint if not added
    if url[-1]!="/":
        url=url+"/"
    try:
        #Get Request 
        req = requests.get(url+resource+'/',headers=headers)  
    except:
        #in case of exception return 0
        return 0
        
    data=req.json()
    #count number of element entry
    count = len(data['entry'])
    return count


#Get Table header based on resource
def GetTableHeader(resource):
    if resource == "Patient":
        header = ["ID","Family Name","Given Name","DOB","Gender"]
    elif resource == "Observation":
        header = ["ID","Category","Code","Value","UOM","Date","Patient"]
    elif resource == "Procedure":
        header = ["ID","Code","Details","StartDate","EndDate","Status"]    
    elif resource == "Immunization":
        header = ["ID","VaccineCode","Details","Date","Encounter","Status"]    
    elif resource == "Encounter":
        header = ["ID","Class","StartDate","EndDate","Provider","Status"]    
    elif resource == "Organization":
        header = ["ID","Code","Details","Name"]   
    elif resource == "Condition":
        header = ["ID","Code","Details","ClinicalStatus","VerificationStatus"]    
    elif resource == "Practitioner":
        header = ["ID","Name","Gender"]     

        #AllergyIntolerance,DiagnosticReport,Claim

    return header

def GetTableData(resource,data,opt):
    rows = []
    if opt == 1: #Get Rows Data
        if resource == "Patient":
            for rowval in data:
                row = [rowval.get('id'),rowval.get_by_path('name.0.family'),rowval.get_by_path('name.0.given.0'),rowval.get_by_path('birthDate'),rowval.get_by_path('gender')]
                rows.append(row)
        elif resource == "Observation":
            for rowval in data:
                row = [rowval.get('id'),
                rowval.get_by_path('category.0.coding.0.code'),
                rowval.get_by_path('code.coding.0.code'),
                rowval.get_by_path('valueQuantity.value'),
                rowval.get_by_path('valueQuantity.code'),
                rowval.get('effectiveDateTime'),
                rowval.get_by_path('subject.reference')
                ,]
                rows.append(row)    
        elif resource == 'Procedure':        
            for rowval in data:
                row = [rowval.get('id'),
                rowval.get_by_path('code.coding.0.code'),
                rowval.get_by_path('code.coding.0.display'),
                rowval.get_by_path('performedPeriod.start'),
                rowval.get_by_path('performedPeriod.end'),
                rowval.get_by_path('status')           
                ]
                rows.append(row)    
        elif resource == 'Immunization':        
            for rowval in data:
                row = [rowval.get('id'),
                rowval.get_by_path('vaccineCode.coding.0.code'),
                rowval.get_by_path('vaccineCode.coding.0.display'),
                rowval.get('occurrenceDateTime'),
                rowval.get_by_path('encounter.reference'),
                rowval.get_by_path('status')           
                ]
                rows.append(row) 
        elif resource == 'Encounter':        
            for rowval in data:
                row = [rowval.get('id'),
                rowval.get_by_path('class.code'),
                rowval.get_by_path('period.start'),
                rowval.get_by_path('period.end'),
                rowval.get_by_path('serviceProvider.reference'),
                rowval.get_by_path('status')           
                ]
                rows.append(row)  
        elif resource == 'Organization':        
            for rowval in data:
                row = [rowval.get('id'),
                rowval.get_by_path('type.0.coding.0.code'),
                rowval.get_by_path('type.0.coding.0.display'),
                rowval.get('name')           
                ]
                rows.append(row)     
        elif resource == 'Condition':        
            for rowval in data:
                row = [rowval.get('id'),
                rowval.get_by_path('code.coding.0.code'),
                rowval.get_by_path('code.coding.0.display'),
                rowval.get_by_path('clinicalStatus.coding.0.code'),           
                rowval.get_by_path('verificationStatus.coding.0.code')           
                ]
                rows.append(row)     
        elif resource == 'Practitioner':        
            for rowval in data:
                row = [rowval.get('id'),
                rowval.get_by_path('name.0.prefix.0')+' '+rowval.get_by_path('name.0.family')+' '+rowval.get_by_path('name.0.given.0'),
                rowval.get('gender')           
                ]
                rows.append(row)             
                
         
                
                                                                          
    elif opt == 2: #Get HTML Data
        rows = ''
        if resource == "Patient":
            for rowval in data:
                row = "<tr><td>"+rowval.get('id')+"</td><td>"+rowval.get_by_path('name.0.family')+"</td><td>"+rowval.get_by_path('name.0.given.0')+"</td><td>"+rowval.get_by_path('birthDate')+"</td><td>"+rowval.get_by_path('gender')+"</td></tr>"
                rows= rows + row
        elif resource == "Observation":
            for rowval in data:
                row = "<tr><td>"+rowval.get('id')+"</td>"
                row = row +"<td>"+ rowval.get_by_path('category.0.coding.0.code') + "</td>"
                row = row +"<td>"+ rowval.get_by_path('code.coding.0.code') + "</td>"
                row = row +"<td>"+ str(rowval.get_by_path('valueQuantity.value')) + "</td>"
                row = row +"<td>"+ str(rowval.get_by_path('valueQuantity.code')) + "</td>"
                row = row +"<td>"+ rowval.get('effectiveDateTime') + "</td>"
                row = row +"<td>"+ rowval.get_by_path('subject.reference') + "</td></tr>"        
                rows = rows + row
        elif resource == "Procedure":
            for rowval in data:
                row = "<tr><td>"+rowval.get('id')+"</td>"
                row = row +"<td>"+ rowval.get_by_path('code.coding.0.code') + "</td>"
                row = row +"<td>"+ rowval.get_by_path('code.coding.0.display') + "</td>"
                row = row +"<td>"+ rowval.get_by_path('performedPeriod.start') + "</td>"
                row = row +"<td>"+ rowval.get_by_path('performedPeriod.end') + "</td>"
                row = row +"<td>"+  rowval.get_by_path('status') + "</td></tr>"        
                rows = rows + row   
        elif resource == "Immunization":
            for rowval in data:
                row = "<tr><td>"+rowval.get('id')+"</td>"
                row = row +"<td>"+ rowval.get_by_path('vaccineCode.coding.0.code') + "</td>"
                row = row +"<td>"+ rowval.get_by_path('vaccineCode.coding.0.display') + "</td>"
                row = row +"<td>"+ rowval.get('occurrenceDateTime') + "</td>"
                row = row +"<td>"+ rowval.get_by_path('encounter.reference') + "</td>"
                row = row +"<td>"+  rowval.get_by_path('status') + "</td></tr>"        
                rows = rows + row    
        elif resource == "Encounter":
            for rowval in data:
                row = "<tr><td>"+rowval.get('id')+"</td>"
                row = row +"<td>"+ rowval.get_by_path('class.code') + "</td>"
                row = row +"<td>"+ rowval.get_by_path('period.start') + "</td>"
                row = row +"<td>"+ rowval.get_by_path('period.end') + "</td>"
                row = row +"<td>"+ rowval.get_by_path('serviceProvider.reference') + "</td>"
                row = row +"<td>"+  rowval.get_by_path('status') + "</td></tr>"        
                rows = rows + row   
        elif resource == "Organization":
            for rowval in data:
                row = "<tr><td>"+rowval.get('id')+"</td>"
                row = row +"<td>"+ rowval.get_by_path('type.0.coding.0.code') + "</td>"
                row = row +"<td>"+ rowval.get_by_path('type.0.coding.0.display') + "</td>"
                row = row +"<td>"+  rowval.get_by_path('name') + "</td></tr>"        
                rows = rows + row                                                                                          
    return rows


#2-Print patient resource from terminal
def GetResource(resource,url,api_key):
    #Get Connection
    cclient = SyncFHIRClient(url = url, extra_headers={"Content-Type":contentType,"x-api-key":api_key})
    try:
        data = cclient.resources(resource).fetch()
    except:
        print("Connection Error")    
          
    header = GetTableHeader(resource)
    rows = GetTableData(resource,data,1)
    #Print Resources
    print(tabulate(rows,headers = header))
    
#3-Print resource agaisnt Patient
def GetPatientResources(resource,patientId,url,api_key):
     #Get Connection
    cclient = SyncFHIRClient(url = url, extra_headers={"Content-Type":contentType,"x-api-key":api_key})
    try:
        data = cclient.resources(resource).search(patient=patientId).fetch()
    except:
        print("Connection Error")    
    header = GetTableHeader(resource)
    rows = GetTableData(resource,data,1)
    #Print Resources
    print(tabulate(rows,headers = header))

#Get Resource HTML Rows data
def GetResourceHTML(resource,url,api_key):
    #Get Connection
    cclient = SyncFHIRClient(url = url, extra_headers={"Content-Type":contentType,"x-api-key":api_key})
    try:
        data = cclient.resources(resource).fetch()
    except:
        print("Connection Error")    
    
    rows = GetTableData(resource,data,1)
    rows = tabulate(rows, tablefmt='html')
    return rows



