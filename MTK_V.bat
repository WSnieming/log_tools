echo off
adb root
echo " CPU0--max_freq, CPU6--max_freq ">> freq_V.log
adb shell cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq>> freq_V.log
adb shell cat /sys/devices/system/cpu/cpu6/cpufreq/scaling_max_freq>> freq_V.log
echo " DDR gear ">> freq_V.log
adb shell cat /sys/devices/platform/soc/1c00f000.dvfsrc/helio-dvfsrc/dvfsrc_opp_table>> freq_V.log
echo " UFS Available freq ">> freq_V.log
adb shell cat /sys/devices/platform/soc/1c00f000.dvfsrc/mtk-dvfsrc-devfreq/devfreq/mtk-dvfsrc-devfreq/available_frequencies>> freq_V.log
echo " UFS max_freq,  UFS min_freq">> freq_V.log
adb shell cat /sys/devices/platform/soc/1c00f000.dvfsrc/mtk-dvfsrc-devfreq/devfreq/mtk-dvfsrc-devfreq/max_freq>> freq_V.log
adb shell cat /sys/devices/platform/soc/1c00f000.dvfsrc/mtk-dvfsrc-devfreq/devfreq/mtk-dvfsrc-devfreq/min_freq>> freq_V.log

:start
echo " CPU0--cur_freq, CPU6--cur_freq ">> freq_V.log
adb shell cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq>> freq_V.log
adb shell cat /sys/devices/system/cpu/cpu6/cpufreq/scaling_cur_freq>> freq_V.log
echo " Current DDR actual frequency ">> freq_V.log
adb shell "cat /sys/devices/platform/soc/1c00f000.dvfsrc/helio-dvfsrc/dvfsrc_dump | grep -e uv -e khz -e FORCE -e CONTROL">> freq_V.log
echo " UFS cur_freq  ">> freq_V.log
adb shell cat /sys/devices/platform/soc/1c00f000.dvfsrc/mtk-dvfsrc-devfreq/devfreq/mtk-dvfsrc-devfreq/cur_freq>> freq_V.log
timeout /t 1

goto start

pause