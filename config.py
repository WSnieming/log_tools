config = {
    'path':{
        'log_path':'data/freq_MTK',
    },
    'commands':{
        'cpu0_freq':'/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq',
        'cpu1_freq':'/sys/devices/system/cpu/cpu6/cpufreq/scaling_cur_freq',
        'ddr_freq':'/sys/devices/platform/soc/1c00f000.dvfsrc/helio-dvfsrc/dvfsrc_dump',
        'ufs_freq':'/sys/devices/platform/soc/1c00f000.dvfsrc/mtk-dvfsrc-devfreq/devfreq/mtk-dvfsrc-devfreq/cur_freq'
    }
}