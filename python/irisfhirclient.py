import sys,json
from fhirpy import SyncFHIRClient
from json import dump
from tabulate import tabulate
import requests

#url = "https://r4.smarthealthit.org"
url = "http://localhost:52773/csp/healthshare/samples/fhir/r4"

#url = "https://fhir.83z8498j30i6.static-test-account.isccloud.io"
api_key = "CDqtU2GjQUaICOC65Ilgv1LHQIEDr4Vn12nnlmMY"
client = SyncFHIRClient(url = url, extra_headers={"Content-Type":"application/fhir+json","x-api-key":api_key})
headers={"Content-Type":"application/fhir+json","x-api-key":api_key}
resources = ["Patient", "Observation", "Appointment","Procedure","Practitioner"]
contentType = "application/fhir+json"

def hello():
   return "HelloFromPython"
# def meanage():
#     observation = client.resource(
#     'Observation',
#     status='preliminary',
#     category=[{
#         'coding': [{
#             'system': 'http://hl7.org/fhir/observation-category',
#             'code': 'vital-signs'
#         }]
#     }],
#     code={
#         'coding': [{
#             'system': 'http://loinc.org',
#             'code': '8310-5'
#         }]
#     })
#     observation['effectiveDateTime'] = '2018-10-20'
#     observation['valueQuantity'] = {
#     'system': 'http://unitsofmeasure.org',
#     'value': 96.8,
#     'code': 'degF'
#     }

#     patient = client.resources('Patient').search(name=['John', 'Thompson']).first()
#     observation['subject'] = patient.to_reference()
#     observation.save()
#     dump(observation, sys.stdout, indent=2)

# 1-Count Number of Resources
def ResourceCount(resource,url,api_key):
    #Get Connection
    #cclient = SyncFHIRClient(url = url, extra_headers={"Content-Type":contentType,"x-api-key":api_key})
    
    headers={"Content-Type":"application/fhir+json","x-api-key":api_key}
   
    if url[-1]!="/":
        url=url+"/"
    try:
        req = requests.get(url+resource+'/',headers=headers)  
    except:
        #in case of exception return 0
        return 0
        
    data=req.json()
    count = len(data['entry'])
    #In case of all, iterate throuch array of resources
    #if resource.upper() == "ALL":
    #    for resource in resources:
    #        ResourceCount(resource)
    #else:
    #count = cclient.resources(resource).count()
    return count


# Serilize Resource
def ResourceSerialize(resource):		
	resources = client.resources(resource).fetch()
	dump(resources, sys.stdout, indent=2)


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
def ResourceList(resource,url,api_key):
    #Get Connection
    cclient = SyncFHIRClient(url = url, extra_headers={"Content-Type":contentType,"x-api-key":api_key})
    try:
        data = cclient.resources(resource).fetch()
    except:
        print("Connection Error")    
          
    header = GetTableHeader(resource)
    rows = GetTableData(resource,data,1)
    print(tabulate(rows,headers = header))
    
    #print(tabulate(table, tablefmt='html'))

#3-Print resource agaisnt Patient
def ResourceListPatient(resource,patientId,url,api_key):
     #Get Connection
    cclient = SyncFHIRClient(url = url, extra_headers={"Content-Type":contentType,"x-api-key":api_key})
    try:
        data = cclient.resources(resource).search(patient=patientId).fetch()
    except:
        print("Connection Error")    
    header = GetTableHeader(resource)
    rows = GetTableData(resource,data,1)
    print(tabulate(rows,headers = header))

#Get Resource HTML Rows data
def GetResourceList(resource,url,api_key):
    #Get Connection
    cclient = SyncFHIRClient(url = url, extra_headers={"Content-Type":contentType,"x-api-key":api_key})
    try:
        data = cclient.resources(resource).fetch()
    except:
        print("Connection Error")    
    
    rows = GetTableData(resource,data,1)
    rows = tabulate(rows, tablefmt='html')
    return rows

#Get Resource HTML Rows data
def ResourceListHTML(resource,url,api_key):
    #Get Connection
    cclient = SyncFHIRClient(url = url, extra_headers={"Content-Type":contentType,"x-api-key":api_key})
    try:
        data = cclient.resources(resource).fetch()
    except:
        print("Connection Error")    
    
    rows = GetTableData(resource,data,1)
    rows = tabulate(rows, tablefmt='html')
    return rows


# #--Counting all the resources ----------------------------------------------------
# headers = {'content-type': 'application/json'}
# x = requests.get('http://localhost:52773/csp/healthshare/samples/fhir/r4/metadata',headers=headers)
# data = x.json()
# # # rows = []
# # # header = ["Parm","Details"]
# # # row = ["ID",data['id']]
# # # rows.append(row)
# # # row = ["Name",data['name']]
# # # rows.append(row)
# # # row = ["Url",data['url']]
# # # rows.append(row)
# # # row = ["Publisher",data['publisher']]
# # # rows.append(row)
# # # print(tabulate(rows,headers = header))

# # # print (len(data['rest'][0]['resource']))
# for item in data['rest'][0]['resource']: 
#      #print(item['type'])
#      x = requests.get('http://localhost:52773/csp/healthshare/samples/fhir/r4/'+item['type']+'/',headers=headers)  
#      #print(x)
#      data2 = x.json()
#      #print(data2)
#      s = json.dumps(data2)
#      if s.find('entry') != -1:
#          print (item['type'] +":"+str(len(data2['entry'])))
# #########################################################################################


# # Count number of resources
# headers = {'content-type': 'application/json'}
# x = requests.get('http://localhost:52773/csp/healthshare/samples/fhir/r4/Claim/',headers=headers)
# data = x.json()
# print (len(data['entry']))



# for item in data['entry'][0]['resource']['resourceType']: 
#     print(item)


#res[]
#for item in data["rest"]:
#    print(item["resource"])
#   #res.append(store_details)


 
#print("ID = "+ data['id'])
#print("Name = "+ data['name'])
#rint("url = "+ data['url'])
#print("Publisher = "+ data['publisher'])
#PrintResourceList("Practitioner")

# json_data = json.dumps({
#   "result":[
#     {
#       "run":[
#         {
#           "action":"stop"
#         },
#         {
#           "action":"start"
#         },
#         {
#           "action":"start"
#         }
#       ],
#       "find": "true"
#     }
#   ]
# })
#print(x)
#item_dict = json.loads(x)
#print(len(data['entry'][0]['resource']['resourceType']))
#print(data['total'])
#ResourceCount("Patient")
#GetResourceList("Patient")
#patient0 = Patient.parse_obj(patients_resources.search(family='familyname',given='givenname1').first().serialize())




#  Set obj = ##class(MyApp.MyClass).%New()
#  Set obj.MyValue = 10

#  Set sc = obj.%Save()


# try: 
#     rc = ResourceCount("Observation","https://fhir.83z8498j30i6.static-test-account.isccloud.io","CDqtU2GjQUaICOC65Ilgv1LHQIEDr4Vn12nnlmMY")
#     print(rc)
# except:
#     print("Connection Error")    
#print(rc)
#ResourceListPatient("Observation",3,url,api_key)

#ResourceListPatient("Observation","Patient","https://fhir.83z8498j30i6.static-test-account.isccloud.io","CDqtU2GjQUaICOC65Ilgv1LHQIEDr4Vn12nnlmMY")
#rows = GetResourceList("Patient","http://localhost:52773/csp/healthshare/samples/fhir/r4","sdf")
#print(rows)

# ResourceList("Patient","http://localhost:52773/csp/healthshare/samples/fhir/r4","87")
#count number of resources
#https://r4.smarthealthit.org/Patient?_count=5


