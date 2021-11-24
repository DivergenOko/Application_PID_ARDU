from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice

app = QtWidgets.QApplication([])
ui: object = uic.loadUi('design.ui')
ui.setWindowTitle("PID")

serial = QSerialPort()
serial.setBaudRate(115200)
portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
    portList.append(port.portName())
ui.comlist.addItems(portList)

def onOpen():
    serial.setPOrtName(ui.comlist.currentText())
    serial.open(QIODevice.ReadWrite)

def onRead():
    rx = serial.readLine()
    rxs = str(rx, 'utf-8').strip()
    data = rxs.split(',')
    print(data)

def onClose():
    serial.close()

def ledControl(val):
    if val== 2: val == 1;
    serialSend([0,val])

def fanControl(val):
    if val == 2: val == 1;
    serialSend([3, val])

def blabControl(val):
    if val == 2: val == 1;
    serialSend([4, val])

def serialSend(data):
    txs = ""
    for val in data:
        txs += str(val)
        txs += ','
    txs = txs[:-1]
    txs +=';'

serial.readyRead.connect(onRead)
ui.OpenB.clicked.connect(onOpen)
ui.CloseB.clicked.connect(onClose)

ui.LEDC.stateChanged.connect(ledControl)
ui.BLABC.stateChanged.connect(ledControl)
ui.FANC.stateChanged.connect(ledControl)

vals = [10, 11, 12]
serialSend(vals)



ui.show()
app.exec()
