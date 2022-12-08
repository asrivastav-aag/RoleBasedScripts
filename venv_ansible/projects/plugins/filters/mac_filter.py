#!/usr/bin/env python
class FilterModule:

    def filters(TotalMACaddr):
        return {
            'TotalMACaddr' : FilterModule.TotalMACaddr,
            'DisplayMACaddr' : FilterModule.DisplayMACaddr,
            'DisplayConnectedMAC' : FilterModule.DisplayConnectedMAC
            }


    def TotalMACaddr (mac_table):
        key_vars = mac_table['mac_table']['vlans']
        mac_list = []
        for keys in key_vars:
            if keys != str('all'):
                for key in key_vars[keys]['mac_addresses']:
                    mac_list.append(key)
        return len(mac_list)


    def DisplayMACaddr (mac_table):
        del mac_table['mac_table']['vlans']['all']
        mac_per_vlan = mac_table['mac_table']['vlans']
        mac_list_dict = {}
        for vlan_keys,vlan_values in mac_per_vlan.items():
            # print(vlan_keys)
            # print(vlan_values['mac_addresses'].keys())
            mac_list_dict.update({
                "VLAN {}".format(vlan_keys) : list(vlan_values['mac_addresses'].keys())
            })
        
        return mac_list_dict


    def DisplayConnectedMAC (mac_table):
        del mac_table['mac_table']['vlans']['all']
        mac_per_vlan = mac_table['mac_table']['vlans']
        mac_inf_dict = {}
        for vlan_values in mac_per_vlan.values():
            for mac_values in vlan_values['mac_addresses'].values():
                for inf_keys in mac_values['interfaces']:
                    if mac_values['interfaces'][inf_keys]['entry_type'] == 'static':
                        mac_inf_dict.update({
                            mac_values['mac_address'] : mac_values['interfaces'][inf_keys]['interface']
                        })
        
        return mac_inf_dict