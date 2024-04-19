from bottle import get, post, run, request, template

import subprocess

#### 这个是 客户端请求 服务端就发给一个 index.html 控制界面给客户端
@get("/")
def index():
    return template("index")


@post("/cmd")
def cmd():
    adss = request.body.read().decode()  #### 接收到 客户端 发过来的数据
    print("### Do cmd:" + adss)
    ret, val = subprocess.getstatusoutput(adss)  # 0表示指令成功执行，1表示失败，256表示没有返回结果
    print('ret=%d' %ret)
    print('val=' + val)
    i = val.find('OnOff: TRUE')
    if i > -1:
        print('OnOff: TRUE')
        return 'on'
    i = val.find('OnOff: FALSE')
    if i > -1:
        print('OnOff: FALSE')
        return 'off'
    
    i = val.find('OperationalState: 1')
    if i > -1:
        print('OperationalState: 1')
        return 'Running'

    i = val.find('OperationalState: 0')
    if i > -1:
        print('OperationalState: 0')
        return 'Stopped'

    i = val.find('OperationalState: 2')
    if i > -1:
        print('OperationalState: 2')
        return 'Paused'
    
    i = val.find('OperationalState: 3')
    if i > -1:
        print('OperationalState: 3')
        return 'OperationalState Error'
    
    i = val.find('CurrentMode: 0')
    if i > -1:
        print('CurrentMode: 0')
        return 'normal'
    else:
        i = val.find('CurrentMode: 1')
        if i > -1:
            print('CurrentMode: 1')
            return 'heavy'
        else:
            i = val.find('CurrentMode: 2')
            if i > -1:
                print('CurrentMode: 2')
                return 'light'
    
    i = val.find('CHIP:TOO: Device commissioning completed with success')
    if i > -1:
        print('CHIP:TOO: Device commissioning completed with success')
        return 'pair success'

    i = val.find('CHIP:TOO: Device unpair completed with success')
    if i > -1:
        print('CHIP:TOO: Device unpair completed with success')
        return 'unpair success'

    i = val.find('CHIP:BLE: Scan complete. No matching device found.')
    if i > -1:
        print('CHIP:BLE: Scan complete. No matching device found.')
        return 'Scan complete. No matching device found.'

    i = val.find('CHIP:TOO: Device commissioning Failure')
    if i > -1:
        print('CHIP:TOO: Device commissioning Failure')
        return 'Device commissioning Failure'

    i = val.find('CHIP:TOO: InitArgs: Invalid argument')
    if i > -1:
        print('CHIP:TOO: InitArgs: Invalid argument')
        return 'Invalid argument'

    i = val.find('CHIP:TOO: Pairing Failure')
    if i > -1:
        print('CHIP:TOO: Pairing Failure')
        return 'Pairing Failure'

    i = val.find('Device unpair Failure')
    if i > -1:
        print('Device unpair Failure')
        return 'Device unpair Failure'

    i = val.find('ErrorStateID: 0')
    if i > -1:
        print('ErrorStateID: 0')
        return 'ErrorStateID: 0'

    i = val.find('ErrorStateID: 1')
    if i > -1:
        print('ErrorStateID: 1')
        return 'ErrorStateID: 1'

    i = val.find('ErrorStateID: 3')
    if i > -1:
        print('ErrorStateID: 3')
        return 'ErrorStateID: 3'

    i = val.find('CHIP:TOO:     status: 0')
    if i > -1:
        print('change mode success')
        return 'change mode success'

    i = val.find('CHIP:TOO:     status: 1')
    if i > -1:
        print('UnsupportedMode')
        return 'UnsupportedMode'

    i = val.find('CHIP:TOO:     status: 2')
    if i > -1:
        print('change mode fail')
        return 'change mode fail'

    i = val.find('CHIP:TOO:   State: 1')
    if i > -1:
        print('Inflow Error')
        return 'Inflow Error'

    i = val.find('CHIP:TOO:   State: 4')
    if i > -1:
        print('Door Open Error')
        return 'Door Open Error'

    i = val.find('CHIP:TOO:   State: 8')
    if i > -1:
        print('TempTooLow')
        return 'TempTooLow'



    if 0 == ret:
        return "OK"
    if 1 == ret:
        return "NG"
    if 256 == ret:
        return "NONE"



run(host='0.0.0.0', port=8088, debug=True)  #### 开启服务端
