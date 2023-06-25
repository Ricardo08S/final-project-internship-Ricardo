#!/usr/bin/env python

import rospy
from hw_comunication.msg import Motor
from motor_controler.srv import *
from socket import *

############################
Ip = "192.168.0.80"
Port = 2004
Pw = "ITS"
############################


def send_motor_data(input):
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    receiver_ip = Ip
    receiver_port = Port

    rospy.init_node("udp_sender", anonymous=True)

    motor_pub = rospy.Publisher("motor_data", Motor, queue_size=10)

    rate = rospy.Rate(10)  # 10 Hz

    motor_msg = Motor()
    motor_msg.Pass = Pw
    motor_msg.data = input
    msg_final = motor_msg.Pass + motor_msg.data

    motor_pub.publish(motor_msg)

    motor_data = "{}".format(msg_final)

    udp_socket.sendto(motor_data.encode(), (receiver_ip, receiver_port))

    rate.sleep()


def receive_motor_data():
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    publisher_ip = Ip
    publisher_port = Port

    udp_socket.bind((publisher_ip, publisher_port))

    # rospy.init_node('udp_receiver', anonymous=True)

    # motor_pub = rospy.Publisher('received_motor_data', Motor, queue_size=10)

    motor_data, addr = udp_socket.recvfrom(1024)

    received_motor_pass = motor_data.decode()[:3]
    received_motor_data = motor_data.decode()[3:]

    if received_motor_pass == Pw:
        print("Receive: {}".format(received_motor_data))

        # received_motor_msg = Motor()
        # received_motor_msg.Pass = received_motor_pass
        # received_motor_msg.data = int(received_motor_data)
        # motor_pub.publish(received_motor_msg)


def kapal_belok_kanan():
    return 1700150  # motor: 1700, servo: 150 derajat


def kapal_belok_kiri():
    return 170030  # motor: 1700, servo: 30 derajat


def kapal_maju():
    return 180088  # motor: 1800, servo 0 derajat


def kapal_berhenti():
    return 150090  # motor: 1500, servo: 90 derajat


def kapal_mundur():
    return 110090  # motor: 1100, servo: 90 derajat


def water_pump():
    return 2222  # perintah untuk menjalankan logika waterpump


def jalankan():
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        input = 1
        if input == 1:
            send_motor_data(kapal_belok_kanan())
        if input == 2:
            send_motor_data(kapal_belok_kiri())
        if input == 3:
            send_motor_data(kapal_maju())
        if input == 4:
            send_motor_data(kapal_berhenti())
        if input == 5:
            send_motor_data(kapal_mundur())
        if input == 6:
            send_motor_data(water_pump())
        receive_motor_data()

        rate.sleep()


if __name__ == "__main__":
    # dapat inputan untuk perintah gerakan untuk mengarah ke tujuan kapal secara terus menerus
    # bisa dengan mengetahui dari bounding box atau mengatur kecepatan juga dengan mendapatkan
    # rospy.ServiceProxy() dari set_pid.py memeanfaatkan PID.srv lalu dikirimkan ke microcontroller
    # dengan menggunakan pesan tertentu yang sudah disetujui
    jalankan()
