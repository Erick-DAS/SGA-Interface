import serial


def main():
    ser = serial.Serial(
        port="/dev/ttyUSB1",  # pode tentar alguma COM tambem, tem que ver na hora
        baudrate=115200,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.SEVENBITS,
    )

    header = b"A"
    end_byte = b"\n"
    size = 4
    msg = []

    print(f"Using serial port {ser.name}")

    current_byte = ser.read()

    while True:
        if current_byte != header:
            current_byte = ser.read()
            continue

        print("Possible header detected. Starting to read message.")

        for _ in range(size):
            current_byte = ser.read()
            msg.append(current_byte)

        current_byte = ser.read()

        if current_byte == end_byte:
            for variable in msg:
                print(variable)

        msg = []


main()
