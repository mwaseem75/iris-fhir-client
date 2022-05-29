## Summary
InterSystems FHIR Client
Connect to any Open FHIR Server and get Resources information from FHIR Server, Both from terminal and form website. 

## Application Layout
![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/18219467/170888223-51e31519-92af-446f-acae-0633df885dbe.gif)


## Features
* Register Any Open FHIR Server
* Retrieve resources
* List Resource details
* List Resource details from command prompt and from web interface
* Programatically add any open source FHIR Web server

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


## Other information
Template used in web application is from [Bootstrap 4 Admin Dashboard](https://github.com/themekita/Atlantis-Lite) and it is free to use to develop non-commercial applications.


## Thanks
