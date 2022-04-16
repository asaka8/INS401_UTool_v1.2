import time
import psutil
import numpy as np
import pyqtgraph as pg

from .data_captor import DataCaptor

class IMUDataVisual:
    def __init__(self) -> None:
        self.data_recv = DataCaptor()
        self.ptr = 0

    def get_imu_accel_x(self):
        accel_x = self.data_recv.get_imu()[2][0]
        # print(accel_x)
        accel_x_lst.append(float(accel_x))
        accel_x_lst[:-1] = accel_x_lst[1:]
        accel_x_lst[:-1].append(float(accel_x))

        curve_accel_x.setData(accel_x_lst, pen='r')
    
    def get_imu_accel_y(self):
        accel_y = self.data_recv.get_imu()[2][1]
        # print(accel_y)
        accel_y_lst.append(float(accel_y))
        accel_y_lst[:-1] = accel_y_lst[1:]
        accel_y_lst[:-1].append(float(accel_y))

        curve_accel_y.setData(accel_y_lst, pen='y')

    def get_imu_accel_z(self):
        accel_z = self.data_recv.get_imu()[2][2]
        # print(accel_z)
        accel_z_lst.append(float(accel_z))
        accel_z_lst[:-1] = accel_z_lst[1:]
        accel_z_lst[:-1].append(float(accel_z))

        curve_accel_z.setData(accel_z_lst, pen='b')

    def get_imu_gyro_x(self):
        gyro_x = self.data_recv.get_imu()[3][0]
        # print(gyro_x)
        gyro_x_lst.append(float(gyro_x))
        gyro_x_lst[:-1] = gyro_x_lst[1:]
        gyro_x_lst[:-1].append(float(gyro_x))

    def get_imu_gyro_y(self):
        gyro_y = self.data_recv.get_imu()[3][1]
        # print(gyro_y)
        gyro_y_lst.append(float(gyro_y))
        gyro_y_lst[:-1] = gyro_y_lst[1:]
        gyro_y_lst[:-1].append(float(gyro_y))

    def get_imu_gyro_z(self):
        gyro_z = self.data_recv.get_imu()[3][2]
        # print(gyro_z)
        gyro_z_lst[:-1] = gyro_z_lst[1:]
        gyro_z_lst[:-1].append(float(gyro_z))

    def curve_runer(self):
        global curve_accel_x, curve_accel_y, curve_accel_z
        global curve_gyro_x, curve_gyro_y, curve_gyro_z
        global accel_x_lst, accel_y_lst, accel_z_lst
        global gyro_x_lst, gyro_y_lst, gyro_z_lst

        accel_x_lst = []
        accel_y_lst = []
        accel_z_lst = []
        gyro_x_lst = []
        gyro_y_lst = []
        gyro_z_lst = []

        self.data_recv.connect()
        app = pg.mkQApp()
        win = pg.GraphicsWindow()
        win.setWindowTitle(u'pyqtgraph updating wave')
        win.resize(1000, 800)
        # pg.setConfigOptions(antialias=True)

        # plotting for X-axis acceleration
        historyLength = 500
        p1 = win.addPlot()
        p1.showGrid(x=True, y=True)
        p1.setRange(xRange=[0, historyLength], yRange=[-15, 15], padding=0)
        p1.setLabel(axis='left', text='Acceleration')
        p1.setLabel(axis='bottom', text='Time')
        p1.setTitle('IMU X-axis Acceleration')
        curve_accel_x = p1.plot()

        timer = pg.QtCore.QTimer()
        timer.timeout.connect(self.get_imu_accel_x)
        timer.start()

        # plotting for Y-axis acceleration
        historyLength = 500
        p2 = win.addPlot()
        p2.showGrid(x=True, y=True)
        p2.setRange(xRange=[0, historyLength], yRange=[-15, 15], padding=0)
        p2.setLabel(axis='left', text='Acceleration')
        p2.setLabel(axis='bottom', text='Time')
        p2.setTitle('IMU Y-axis Acceleration')
        curve_accel_y = p2.plot()

        timer.timeout.connect(self.get_imu_accel_y)
        timer.start()

        # plotting for Z-axis acceleration
        historyLength = 500
        p3 = win.addPlot()
        p3.showGrid(x=True, y=True)
        p3.setRange(xRange=[0, historyLength], yRange=[-15, 15], padding=0)
        p3.setLabel(axis='left', text='Acceleration')
        p3.setLabel(axis='bottom', text='Time')
        p3.setTitle('IMU Z-axis Acceleration')
        curve_accel_z = p3.plot()

        timer.timeout.connect(self.get_imu_accel_z)
        timer.start()

        # switch the plotting row
        win.nextRow()

        # plotting for X-axis gyro
        p4 = win.addPlot()
        p4.showGrid(x=True, y=True)
        p4.setRange(xRange=[0, historyLength], yRange=[-15, 15], padding=0)
        p4.setLabel(axis='left', text='Gyro')
        p4.setLabel(axis='bottom', text='Time')
        p4.setTitle('IMU X-axis Gyro')
        curve_gyro_x = p4.plot()
        
        timer.timeout.connect(self.get_imu_gyro_x)
        timer.start()

        # plotting for Y-axis gyro
        p5 = win.addPlot()
        p5.showGrid(x=True, y=True)
        p5.setRange(xRange=[0, historyLength], yRange=[-15, 15], padding=0)
        p5.setLabel(axis='left', text='Gyro')
        p5.setLabel(axis='bottom', text='Time')
        p5.setTitle('IMU Y-axis Gyro')
        curve_gyro_y = p5.plot()

        timer.timeout.connect(self.get_imu_gyro_y)
        timer.start()

        # plotting for Z-axis gyro
        p6 = win.addPlot()
        p6.showGrid(x=True, y=True)
        p6.setRange(xRange=[0, historyLength], yRange=[-15, 15], padding=0)
        p6.setLabel(axis='left', text='Gyro')
        p6.setLabel(axis='bottom', text='Time')
        p6.setTitle('IMU Z-axis Gyro')
        curve_gyro_z = p6.plot()

        timer.timeout.connect(self.get_imu_gyro_z)
        timer.start()

        app.exec_()