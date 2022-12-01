#!/usr/bin/env python
class FilterModule:

    def filters(cpu60min):
        return {'cpu60min' : FilterModule.cpu60min, 'cpu72hrs': FilterModule.cpu72hrs, 'cpu60sec': FilterModule.cpu60sec}
    
    def cpu60min (cpu_data):
        cpu60min_max_values = []
        for data in cpu_data['60m']:
            if cpu_data['60m'][data]['maximum'] != 0:
                cpu60min_max_values.append(cpu_data['60m'][data]['maximum'])
        cpu60min_avg = sum(cpu60min_max_values) / len(cpu60min_max_values)

        return int(cpu60min_avg)

    def cpu72hrs (cpu_data):
        cpu72hrs_max_values = []
        for data in cpu_data['72h']:
            if cpu_data['72h'][data]['maximum'] != 0:
                cpu72hrs_max_values.append(cpu_data['72h'][data]['maximum'])
        cpu72hrs_avg = sum(cpu72hrs_max_values) / len(cpu72hrs_max_values)

        return int(cpu72hrs_avg)

    def cpu60sec (cpu_data):
        cpu60sec_max_values = []
        for data in cpu_data['60s']:
            if cpu_data['60s'][data]['maximum'] != 0:
                cpu60sec_max_values.append(cpu_data['60s'][data]['maximum'])
        cpu60sec_avg = sum(cpu60sec_max_values) / len(cpu60sec_max_values)

        return int(cpu60sec_avg)
