import serial


def main():
    ser = serial.Serial(
        port="/dev/ttyUSB0",
        baudrate=115200,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.SEVENBITS,
    )

    header = b"\x02"
    end_byte = b"\n"
    size = 4
    msg = []

    print(f"Using serial port {ser.name}")

    current_byte = ser.read()

    while True:
        if current_byte != header:
            current_byte = ser.read()
            continue

        for _ in range(size):
            current_byte = ser.read()
            msg.append(current_byte)

        current_byte = ser.read()

        if current_byte == end_byte:
            print(f"Full message: {msg}\n")
            for variable in msg:
                pass

        msg = []

main()
