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
    import serial
    ser = serial.Serial(port, speed)

    while True:
        byteRead = ser.read()
        byteReadHex = hex(ord(byteRead))

        # Copiar lista a un fichero.
        file = open("log2.txt", "a")
        file.write(byteReadHex)
        file.write("\n")
        file.close()


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
    speed = 115200

    import sys
    try:
        if sys.argv[1] == '-s':
            mainSerialSocket(port, speed)
        elif sys.argv[1] == '-k':
            mainKISSSocket(port, speed)
    except:
        pass
