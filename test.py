from nornir import InitNornir
from nornir_utils.plugins.tasks.data import load_yaml
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_command
import getpass
from datetime import datetime
startTime = datetime.now()

nr = InitNornir(config_file="config.yaml")

# password = getpass.getpass()

# nr.inventory.defaults.password = password


def show_output(task):
    task.run(task=netmiko_send_command, name = "check ip int brief", command_string = "show inventory", use_genie = True)

results = nr.run(task = show_output)

#print_result(results)

for key in results.keys():
    print(results[key][1].result)
    print("next")

# # import ipdb; ipdb.set_trace()

# vrf_devices, dev_failed=[],[]
# for key in results.keys():
# 	if results[key][1].result=='':
# 		pass
# 	elif results[key][1].exception != None:
# 	    dev_failed.append(key)
# 	else:
# 		vrf_devices.append(key)
# print('checking VRF 192')
# print('devices queried: ', len(results.keys()))
# print('devices failed: ', dev_failed)
# print('devices with vrf: ',vrf_devices)

# print((datetime.now() - startTime), 'seconds it took to run the script')
# import ipdb; ipdb.set_trace()
# print(results['BRD-CS-01'][1].changed)
# print(results['BRD-CS-01'][1].diff)
# print(results['BRD-CS-01'][1].result)