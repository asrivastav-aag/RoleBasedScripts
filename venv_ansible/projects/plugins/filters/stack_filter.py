#!/usr/bin/env python
class FilterModule:

    def filters(TotalStackMembers):
        return {
            'TotalStackMembers' : FilterModule.TotalStackMembers, 
            'DisplayStackState': FilterModule.DisplayStackState, 
            }
    
    def TotalStackMembers (stack_data):
        TotalStackMembers = stack_data['switch']['stack']

        return len(TotalStackMembers)


    def DisplayStackState (stack_data):
        stacks_members = stack_data['switch']['stack']
        stack_dict = {}
        port_details = {}
        for keys,values in stacks_members.items():
            i = 1
            while i <= len(stacks_members):
                stack_dict.update({
                    "stacks_member{}".format(keys):
                    {
                        "Stack Priority" : values['priority'],
                        "Stack Member Role" : values['role'],
                        "Stack Member State" : values['state'],
                        "Port Details" : port_details
                    }
                })
                for port_key, port_value in values['ports'].items():
                    j = 1
                    while j <= len(values['ports']):
                        port_details.update({
                            "port{}".format(port_key):
                                {
                                    "Port Status": port_value['stack_port_status']
                                }
                        })
                        j +=1
                i += 1
        
        return stack_dict
        