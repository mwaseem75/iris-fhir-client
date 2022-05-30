## Summary
InterSystems FHIR Client to connect any open FHIR Server by using embedded python with the help of [**fhirpy**](https://pypi.org/project/fhirpy/) Library.  
Get Resource information by terminal and by using CSP web application.

## Application Layout
![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/18219467/170888223-51e31519-92af-446f-acae-0633df885dbe.gif)


## Features
* Register and Connect to any open FHIR Server
* InterSystem FHIR Accelerator Service and SmartHealthIT Open FHIR Server are registered by default and ready to use
* Get Resources information by providing resource
* Get Resources details by all or by Patient
* List Resource details from command prompt and from web interface
* Programatically add any open source FHIR server

## Recommendation 
 * Read related documentations [HL7 FHIR ](https://www.hl7.org/fhir/)
 * Python FHIR Client [fhirpy](https://pypi.org/project/fhirpy/)


## How to Run

To start coding with this repo, you do the following:

1. Clone/git pull the repo into any local directory

```shell
git clone https://github.com/mwaseem75/iris-fhir-client.git
```

2. Open the terminal in this directory and run:

```shell
docker-compose build
```

3. Run the IRIS container with your project:

```shell
docker-compose up -d
```
## Installation with ZPM
```
zpm "install iris-fhir-client"
```
## Repo Contents   
* Dockerfile, docker-compose.yml, and Installer.cls to create container
* iris.script, contains script to execute during container initialization 
* /src with source files of classes and CSP application 
* /python with python source files 
* /.vscode/settings.json for automatic server connections when opened in VS Code.

## Requirements:  
* [Docker desktop]( https://www.docker.com/products/docker-desktop)
* Get the latest InterSystems IRIS for Health image for use in the Dockerfile: https://hub.docker.com/_/intersystems-iris-for-health  

## Getting Started 
## Registered FHIR Servers
###### Connect to IRIS Terminal
```
docker-compose exec iris iris session iris
```
###### To list down registered server use ServerList() of dc.FhirClient class
```
do ##class(dc.FhirClient).ServerList()
```
![image](https://user-images.githubusercontent.com/18219467/170888825-7d655866-3a8b-4322-9b64-1ccf0b1ffbf4.png)

###### To Register New Server use RegisterServer() function of dc.FhirClient class
###### class(dc.FhirClient).RegsterServer("Server Name","Endpoint","ApiKey"[optional],"EndpointOAuth"[optional]
To Register New Server use RegisterServer class method
```
do ##class(dc.FhirClient).RegisterServer("INTERSYSTEMS FHIR Server","http://localhost:52773/csp/healthshare/samples/fhir/r4/","","")
```
![image](https://user-images.githubusercontent.com/18219467/170890315-48ed8172-4c1a-4c22-9794-dad2e6c0d277.png)


###### To Activate server, call below method by passing server ID
```
do ##class(dc.FhirClient).SetFhirServer(2)
```
## Get Resources from the FHIR Servers
###### To Retrieve all the resouces for the current server use ListResources() method of dc.FhirClient class
```
do ##class(dc.FhirClient).ListResources()
```
![image](https://user-images.githubusercontent.com/18219467/170890855-891bf5eb-a724-4297-8bcb-821637a146f5.png)

###### In order to display number of recordes of any resources use CountResource() method by passing Resource of dc.FhirClient
###### Below command will get counter of Patient Resource against active FHIR Server
```
set count = ##class(dc.FhirClient).CountResource("Patient")
write count
```


###### To Retrieve all the created Resources along with their count just pass 1 to ListResource() function
```
do ##class(dc.FhirClient).ListResources(1)
```
![image](https://user-images.githubusercontent.com/18219467/170890718-1dacba2c-4d2d-4830-8606-be0542230afb.png)


###### To get details of the resource use GetResource() by passing Resource of dc.FhirClient class
###### Below command will retrieve all the Patients from the active FHIR Server
```
do ##class(dc.FhirClient).GetResource("Patient")
```
![image](https://user-images.githubusercontent.com/18219467/170890728-7fb7d8a3-4c33-4084-8f54-6ca772b60a41.png)
###### Below command will retrieve all the Observations from the active FHIR Server
```
do ##class(dc.FhirClient).GetResource("Observation")
```
![image](https://user-images.githubusercontent.com/18219467/170890999-9548988e-40e7-49c1-ad7f-f95d45f62b50.png)

## Get Resources for particular patient from the FHIR Servers
###### Below command will retrieve Observations detail against Patinet ID 1 from the active FHIR Server
```
do ##class(dc.FhirClient).GetPatientResources("Observation","1")
```
![image](https://user-images.githubusercontent.com/18219467/170956427-4b46797d-45ce-49af-996d-465a2239d73c.png)

###### Below command will retrieve detail of Encounters against Patinet ID 1 from the active FHIR Server
```
do ##class(dc.FhirClient).GetPatientResources("Encounter","1")
```
![image](https://user-images.githubusercontent.com/18219467/170956695-ec3a396a-580c-41dc-b9f1-d5465a4a3653.png)


## Other information
Template used in web application is from [Bootstrap 4 Admin Dashboard](https://github.com/themekita/Atlantis-Lite) and it is free to use to develop non-commercial applications.


## Thanks
