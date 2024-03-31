from PySide6.QtSerialBus import QCanBus, QCanBusDevice, QCanBusDeviceInfo, QCanBusFactory, QCanBusFrame
from PySide6.QtCore import QTimer


def send_frame(device, frame):
    if device:
        device.writeFrame(frame)
        
def process_received_frames(device):
    while device.framesAvailable():
        frame = device.readFrame()
        data = ""
        if frame.frameType() == QCanBusFrame.ErrorFrame:
            data = device.interpretErrorFrame(frame)
        else:
            data = frame.payload().toHex(' ').toUpper()

        secs = frame.timeStamp().seconds()
        microsecs = frame.timeStamp().microSeconds() / 100
        time = f"{secs:>10}.{microsecs:0>4}"

        id = f"{frame.frameId():x}"
        dlc = f"{frame.payload().size()}"
        print("{}, {}, {}, {}".format(time, id, dlc, data))
        

alpha, error_string = QCanBus.instance().createDevice("socketcan", "vcan0")

alpha.framesReceived.connect(lambda: process_received_frames(alpha))
alpha.configurationParameter(QCanBusDevice.BitRateKey)
alpha.configurationParameter(QCanBusDevice.DataBitRateKey)

print(alpha)