import os.path
import subprocess
import argparse
import time
from config import config as cf
from picture_generate import Picture_Generate


def get_time():
    timeStamp = time.time()
    timeArray = time.localtime(timeStamp)
    time_str = time.strftime("%Y %m %d %H:%M:%S", timeArray)
    return time_str

def get_time2():
    timeStamp = time.time()
    timeArray = time.localtime(timeStamp)
    time_str = time.strftime("_%m_%d_%H_%M", timeArray)
    return time_str

root_dir = os.path.dirname(__file__)
info = ''
info += get_time()+": 程序开始执行...\n"


lp = cf['path']['log_path']
command_cpu0_freq = cf['commands']['cpu0_freq']
command_cpu1_freq = cf['commands']['cpu1_freq']
command_ddr_freq = cf['commands']['ddr_freq']
command_ufs_freq = cf['commands']['ufs_freq']

parser = argparse.ArgumentParser()
parser.add_argument('--p', type=str, default=lp)
parser.add_argument('--c0', type=str, default=command_cpu0_freq)
parser.add_argument('--c1', type=str, default=command_cpu1_freq)
parser.add_argument('--d', type=str, default=command_ddr_freq)
parser.add_argument('--u', type=str, default=command_ufs_freq)
args = parser.parse_args()

bat_path = os.path.join(root_dir, 'test.bat')
lp = os.path.join(root_dir, args.p)+get_time2()+".log"


try:
    subprocess.call([bat_path, lp, args.c0, args.c1, args.d, args.u], shell=True)
except KeyboardInterrupt as e:
    info += get_time() + ": 命令执行结束（手动打断）\n"
except Exception as e1:
    info += get_time()+": 命令执行结束，异常信息："+str(e1)+"\n"
finally:
    print("准备画图...")
    try:
        pic = Picture_Generate("D:/Documents/Desktop/cpu_freq_get/data/freq_V.log")
        pic.display_all(root_dir+"/pictures/")
        print("图片生成完毕。保存位置：" + "")
    except Exception as e2:
        info += get_time2() + ": 画图失败，异常信息：" + str(e2) + "\n"
    finally:
        log_path = os.path.join(root_dir, 'Running.log')
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(info)


if __name__ == '__main__':
    pass