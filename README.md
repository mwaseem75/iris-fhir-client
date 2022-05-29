## Summary
InterSystems FHIR Client to connect any open FHIR Server by using embedded python with the help of [**fhirpy**](https://pypi.org/project/fhirpy/) Library.  
Get Resource details by terminal and by using CSP web application.

## Application Layout
![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/18219467/170888223-51e31519-92af-446f-acae-0633df885dbe.gif)


## Features
* Connect to any open FHIR Server
* InterSystem FHIR Accelerator Service and SmartHealthIT Open FHIR Server are registered by default and ready to use
* Get Resources information
* Get Resources details by Patient
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
* /src with source files 
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
###### To list down registered server
```
do ##class(dc.FhirClient).ServerList()
```
![image](https://user-images.githubusercontent.com/18219467/170888825-7d655866-3a8b-4322-9b64-1ccf0b1ffbf4.png)
###### To Register New Server use RegisterServer class method
###### class(dc.FhirClient).RegsterServer("Server Name","Endpoint","ApiKey"[optional],"EndpointOAuth"[optional]
To Register New Server use RegisterServer class method
```
do ##class(dc.FhirClient).RegisterServer("INTERSYSTEMS FHIR Server","http://localhost:52773/csp/healthshare/samples/fhir/r4/","","")
```
![image](https://user-images.githubusercontent.com/18219467/170890315-48ed8172-4c1a-4c22-9794-dad2e6c0d277.png)


###### To Activate Other server, call below method by passing server ID
```
do ##class(dc.FhirClient).SetFhirServer(2)
```
###### To Retrieve all the resouces for the current server user below command
```
do ##class(dc.FhirClient).ListResources()
```
![image](https://user-images.githubusercontent.com/18219467/170890855-891bf5eb-a724-4297-8bcb-821637a146f5.png)

###### To Retrieve all the created Resources along with there count just pass 1 to ListResource() function
```
do ##class(dc.FhirClient).ListResources(1)
```
![image](https://user-images.githubusercontent.com/18219467/170890718-1dacba2c-4d2d-4830-8606-be0542230afb.png)


###### To get resource list use below command
```
do ##class(dc.FhirClient).GetResource("Patient")
```
![image](https://user-images.githubusercontent.com/18219467/170890728-7fb7d8a3-4c33-4084-8f54-6ca772b60a41.png)

```
do ##class(dc.FhirClient).GetResource("Observation")
```
![image](https://user-images.githubusercontent.com/18219467/170890999-9548988e-40e7-49c1-ad7f-f95d45f62b50.png)


## Other information
Template used in web application is from [Bootstrap 4 Admin Dashboard](https://github.com/themekita/Atlantis-Lite) and it is free to use to develop non-commercial applications.


## Thanks
