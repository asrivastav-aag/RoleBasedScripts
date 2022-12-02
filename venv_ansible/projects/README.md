# Role Based Scripts | Perform Complete Health Check for Cisco Switches
## Features

- Logins to Cisco Switches via Paramiko & Local Creds
- Gathers certain Commands output (mentioned in below table) and import them into Variable
- Uses Genie Parser to Parse out the Data in JSON structure
- Uses default & custom Python based filters to display required messages


As I believe...

> CHANGE IS THE PERMANENT CONSTANT

please ping me or add comments on scripts if a script can be betterly modified/written; Or something new can be included.

## Tech

All Script uses:

- Ansible
- Python

## Python Packages Used
- ansible
- paramiko
- ncclient
- 'pyats[full]'
- genie
- pycparser
- colorama

## Ansible Roles Used
- switch_health_check (self/locally initialized)
 

## Ansible Collections Used
- cisco.ios
- clay584.genie

## Plugins, Variables, and Commands Used so far


Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Task Name | Command Used | Description | Variables Used | Pyhon Filters Used |
| ------ | ------ | ------ | ------ | ------ |
| 001Clock.yaml | show clock| Show clock | clock | None |
| 002ConfChange.yaml |show run ! sec Last!NVRAM | Last Configuration Change - Date, time, and who | run_config | None|
| 003Uptime.yaml | show version | Uptime, Last reboot reason, and when was the reboot occurred | Uptime & uptime_data | None|
| 004CPU_History.yaml | show processes cpu history | Processor Load History | cpu & cpu_history | filters/cpu_load.py Cpu60sec, Cpu60min, cpu72hrs|
| 005CPU_Sorted.yaml | show processes cpu sorted | Processor Load Sorted | cpu_sorted | filters/cpu_sorted.py Cpu5secload,cpu5minload, cpu1minload, LoadConsumingProcess|
| 006MemoryUtilization.yaml | show memory statistics | Memory Load | mem_stats, mem_data, free_mem, total_mem | ansible defaults|
| DisplayMessages.yaml | NA | Display All messages in one debug | NA | NA|
| 007HardwareAndSoftwareDetails.yaml | show version | | Hardware Make, Model and Software Version | version | filters/version_filter.py TotalStackMembers, HardwareDetails|