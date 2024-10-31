import time

from matplotlib import pyplot as plt
from data_progress import Data_Progress

class Picture_Generate(Data_Progress):

    def __init__(self, src_path):
        super().__init__(src_path)
        self.dp = Data_Progress(src_path)
        self.dp.progress()
        # cpu 大小核  频率数据
        self.c_min = self.dp.cpu1_freq_list
        self.c_max = self.dp.cpu2_freq_list
        # ddr 频率
        self.ddr = self.dp.ddr_freq_list
        # ufs 频率
        self.ufs = self.dp.ufs_freq_list
        self.x1 = [i for i in range(len(self.c_min))]
        self.x2 = [i for i in range(len(self.ddr))]
        self.x3 = [i for i in range(len(self.ufs))]

        self.font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 8}

    def get_time(self):
        timeStamp = time.time()
        timeArray = time.localtime(timeStamp)
        time_str = time.strftime("_%m_%d_%H_%M", timeArray)
        return time_str

    def cpu_display(self, dir):
        # 设置画板：figsize 画板大小
        fig = plt.figure(figsize=(10, 3))
        # 绘图 color:设置颜色, linewidth：设置折线粗细
        plt.plot(self.c_min, color='#ff9408', linewidth=1.0, label='cpu 0', marker='o', markersize=1.5)
        plt.plot(self.c_max, color='#b96902', linewidth=1.0, label='cpu 1', marker='o', markersize=1.5)

        plt.legend(loc='upper right')
        plt.tick_params('x', labelbottom=False)  # 设置图形，不显示X轴内容
        # y_major_locator = MultipleLocator(1e6)  # 把x轴的刻度间隔设置为1，并存在变量里
        # ax = plt.gca()  # ax为两条坐标轴的实例
        # ax.yaxis.set_major_locator(y_major_locator)  # 把x轴的主刻度设置为1的倍数

        # 设置标签样本点值标签（改为 Ghz单位）
        # for a, b in enumerate(self.c_min):
        #     plt.text(a, b + 0.5, "{:.1e}".format(b), ha='center', va='bottom', fontproperties=self.font)

        # 颜色填充
        plt.fill_between(self.x1, self.c_min, y2=0, color='#ff9408', alpha=0.15)
        plt.fill_between(self.x1, self.c_max, self.c_min, color='#b96902', alpha=0.15)
        # 保存
        plt.savefig(dir + "/cpu" + self.get_time() + ".png")

        plt.tight_layout()
        # 展示
        plt.show()

    def ddr_display(self, dir):
        # 设置画板：figsize 画板大小
        fig = plt.figure(figsize=(10, 3))
        # 绘图 color:设置颜色, linewidth：设置折线粗细
        plt.plot(self.ddr, color='#75fd63', linewidth=1.0)
        plt.fill_between(self.x2, self.ddr, y2=0, color='#75fd63', alpha=0.15)
        # 绘制图例
        # plt.legend(loc='upper right')
        # 保存
        plt.savefig(dir + "/ddr" + self.get_time() + ".png")
        plt.tick_params('x', labelbottom=False)  # 设置图形，不显示X轴内容
        plt.title("ddr freq")
        # 展示
        plt.show()

    def ufs_display(self, dir):
        # 设置画板：figsize 画板大小
        fig = plt.figure(figsize=(10, 3))
        # 绘图 color:设置颜色, linewidth：设置折线粗细
        plt.plot(self.ufs, color='#02ccfe', linewidth=1.0, marker='o', markersize=1.5)
        plt.fill_between(self.x3, self.ufs, y2=0, color='#02ccfe', alpha=0.15)
        # 绘制图例
        # plt.legend(loc='upper right')
        plt.tick_params('x', labelbottom=False)  # 设置图形，不显示X轴内容
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.title("ufs freq")
        # 保存
        plt.savefig(dir + "/ufs" + self.get_time() + ".png")
        # 展示
        plt.show()

    def display_all(self, dir):
        ax1 = plt.subplot(311)
        plt.plot(self.c_min, color='#ff9408', linewidth=1.0, label='cpu 0')
        plt.plot(self.c_max, color='#b96902', linewidth=1.0, label='cpu 1')

        plt.fill_between(self.x1, self.c_min, y2=0, color='#ff9408', alpha=0.15)
        plt.fill_between(self.x1, self.c_max, self.c_min, color='#b96902', alpha=0.15)
        plt.tick_params('x', labelbottom=False)  # 设置图形，不显示X轴内容
        plt.legend(loc='upper right')
        plt.title('cpu_freq', fontsize=5)
        plt.ylabel('freq/hz')

        ax2 = plt.subplot(312, sharex=ax1)
        plt.plot(self.ddr, color='#75fd63', linewidth=1.0)
        plt.fill_between(self.x2, self.ddr, y2=0, color='#75fd63', alpha=0.15)
        plt.tick_params('x', labelbottom=False)  # 设置图形，不显示X轴内容
        plt.title('ddr_freq', fontsize=5)
        plt.ylabel('freq/hz')

        ax3 = plt.subplot(313, sharex=ax1) # 共享第一个图形的x轴
        plt.plot(self.ufs, color='#02ccfe', linewidth=1.0)
        plt.fill_between(self.x3, self.ufs, y2=0, color='#02ccfe', alpha=0.15)
        plt.tick_params('x', labelbottom=False)  # 设置图形，不显示X轴内容
        plt.title('ufs_freq', fontsize=5)
        plt.ylabel('freq/hz')

        plt.savefig(dir + "/all" + self.get_time() + ".png")
        plt.show()


if __name__ == '__main__':
    pic = Picture_Generate(src_path='data/freq_V.log')
    # pic.cpu_display()
    # pic.ddr_display()
    # pic.ufs_display()
    # pic.display_all()
    print(pic.get_time())