
import serial # pyserial


import time


def main():
    portx = "COM3"
    bps = 4800
    timex = 5

    # 打开串口，并得到串口对象
    ser = serial.Serial(portx, bps, timeout=timex)

    # 写数据
    with open(".\\51codes.txt","r") as f:
        string=f.read()
        codes=string.split(",")
    string=""
    for i in range(len(codes)):
        if(len(codes[i])==1):
            codes[i]='0'+codes[i]
        string=string+" "+codes[i]
        if(i%8==7):
            ser.write(bytes.fromhex(string))#codes[i].encode('utf-8')
            print("当前帧数：", int(i/8),string)
            string=""
        time.sleep(0.01)

    ser.close() # 关闭串口

main()
