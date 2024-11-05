Class dc.FhirServer Extends %Persistent
{

Property ServerName As %String;

Property Endpoint As %String(MAXLEN = 200);

Property ApiKey As %String;

Property EndpointOAuth As %String(MAXLEN = 200);

Storage Default
{
<Data name="FhirServerDefaultData">
<Value name="1">
<Value>%%CLASSNAME</Value>
</Value>
<Value name="2">
<Value>ServerName</Value>
</Value>
<Value name="3">
<Value>Endpoint</Value>
</Value>
<Value name="4">
<Value>ApiKey</Value>
</Value>
<Value name="5">
<Value>EndpointOAuth</Value>
</Value>
</Data>
<DataLocation>^dc.FhirServerD</DataLocation>
<DefaultData>FhirServerDefaultData</DefaultData>
<ExtentSize>1</ExtentSize>
<IdLocation>^dc.FhirServerD</IdLocation>
<IndexLocation>^dc.FhirServerI</IndexLocation>
<Property name="%%CLASSNAME">
<AverageFieldSize>2</AverageFieldSize>
<OutlierSelectivity>.999999:</OutlierSelectivity>
<Selectivity>0.0001%</Selectivity>
</Property>
<Property name="%%ID">
<AverageFieldSize>3</AverageFieldSize>
<Selectivity>1</Selectivity>
</Property>
<Property name="ApiKey">
<AverageFieldSize>2</AverageFieldSize>
<OutlierSelectivity>.999999:</OutlierSelectivity>
<Selectivity>0.0001%</Selectivity>
</Property>
<Property name="Endpoint">
<AverageFieldSize>30</AverageFieldSize>
<OutlierSelectivity>.999999:"https://r4.smarthealthit.org"</OutlierSelectivity>
<Selectivity>0.0001%</Selectivity>
</Property>
<Property name="EndpointOAuth">
<AverageFieldSize>2</AverageFieldSize>
<OutlierSelectivity>.999999:</OutlierSelectivity>
<Selectivity>0.0001%</Selectivity>
</Property>
<Property name="ServerName">
<AverageFieldSize>32</AverageFieldSize>
<OutlierSelectivity>.999999:"SmartHealthIT Open FHIR Server"</OutlierSelectivity>
<Selectivity>0.0001%</Selectivity>
</Property>
<SQLMap name="IDKEY">
<BlockCount>-4</BlockCount>
</SQLMap>
<StreamLocation>^dc.FhirServerS</StreamLocation>
<Type>%Storage.Persistent</Type>
}

}
