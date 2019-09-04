## Database Library Format

Unlike the schematic library (SchLib) and PCB library (PcbLib) files in Altium, database library (DbLib) files are plain text. If you use Altium to create an empty DbLib file, the biolerplate is as follows:

```
[OutputDatabaseLinkFile]
Version=1.1
[DatabaseLinks]
ConnectionString=
AddMode=3
RemoveMode=1
UpdateMode=2
ViewMode=0
LeftQuote=[
RightQuote=]
QuoteTableNames=1
UseTableSchemaName=0
DefaultColumnType=VARCHAR(255)
LibraryDatabaseType=Microsoft Access
LibraryDatabasePath=
DatabasePathRelative=0
TopPanelCollapsed=0
LibrarySearchPath=
OrcadMultiValueDelimiter=,
SearchSubDirectories=0
SchemaName=
```

Altium relies on an [ODBC interface](https://en.wikipedia.org/wiki/Open_Database_Connectivity) to talk to databases and so in order to add new ones, an _ODBC driver_ is required to translate ODBC API calls into something the database understands. The [Altium_PassiveSMT_DbLib][https://github.com/mikef5410/Altium_PassiveSMT_DbLib] repo shares some useful insights into how to connect DbLibs to non-microsoft databases, specifically SQLite3. 

> This library uses SQLite3, so you need to install a "data source" for SQLite3
> before you can use it. You can get it from: http://www.ch-werner.de/sqliteodbc/
> 
> In particular, you want: http://www.ch-werner.de/sqliteodbc/sqliteodbc.exe
> 
> Install it, and re-start Altium.

It's definitely worth mentioning that **sqliteodbc** is a BSD-licensed, open-source project.

Once installed you can use Altium to create the connection string:

![Data Link Provider](assets/data-link_provider_odbc.png?raw=true)
![Connection to SQLite 3](assets/data-link_conn_sqlite3.png?raw=true)
![Advanced settings](assets/data-link_conn_driver-connect.png?raw=true)

Another option is edit the connection string that mikef5410 provided in his repository directly:

`ConnectionString=Provider=MSDASQL.1;Persist Security Info=False;Extended Properties="DSN=SQLite3 Datasource;Database=Z:\projects\MF_CAD\PassiveSMT\PassiveSMT.db;StepAPI=0;SyncPragma=NORMAL;NoTXN=0;Timeout=100000;ShortNames=0;LongNames=0;NoCreat=0;NoWCHAR=0;FKSupport=0;JournalMode=;OEMCP=0;LoadExt=;BigInt=0;JDConv=0;"`


