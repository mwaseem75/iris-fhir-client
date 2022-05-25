Class dc.FhirServer
{

Property ServerName As %String;

Property Url As %String(MAXLEN = 200);

Property ApiKey As %String;

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
<Value>Url</Value>
</Value>
<Value name="4">
<Value>ApiKey</Value>
</Value>
</Data>
<DataLocation>^dc.FhirServerD</DataLocation>
<DefaultData>FhirServerDefaultData</DefaultData>
<ExtentSize>7</ExtentSize>
<IdLocation>^dc.FhirServerD</IdLocation>
<IndexLocation>^dc.FhirServerI</IndexLocation>
<Property name="%%CLASSNAME">
<AverageFieldSize>2</AverageFieldSize>
<Selectivity>100.0000%</Selectivity>
</Property>
<Property name="%%ID">
<AverageFieldSize>3</AverageFieldSize>
<Selectivity>1</Selectivity>
</Property>
<Property name="ApiKey">
<AverageFieldSize>7.71</AverageFieldSize>
<OutlierSelectivity>.857143:</OutlierSelectivity>
<Selectivity>14.2857%</Selectivity>
</Property>
<Property name="ServerName">
<AverageFieldSize>13.71</AverageFieldSize>
<Selectivity>16.6667%</Selectivity>
</Property>
<Property name="Url">
<AverageFieldSize>30.14</AverageFieldSize>
<Selectivity>20.0000%</Selectivity>
</Property>
<SQLMap name="IDKEY">
<BlockCount>-4</BlockCount>
</SQLMap>
<StreamLocation>^dc.FhirServerS</StreamLocation>
<Type>%Storage.Persistent</Type>
}

}
