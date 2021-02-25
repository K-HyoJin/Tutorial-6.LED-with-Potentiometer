# Arduino example 6
Tutorial 6. LED with Potentiometer\
저항값를 측정하고 변화된 저항값에 따라서 LED가 깜박이는 속도를 다르게 동작하도록 제작

## circuit
LED : digital 13pin\
Potentiometer : analog 0pin\
![image](https://user-images.githubusercontent.com/79436159/109194012-55260e80-77dc-11eb-8893-6756935487f4.png)

## code
``` from pyfirmata import Arduino,util ```\
pyfirmata의 아두이노 모듈을 사용하기 위해 import함 

``` import time ```\
프로그램을 일정시간동안 지연시키기위해 time 모듈을 import함

``` board = Arduino('COM8')``` \
변수1 = Arduino('**포트번호**') 를 해서 보드와 연결 

``` analog_input = board.get_pin('a:0:i')``` \
  -> 0번핀을 analog신호 입력핀으로 설정\
  ```led = board.get_pin('d:13:o') ```\
  -> 13번 핀을 digital신호 출력핀으로 설정\
변수1 = 변수2.get_pin('**d or a** : **pin number** : **i or o** ') \
**d or a** : The type of the pin \
**pin number** : The number of the pin\
**i or o** : The mode of the pin 

  ``` it = util.Iterator(board) ```\
보드의 입력값을 지속적으로 업데이트해주는 iterator 변수 선언

 ``` it.start()``` \
iterator 시작

``` analog_value = analog_input.read() ```\
Photoresistor 연결된 0번핀의 입력을 읽어와서 변수 analog_value에 저장

``` 
if analog_value is not None:
  delay = analog_value + 0.01
  led.write(1)
  time.sleep(delay)
  led.write(0)
  time.sleep(delay)
else:
  time.sleep(0.1)
```
입력으로 들어온 analog_value 값이 None이 아니면 delay변수에 analog_value를 더해주어 지연시키고\
led가 켜지도록 1을 입력으로 줌\ delay만큼 지연시킨후 led가 꺼지도록 0을 입력으로 줌


