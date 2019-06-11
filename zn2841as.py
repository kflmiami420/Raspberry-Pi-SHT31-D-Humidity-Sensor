# credit goes to donly (https://github.com/donly/sht31demo/blob/master/zn2841as.py)

#!/usr/bin/env python
#encoding: utf-8

import RPi.GPIO
import time

# 定义单个数码管各段led对应的GPIO口
LED_A = 20
LED_B = 21
LED_C = 6
LED_D = 19
LED_E = 26
LED_F = 16
LED_G = 5
LED_DP = 13

# 定义1到4号数码管阳极对应的GPIO口
DIGIT1 = 17
DIGIT2 = 27
DIGIT3 = 22
DIGIT4 = 23

# 定义按钮输入的GPIO口
btn = 27

RPi.GPIO.setmode(RPi.GPIO.BCM)

#RPi.GPIO.output(DIGIT1, False)
#RPi.GPIO.output(DIGIT2, False)
#RPi.GPIO.output(DIGIT3, False)
#RPi.GPIO.output(DIGIT4, False)

#RPi.GPIO.setup(btn, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)

# 指定no(1-4)号数码管显示数字num(0-9)，第三个参数是显示不显示小数点（true/false）
def showDigit(no, num, showDotPoint):
  # 先将负极拉高，关掉显示
  RPi.GPIO.output(DIGIT1, True)
  RPi.GPIO.output(DIGIT2, True)
  RPi.GPIO.output(DIGIT3, True)
  RPi.GPIO.output(DIGIT4, True)

  if (num == 0) :
    RPi.GPIO.output(LED_A, True)
    RPi.GPIO.output(LED_B, True)
    RPi.GPIO.output(LED_C, True)
    RPi.GPIO.output(LED_D, True)
    RPi.GPIO.output(LED_E, True)
    RPi.GPIO.output(LED_F, True)
    RPi.GPIO.output(LED_G, False)
  elif (num == 1) :
    RPi.GPIO.output(LED_A, False)
    RPi.GPIO.output(LED_B, True)
    RPi.GPIO.output(LED_C, True)
    RPi.GPIO.output(LED_D, False)
    RPi.GPIO.output(LED_E, False)
    RPi.GPIO.output(LED_F, False)
    RPi.GPIO.output(LED_G, False) 
  elif (num == 2) :
    RPi.GPIO.output(LED_A, True)
    RPi.GPIO.output(LED_B, True)
    RPi.GPIO.output(LED_C, False)
    RPi.GPIO.output(LED_D, True)
    RPi.GPIO.output(LED_E, True)
    RPi.GPIO.output(LED_F, False)
    RPi.GPIO.output(LED_G, True)
  elif (num == 3) :
    RPi.GPIO.output(LED_A, True)
    RPi.GPIO.output(LED_B, True)
    RPi.GPIO.output(LED_C, True)
    RPi.GPIO.output(LED_D, True)
    RPi.GPIO.output(LED_E, False)
    RPi.GPIO.output(LED_F, False)
    RPi.GPIO.output(LED_G, True)
  elif (num == 4) :
    RPi.GPIO.output(LED_A, False)
    RPi.GPIO.output(LED_B, True)
    RPi.GPIO.output(LED_C, True)
    RPi.GPIO.output(LED_D, False)
    RPi.GPIO.output(LED_E, False)
    RPi.GPIO.output(LED_F, True)
    RPi.GPIO.output(LED_G, True)
  elif (num == 5) :
    RPi.GPIO.output(LED_A, True)
    RPi.GPIO.output(LED_B, False)
    RPi.GPIO.output(LED_C, True)
    RPi.GPIO.output(LED_D, True)
    RPi.GPIO.output(LED_E, False)
    RPi.GPIO.output(LED_F, True)
    RPi.GPIO.output(LED_G, True)
  elif (num == 6) :
    RPi.GPIO.output(LED_A, True)
    RPi.GPIO.output(LED_B, False)
    RPi.GPIO.output(LED_C, True)
    RPi.GPIO.output(LED_D, True)
    RPi.GPIO.output(LED_E, True)
    RPi.GPIO.output(LED_F, True)
    RPi.GPIO.output(LED_G, True)
  elif (num == 7) :
    RPi.GPIO.output(LED_A, True)
    RPi.GPIO.output(LED_B, True)
    RPi.GPIO.output(LED_C, True)
    RPi.GPIO.output(LED_D, False)
    RPi.GPIO.output(LED_E, False)
    RPi.GPIO.output(LED_F, False)
    RPi.GPIO.output(LED_G, False)
  elif (num == 8) :
    RPi.GPIO.output(LED_A, True)
    RPi.GPIO.output(LED_B, True)
    RPi.GPIO.output(LED_C, True)
    RPi.GPIO.output(LED_D, True)
    RPi.GPIO.output(LED_E, True)
    RPi.GPIO.output(LED_F, True)
    RPi.GPIO.output(LED_G, True)
  elif (num == 9) :
    RPi.GPIO.output(LED_A, True)
    RPi.GPIO.output(LED_B, True)
    RPi.GPIO.output(LED_C, True)
    RPi.GPIO.output(LED_D, True)
    RPi.GPIO.output(LED_E, False)
    RPi.GPIO.output(LED_F, True)
    RPi.GPIO.output(LED_G, True)

  RPi.GPIO.output(LED_DP, False)
  if (no == 1) :
    RPi.GPIO.output(DIGIT1, False)
    RPi.GPIO.output(LED_DP, True)
  elif (no == 2) :
    RPi.GPIO.output(DIGIT2, False)
  elif (no == 3) :
    RPi.GPIO.output(DIGIT3, False)
  elif (no == 4) :
    RPi.GPIO.output(DIGIT4, False)

def setup():
  RPi.GPIO.setup(LED_A, RPi.GPIO.OUT)
  RPi.GPIO.setup(LED_B, RPi.GPIO.OUT)
  RPi.GPIO.setup(LED_C, RPi.GPIO.OUT)
  RPi.GPIO.setup(LED_D, RPi.GPIO.OUT)
  RPi.GPIO.setup(LED_E, RPi.GPIO.OUT)
  RPi.GPIO.setup(LED_F, RPi.GPIO.OUT)
  RPi.GPIO.setup(LED_G, RPi.GPIO.OUT)
  RPi.GPIO.setup(LED_DP, RPi.GPIO.OUT)
  RPi.GPIO.setup(DIGIT1, RPi.GPIO.OUT)
  RPi.GPIO.setup(DIGIT2, RPi.GPIO.OUT)
  RPi.GPIO.setup(DIGIT3, RPi.GPIO.OUT)
  RPi.GPIO.setup(DIGIT4, RPi.GPIO.OUT)

def showTemp(temp):
  setup()
  try:
    tem = int(temp) 
    f = int((round(temp, 2)-tem)*100);
    print f
    t=0.005
    while True:
      time.sleep(t)
      showDigit(1, tem/10, False)
      time.sleep(t)
      showDigit(2, tem%10, True)
      time.sleep(t)
      showDigit(3, f/10, False)
      time.sleep(t)
      showDigit(4, f%10, False)
  except KeyboardInterrupt, ValueError:
    RPi.GPIO.cleanup()
