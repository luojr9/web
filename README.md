# web
Matter Dishwasher controller web on Raspberry Pi

## 快速开始Quick Start

1. 树莓派启动chip-lighting-app，并用chip-tool配对自己，测试开关机功能正常。
2. clone这个仓库到树莓派
3. `cd web`
4. 首次运行要先安装bottle，执行`pip3 install bottle`
5. `python3 index.py`
6. 打开网页，树莓派IP:8088，例如192.168.1.104:8088
7. 点击按钮Power ON、Power OFF，查看灯状态是否有变化。

## 测试洗碗机Test Dishwasher

1. 修改index.html，点击按钮发送指令

   ```
   httpRequest.send('~/apps/chip-tool onoff on 1 1');
   ```

