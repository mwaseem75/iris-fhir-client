## Summary
InterSystems FHIR Client
Get Resources information from FHIR Server. Command Line utility and Web interface. 

## Application Layout
![image](https://user-images.githubusercontent.com/18219467/149624925-2d779d04-9391-4856-a7a2-c2907d14a70d.png)

## Online Demo
https://medicaldatasets.demo.community.intersystems.com/csp/datasets/index.csp by using SuperUser | SYS

## Datasets List
* [**1 - Synthetic Medical Data**](https://data.world/siyeh/synthetic-medical-data) : Synthetic medical record data for Introduction to Biomedical Data Science. [LICENCE:Public Domain](https://docs.data.world/en/59261-59714-2--Common-license-types-for-datasets.html)
* [**2 - Health Care Analytics - 1**](https://www.kaggle.com/abisheksudarshan/health-care-analytics) : Part of Janatahack Hackathon in Analytics Vidhya [LICENCE:Public Domain](https://docs.data.world/en/59261-59714-2--Common-license-types-for-datasets.html)

## Features
* Retrieve all the resource list
* Retrieve already defined resources
* List Resource details
* List Resource details from command prompt and from web interface
* Patient and Observation resource CRUD operations
* Interoperability PEX
* Programatically add any open source FHIR Web server
* Smart on FHIR application details

## Recommendation 
 * Read related documentations [LOAD DATA (SQL)](https://irisdocs.intersystems.com/iris20212/csp/docbook/DocBook.UI.Page.cls?KEY=RSQL_loaddata).


## How to Run

To start coding with this repo, you do the following:

1. Clone/git pull the repo into any local directory

```shell
git clone https://github.com/mwaseem75/DataSetProj.git
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
zpm "install dataset-medical"
```
## Repo Contents   
* Dockerfile, docker-compose.yml, and Installer.cls to create container
* iris.script, contains script to execute during container initialization 
* /src with source files 
* /.vscode/settings.json for automatic server connections when opened in VS Code.

## Requirements:  
* [Docker desktop]( https://www.docker.com/products/docker-desktop)
* Get the latest InterSystems IRIS for Health image for use in the Dockerfile: https://hub.docker.com/_/intersystems-iris-for-health  

## Getting Started 
## Importing DataSet from Terminal
###### Connect to IRIS Terminal
```
docker-compose exec iris iris session iris
```
###### Change Namespace to DATASETS
```
ZN "DATASETS"
```
###### Run below command to import Synthetic Medical Data dataset by passing dataset ID(1) 
```
do ##class(dc.data.medical.utility).ImportDS(1)
```
![image](https://user-images.githubusercontent.com/18219467/149458527-4aa1e5fe-bcc0-4d77-a6b8-c2997d98ebb6.png)
**11** Tables are created, **83,341** Records Loaded successfully, **140** errors Reported
## Use of %SQL_Diag.Result and %SQL_Diag.Message to check errors
As you noticed previous LOAD DATA returns **140** errors. To check the error details we will use %SQL_Diag.Result and %SQL_Diag.Message tables. We need diag ID to check detail which in our case is **5** (Last column in previous snapshot)
###### We will use Management Portal SQL to check the details
Open Management Portal SQL and type below SQL command to check details in %SQL_Diag.Result table against Diag ID
```
SELECT * FROM %SQL_Diag.Result WHERE ID = 5
```
![image](https://user-images.githubusercontent.com/18219467/148871787-d1cf2c02-1028-4523-947d-3f85b65480ad.png)
and to check the details of 140 errors type below SQL command
```
SELECT * FROM %SQL_Diag.Message WHERE severity = 'error' and diagResult = 5
```
![image](https://user-images.githubusercontent.com/18219467/148872183-61cb2c2d-d708-4d3e-87e4-e0e9a7727079.png)
System is displaying details of **140** errors. Please note that we are passing same %SQL_Diag.Result ID to diagResulg column 

## Importing DataSet from Web Application
Navigate to [http://localhost:52773/csp/datasets/index.csp](http://localhost:52773/csp/datasets/index.csp) and press Install DataSet button
![image](https://user-images.githubusercontent.com/18219467/148712707-f4dc38ec-d86b-4df2-8b8c-2ea2235a57c7.png)
![image](https://user-images.githubusercontent.com/18219467/148711619-c01c3207-b30f-45c9-9c42-a861ea008062.png)
###### Dataset is imported successfully
![image](https://user-images.githubusercontent.com/18219467/148711723-21bd863e-a0a0-4fa6-a49e-a0ce080afc8a.png)

## View Data from Web Application
###### Navigate to [http://localhost:52773/csp/datasets/index.csp](http://localhost:52773/csp/datasets/index.csp) and click any table from sidebar
![image](https://user-images.githubusercontent.com/18219467/148712249-b6b2fbd9-2170-467a-8388-3e3e6eba5bfa.png)

## Export Data from Web Application
###### Navigate to View Datasets and select particular dataset, click Excel,CSV or PDF button to export data
![image](https://user-images.githubusercontent.com/18219467/148712475-6a672123-4ed0-410c-8d67-c01aeb644f61.png)


## Removing DataSet from Terminal
###### Run below command to Remove Synthetic Medical Data dataset by passing dataset ID(1) 
```
do ##class(dc.data.medical.utility).RemoveDS(1)
```
![image](https://user-images.githubusercontent.com/18219467/148712878-7737f908-e6ac-4d01-ab24-db62394f7f10.png)

## Removing DataSet from Web Application
###### Navigate to [http://localhost:52773/csp/datasets/index.csp](http://localhost:52773/csp/datasets/index.csp) and press Remove DataSet button
![image](https://user-images.githubusercontent.com/18219467/148713154-009dac5d-3f7d-4e57-bbc2-72ba7f1589ba.png)
###### Dataset is removed successfully
![image](https://user-images.githubusercontent.com/18219467/148713212-d094cf64-7b8e-4879-aaf8-30cb65ce49d0.png)


## Importing all DataSets at once
###### Run below command to Import all datasets by passing ID 999 
```
do ##class(dc.data.medical.utility).ImportDS(999)
```
![image](https://user-images.githubusercontent.com/18219467/148715361-9ffc5517-f579-4e16-931f-a3b9a170f4e9.png)


## Removing all DataSets at once
###### Run below command to Remove all datasets by passing ID 999 
```
do ##class(dc.data.medical.utility).RemoveDS(999)
```
![image](https://user-images.githubusercontent.com/18219467/148715463-4318a20b-16b6-473f-86b5-b458a2916da6.png)


## Check Status of DataSet
###### Run below command to check the status of particular DataSet by passing DataSet ID, 
```
do ##class(dc.data.medical.utility).GetStatusDS(1)
```
![image](https://user-images.githubusercontent.com/18219467/148715890-6942031a-bd8d-4e96-a20a-4580910eb394.png)
###### Run below command to check the status of all Datasets
```
do ##class(dc.data.medical.utility).GetStatusDS(999)
```

## Other information
Template used in web application is from [Bootstrap 4 Admin Dashboard](https://github.com/themekita/Atlantis-Lite) and it is free to use to develop non-commercial applications.


## Thanks