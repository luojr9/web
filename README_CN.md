# web
Matter Dishwasher controller web on Raspberry Pi

## 准备工作

1. 树莓派：把chip-tool-1.2文件放到目录~/apps。增加执行权限，`chmod +x ~/apps/chip-tool-1.2`
2. 树莓派：首次运行要先安装bottle，执行`pip3 install bottle`
3. 树莓派：`cd ~`
4. 树莓派：clone这个Git仓库
5. 树莓派：`cd ~/web`
6. 树莓派：`python3 main.py`
7. 树莓派：把PAA证书Chip-Midea-PAA-118C-Cert.der放在目录/var/paa-root-certs/
8. 查看树莓派IP
9. 电脑：打开网页浏览器，网址输入树莓派IP，可以显示网页Matter Test Harness (v2.8-official)。确认电脑和树莓派的网络已连通。
10. 电脑：网址输入 树莓派IP:8088，例如192.168.1.104:8088，打开网页Midea Dishwasher Matter Demo
11. WiFi模组：烧录支持Matter洗碗机的固件。



## 树莓派控制洗碗机

控制端：树莓派

服务端：洗碗机

测试步骤：

1. 洗碗机：上电，开机。
2. 洗碗机：长按WiFi键3秒，等待配对。
3. 电脑：打开Demo网页，Node ID默认是1，填入无线路由器的SSID和密码，点【Pair】，等待十多秒，配对成功则显示Response: pair success。
4. 电脑：点击【Power OFF】关机，【Power ON】开机，
5. 电脑：点击【Start】启动，【Pause】暂停，【Cancel】停止
6. 电脑：点击【Normal】、【Heavy】、【Light】选择洗涤模式
7. 电脑：点击【Get Status】获取洗碗机状态。



## 树莓派模拟洗碗机

控制端：树莓派

服务端：树莓派模拟洗碗机APP

1. 树莓派：`cd ~/apps`
2. 树莓派：`./chip-dishwasher-app`
3. 树莓派：配对，`./chip-tool-1.2 pairing onnetwork-long 2 20202021 3840`
4. 电脑：网页修改Node ID为2。
5. 电脑：点击【Power ON】开机，【Power OFF】关机。
