import re

class Data_Progress:
    def __init__(self, src_path):
        self.cpu1_freq_list = []
        self.cpu2_freq_list = []
        self.ddr_freq_list = []
        self.ufs_freq_list = []
        self.cpu_info = dict()
        self.ufs_info = dict()
        self.ddr_gear = dict()
        self.src_path = src_path

        self.cpu_freq_info = r'.*CPU[0-9]--cur_freq.*'
        self.cpu_max_info = r'.*CPU[0-9]--max_freq.*'
        self.DDR_actual_info = r'.*Current DDR actual frequency.*'
        self.ufs_cur_info = r'.*UFS cur_freq.*'

        self.ufs_title = "UFS Available freq"
        self.ddr_gear_title = "DDR gear"
        # self.ufs_freq_title = "UFS max_freq"

    def is_CPU_info(self, info):
        return re.match(self.cpu_max_info, info)

    def put_cpu1_freq(self, freq):
        self.cpu1_freq_list.append(freq)

    def put_cpu2_freq(self, freq):
        self.cpu2_freq_list.append(freq)

    def put_ddr_freq(self, freq):
        self.ddr_freq_list.append(freq)

    def put_ufs_freq(self, freq):
        self.ufs_freq_list.append(freq)

    def is_UFS_info(self, info):
        return self.ufs_title in info

    def is_DDR_info(self, info):
        return self.ddr_gear_title in info

    # def is_UFS_max_min_freq(self, info):
    #     return self.ufs_freq_title in info

    def progress(self):
        with open(self.src_path, 'r') as f:
            def readline():
                return f.readline().strip("\n")
            while True:
                info = readline()
                if not info:
                    # print("no info")
                    break
                elif info.startswith('\"'):
                    # 正则匹配判断是否位 cpu_cur_freq 信息，并将对应信息存入列表
                    if re.match(self.cpu_freq_info, info):
                        # print("get cpu freq info")
                        self.put_cpu1_freq(int(readline()))
                        self.put_cpu2_freq(readline())
                    # 获取ddr actual freq 信息
                    elif re.match(self.DDR_actual_info, info):
                        # 获取 ddr 信息
                        # print("get DDR actual freq info")
                        Vcore_info = readline()
                        DDR_info = readline().split(":") # DDR       : 2066000  khz
                        FORCE_OPP_IDX_info = readline()
                        CONTROL_info = readline()
                        ddr_freq = DDR_info[1].split("  ")[0].strip(" ")# 2066000
                        self.put_ddr_freq(ddr_freq)
                    # 获取ufs cur freq 信息
                    elif re.match(self.ufs_cur_info, info):
                        # print("get ufs freq info")
                        ufs_cur_freq = readline()
                        self.put_ufs_freq(ufs_cur_freq)
                    # 获取cpu大小核的 max freq 信息
                    elif self.is_CPU_info(info):
                        words = info.strip("\"").split(",")
                        cpu1_freq = readline()
                        self.cpu_info[words[0].strip(" ")] = cpu1_freq
                        cpu2_freq = readline()
                        self.cpu_info[words[-1].strip(" ")] = cpu2_freq
                    # 获取 ufs 频率相关信息
                    elif self.is_UFS_info(info):
                        ufs_available_freq_list = readline().strip("\"").split(",")
                        self.ufs_info["UFS Available freq"] = ufs_available_freq_list
                        ufs_max_min_freq = readline().strip("\"").split(",")
                        self.ufs_info[ufs_max_min_freq[0].strip(" ")] = readline()
                        self.ufs_info[ufs_max_min_freq[1].strip(" ")] = readline()
                    # 获取 ddr gear 相关信息
                    elif self.is_DDR_info(info):
                        NUM_VCORE_OPP = readline().split(":")
                        NUM_DDR_OPP = readline().split(":")
                        NUM_DVFSRC_OPP = readline().split(":")
                        self.ddr_gear[NUM_VCORE_OPP[0].strip(" ")] = NUM_DDR_OPP[1].strip(" ")
                        self.ddr_gear[NUM_DDR_OPP[0].strip(" ")] = NUM_VCORE_OPP[1].strip(" ")
                        self.ddr_gear[NUM_DVFSRC_OPP[0].strip(" ")] = NUM_DVFSRC_OPP[1].strip(" ")
                    else:
                        print("something is wrong...")
                        # print("skip")

        # 字符串数组转数字数组
        self.cpu1_freq_list[:] = [x for x in self.cpu1_freq_list if x]
        self.cpu1_freq_list = list(map(int, self.cpu1_freq_list))

        self.cpu2_freq_list[:] = [x for x in self.cpu2_freq_list if x]
        self.cpu2_freq_list = list(map(int, self.cpu2_freq_list))

        self.ddr_freq_list[:] = [x for x in self.ddr_freq_list if x]
        self.ddr_freq_list = list(map(int, self.ddr_freq_list))

        self.ufs_freq_list[:] = [x for x in self.ufs_freq_list if x]
        self.ufs_freq_list = list(map(int, self.ufs_freq_list))


if __name__ == '__main__':
    dp = Data_Progress(src_path='data/freq_V.log')
    dp.progress()
    print(dp.cpu_info)
    print(dp.ufs_info)
    print(dp.ddr_gear)
    print(dp.cpu1_freq_list)
    print(dp.cpu2_freq_list)
    print(dp.ddr_freq_list)
    print(dp.ufs_freq_list)