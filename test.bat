echo off
adb root
echo " CPU0--max_freq, CPU6--max_freq ">> %1
adb shell cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq >> %1
adb shell cat /sys/devices/system/cpu/cpu6/cpufreq/scaling_max_freq >> %1
echo " DDR gear ">> %1
adb shell cat /sys/devices/platform/soc/1c00f000.dvfsrc/helio-dvfsrc/dvfsrc_opp_table>> %1
echo " UFS Available freq ">> %1
adb shell cat /sys/devices/platform/soc/1c00f000.dvfsrc/mtk-dvfsrc-devfreq/devfreq/mtk-dvfsrc-devfreq/available_frequencies>> %1
echo " UFS max_freq,  UFS min_freq">> %1
adb shell cat /sys/devices/platform/soc/1c00f000.dvfsrc/mtk-dvfsrc-devfreq/devfreq/mtk-dvfsrc-devfreq/max_freq>> %1
adb shell cat /sys/devices/platform/soc/1c00f000.dvfsrc/mtk-dvfsrc-devfreq/devfreq/mtk-dvfsrc-devfreq/min_freq>> %1

:start
echo " CPU0--cur_freq, CPU6--cur_freq ">> %1
adb shell cat %2 >> %1
adb shell cat %3 >> %1
echo " Current DDR actual frequency ">> %1
adb shell "cat %4 | grep -e uv -e khz -e FORCE -e CONTROL">> %1
echo " UFS cur_freq  ">> %1
adb shell cat %5 >> %1
timeout /t 1

goto start

pause


