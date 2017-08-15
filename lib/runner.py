#!/usr/bin/python
import subprocess

# runs python file_name and pass params from data_list
def cmd_exec(file_name, data_list):
    with open ('data.txt','w') as f:
        f.seek(0)
        for line in data_list:
            f.write(line + '\n')
        f.close()
    command = file_name + " < %s" % f.name
    print(command)
    process = subprocess.Popen(command, shell=True, executable="/bin/bash")
    output, err = process.communicate()
    p_status = process.wait()
    print("Executed command: {}, status: {}".format(command, p_status))
    print('Output: ' + str(output))
    if p_status > 0:
        print("ERROR: Not able to execute:" + command)
    return p_status

def cmd_exec1( cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output, err = p.communicate()
    p_status = p.wait()
    print("Executed command: {}, status: {}".format(cmd, p_status))
    print('Output: ' + str(output))
    if p_status > 0:
        print("ERROR: Not able to execute:" + cmd)
        exit()
    return p_status, output

