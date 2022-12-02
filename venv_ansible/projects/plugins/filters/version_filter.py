#!/usr/bin/env python
class FilterModule:

    def filters(BasicInfo):
        return {
            'BasicInfo' : FilterModule.BasicInfo, 
            'TotalStackMembers': FilterModule.TotalStackMembers, 
            'HardwareDetails': FilterModule.HardwareDetails,
            }
    
    def BasicInfo (version_data):
        version = version_data['version']
        final_data = {}
        final_data.update(
            {
                "Hardware Platform": version['platform'],
                "Hardware Chassis" : version['chassis'],
                "OS Type" : version['os'],
                "IOS Version":version['version'],
                }
                )
        
        return final_data

    def TotalStackMembers (version_data):
        version = version_data['version']['switch_num']
        stack_members = len(version)

        return stack_members

    def HardwareDetails (version_data):
        version = version_data['version']['switch_num']
        StackMemberDetails = {}
        for keys,values in version.items():
            StackMemberDetails.update({
                "stack_member{}".format(keys):
                {
                    "Model Number" : values['model'],
                    "Serial Number" : values['system_sn'],
                    "Total Network Ports" : values['ports'],
                    "Software Version" : values['sw_ver'],
                    "Installed OS Image": values['sw_image']
                    
                    }
                })
        
        return StackMemberDetails