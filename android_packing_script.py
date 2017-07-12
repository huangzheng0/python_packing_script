# This Python file uses the following encoding: utf-8
# labifenqi-{channel}-release-v4.2.0-170620.apk
# labifenqi-{channel}.apk
import zipfile
import sys
import os.path
import time
from shutil import copyfile
from os.path import basename

current_milli_time = lambda: int(round(time.time() * 1000))

channels = ['website', 'baidu', '_360', 'mumayi', 'sogou', '_3gqq', 'aliapp', 'coolchuan', '_3gandroid',
            'goapk',
            'appchina', 'huawei', 'xiaomi', 'oppo', 'meizu', 'le', 'smartisan', 'aoratec', 'lenovo', 'vivo']


def generate_lb_web_channel():
    list_channel = []
    create_lb_web_channel(list_channel, 'X', 0, 40)
    create_lb_web_channel(list_channel, 'Y', 0, 20)
    create_lb_web_channel(list_channel, 'Z', 0, 40)
    return list_channel


def create_lb_web_channel(list, mark_letter, start, end):
    base_name = 'LB{mark_letter}00{mark_index}'
    for index in range(start, end):
        mark_index = str(index)
        if (index < 10): mark_index = "0" + str(index)
        list.append(
            base_name.format(mark_letter=mark_letter, mark_index=mark_index))


def add_channel_file_to_apk(apk, channel, empty_file):
    zipped = zipfile.ZipFile(apk, 'a', zipfile.ZIP_DEFLATED)
    empty_channel_file = "META-INF/channel_{channel}".format(channel=channel)
    zipped.write(empty_file.name, empty_channel_file)
    zipped.close()


def copy_and_rename_file(origin, new):
    copyfile(origin, new)
    print ('create new file success' + new)


def generate_apk_file_name_by_channel(file_name, channel):
    if (channel.startswith("LB")):
        return "labifenqi-" + channel + ".apk"
    return file_name.format(channel=channel)


def create_new_empty_channel_file(out_put_directory):
    print("create empty file")
    try:
        name = out_put_directory + 'channel_temp_empty_file'
        file = open(name, 'a')
        file.close()
        return file
    except:
        print("error occured")
        sys.exit(0)


def create_channel_apk(channel):
    print ("===== start process channel :" + channel + "=====")
    new_apk_name = generate_apk_file_name_by_channel(file_name, channel)
    new_file_path = out_put_directory + new_apk_name
    print ('create file :' + new_apk_name)
    copy_and_rename_file(origin_apk, new_file_path)
    print ('complete...')
    print ('add channel file to apk...')
    add_channel_file_to_apk(new_file_path, channel, empty_file)
    print ('complete...')
    print ("===== end process channel :" + channel + "=====")


# create new empty file

origin_apk = "/home/jackwang/Desktop/4.2.1/labifenqi-website-beta-v4.2.1-3-gd5118cb-dirty-170626.apk"
print ("***** name replace rule *****")
print ("***** '{channel}' part will replace to real channel name *****")
origin_apk = raw_input("input the apk path : \n")

startMils = current_milli_time();

file_name = basename(origin_apk)

out_put_directory = origin_apk.replace(file_name, 'channel_apk_out_put/')

print ("out_put_directory = " + out_put_directory)

if not os.path.exists(out_put_directory):
    os.makedirs(out_put_directory)
    print ('create out_put_directory')

empty_file = create_new_empty_channel_file(out_put_directory)

for channel in channels:
    create_channel_apk(channel)

web_channel = generate_lb_web_channel()
for channel in web_channel:
    create_channel_apk(channel)

print ("Total time: " + str(current_milli_time() - startMils) + " ms")
