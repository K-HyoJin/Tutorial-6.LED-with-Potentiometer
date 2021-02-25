from pyfirmata import Arduino,util
import time

#핀 모드설정
board = Arduino('COM8')
analog_input= board.get_pin('a:0:i') # 0번핀 입력
led = board.get_pin('d:13:o') # 13번핀 출력

it = util.Iterator(board) # 회로의 입력상태를 읽어올 변수 선언
it.start()

while True:
    analog_value = analog_input.read()
    if analog_value is not None:
        delay = analog_value + 0.01
        print(analog_value)
        led.write(1)
        time.sleep(delay)
        led.write(0)
        time.sleep(delay)
    else:
        time.sleep(0.1)


