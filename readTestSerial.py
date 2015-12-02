# coding=utf-8
"""
   Copyright 2015 Samuel Góngora García

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

:Author:
    Samuel Góngora García (s.gongoragarcia@gmail.com)
"""
__author__ = 's.gongoragarcia@gmail.com'


def mainSerialSocket(port, speed):

    print "inside"

    import serial
    ser = serial.Serial(port, speed)
    ser.timeout = None

    print ser

    lista = []
    i = 0
    fichero = open("log6.txt", "a")

    try:
        while i < 35:  # was 400
            i = i + 1
            byteRead = ser.read(10)
            # byteReadHex = hex(ord(byteRead))
            byteReadHex = byteRead
            lista.append(byteReadHex)
    except Exception as e:
        print e

    try:
        for item in lista:
            fichero.write("%s\n" % item)
        fichero.close()
    except Exception as e:
        print e
        print "error en el volcado"


def mainKISSSocket(port, speed):
    import kiss
    k = kiss.KISS(port, speed)
    k.start()
    k.read(callback=print_frame)


def print_frame(frame):
    try:
        import aprs
        # Decode raw APRS frame into dictionary of separate sections
        decoded_frame = aprs.util.decode_frame(frame)
        # Format the APRS frame (in Raw ASCII Text) as a human readable frame
        formatted_aprs = aprs.util.format_aprs_frame(decoded_frame)
        # This is the human readable APRS output:
        print formatted_aprs

    except Exception as ex:
        print ex
        print "Error decoding frame:"
        print "\t%s" % frame


if __name__ == "__main__":
    port = '/dev/ttyUSB0'
    speed = 500000

    import sys
    try:
        if sys.argv[1] == '-s':
            mainSerialSocket(port, speed)
        elif sys.argv[1] == '-k':
            mainKISSSocket(port, speed)
    except:
        print "Error"
