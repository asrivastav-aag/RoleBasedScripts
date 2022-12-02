#!/usr/bin/env python
class FilterModule:

    def filters(cpu5secload):
        return {
            'cpu5secload' : FilterModule.cpu5secload, 
            'cpu1minload': FilterModule.cpu1minload, 
            'cpu5minload': FilterModule.cpu5minload,
            'LoadConsumingProcess' : FilterModule.LoadConsumingProcess
            }
    
    def cpu5secload (cpu_sorted_data):
        cpu5secload = cpu_sorted_data['five_sec_cpu_total']
        return cpu5secload

    def cpu1minload (cpu_sorted_data):
        cpu1minload = cpu_sorted_data['one_min_cpu']
        return cpu1minload

    def cpu5minload (cpu_sorted_data):
        cpu5minload = cpu_sorted_data['five_min_cpu']
        return cpu5minload

    def LoadConsumingProcess (cpu_sorted_data):
        top_processes = {}
        cpu_sorted = cpu_sorted_data['sort']
        for dic_key in cpu_sorted:
            if cpu_sorted[dic_key]['five_min_cpu'] >= 40.00:
                top_processes.update({cpu_sorted[dic_key]['process']:cpu_sorted[dic_key]['five_min_cpu']})
        
        if len(top_processes) == 0:
            top_processes.update({"None":"None"})

        return top_processes