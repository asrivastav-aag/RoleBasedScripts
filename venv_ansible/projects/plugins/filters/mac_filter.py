#!/usr/bin/env python
class FilterModule:

    def filters(BasicInfo):
        return {
            'TotalMACaddr' : FilterModule.TotalMACaddr
            }
    
    def TotalMACaddr (mac_table):
        key_vars = mac_table['mac_table']['vlans']
        mac_list = []
        for keys in key_vars:
            if keys != str('all'):
                for key in key_vars[keys]['mac_addresses']:
                    mac_list.append(key)
        return len(mac_list)