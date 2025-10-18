def right(speed: number, time: number):
    powerbrick.motor_run_dual(speed * m1 / 100, 0)
    if time == 0:
        return
    else:
        basic.pause(time * timefix)
        stop()
def back(speed2: number, time2: number):
    powerbrick.motor_run_dual(speed2 * (m1 * -1) / 100, speed2 * (m2 * -1) / 100)
    if time2 == 0:
        return
    else:
        basic.pause(time2 * timefix)
        stop()
def Coior():
    basic.show_icon(IconNames.TORTOISE)
    powerbrick.servo2_kg(powerbrick.Servos.S1, 170)
    basic.pause(500)
    back(100, 900)
    rotaghtleft(100, 700)
    front(100, 150)
    powerbrick.servo2_kg(powerbrick.Servos.S1, 30)
    basic.pause(500)
    back(100, 800)
    left(100, 500)
    basic.show_icon(IconNames.CONFUSED)
    循線2(80, 0)
    front(100, 400)
    rotaghtleft(100, 700)
    循線3(80, 0)
def 左內黑0():
    if powerbrick.tracer(powerbrick.Ports.PORT2, powerbrick.Slots.B):
        return 0
    return 1
def front(speed3: number, time3: number):
    powerbrick.motor_run_dual(speed3 * m1 / 100, speed3 * m2 / 100)
    if time3 == 0:
        return
    else:
        basic.pause(time3 * timefix)
        stop()
def left(speed4: number, time4: number):
    powerbrick.motor_run_dual(0, speed4 * m2 / 100)
    if time4 == 0:
        return
    else:
        basic.pause(time4 * timefix)
        stop()
def stop():
    powerbrick.motor_run_dual(0, 0)

def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
    Coior()
    basic.show_icon(IconNames.YES)
    front(80, 1220)
    stop()
    left(100, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def 循線(speed5: number, time5: number):
    global start, breakflag
    basic.show_icon(IconNames.TARGET)
    front(speed5 * 0.7, 0)
    while not (powerbrick.tracer(powerbrick.Ports.PORT3, powerbrick.Slots.B)) and not (powerbrick.tracer(powerbrick.Ports.PORT2, powerbrick.Slots.A)):
        basic.pause(10)
    basic.show_icon(IconNames.GIRAFFE)
    start = input.running_time()
    breakflag = 0
    while breakflag == 0:
        if not (powerbrick.tracer(powerbrick.Ports.PORT2, powerbrick.Slots.A)) and not (powerbrick.tracer(powerbrick.Ports.PORT3, powerbrick.Slots.B)):
            front(speed5, 0)
        elif powerbrick.tracer(powerbrick.Ports.PORT2, powerbrick.Slots.A) and not (powerbrick.tracer(powerbrick.Ports.PORT3, powerbrick.Slots.B)):
            left(speed5, 0)
        elif not (powerbrick.tracer(powerbrick.Ports.PORT2, powerbrick.Slots.A)) and powerbrick.tracer(powerbrick.Ports.PORT3, powerbrick.Slots.B):
            right(speed5, 0)
        elif powerbrick.tracer(powerbrick.Ports.PORT2, powerbrick.Slots.A) and powerbrick.tracer(powerbrick.Ports.PORT2, powerbrick.Slots.B):
            stop()
            rotaghtleft(speed5, 0)
        elif False and False:
            pass
        elif False and False:
            pass
def left2(speed6: number):
    rotaghtleft(speed6, 0)
    while 左內黑0() == 1:
        basic.pause(100)
    stop()
def 右內黑0():
    if powerbrick.tracer(powerbrick.Ports.PORT3, powerbrick.Slots.B):
        return 0
    return 1
def rotaghtleft(speed7: number, time6: number):
    powerbrick.motor_run_dual(speed7 * m1 / -100, speed7 * m2 / 100)
    if time6 == 0:
        return
    else:
        music.play(music.string_playable("C5 B - - - - - - ", 120),
            music.PlaybackMode.IN_BACKGROUND)
        basic.pause(time6 * timefix)
        stop()
def 循線3(speed8: number, time7: number):
    global start, breakflag
    basic.show_icon(IconNames.TARGET)
    front(speed8 * 0.7, 0)
    basic.show_icon(IconNames.GIRAFFE)
    start = input.running_time()
    breakflag = 0
    while breakflag == 0:
        if 左內黑0() == 1 and 右內黑0() == 1:
            front(speed8, 0)
        elif 左內黑0() == 0 and 右內黑0() == 1:
            left(speed8, 0)
        elif 左內黑0() == 1 and 右內黑0() == 0:
            right(speed8, 0)
        elif 左內黑0() == 0 and 右內黑0() == 0:
            front(speed8, 0)
        if 左外黑0() == 0 and 左外黑0() == 0 and (右外黑0() == 0 and 右內黑0() == 0):
            stop()
            breakflag = 1
            basic.show_icon(IconNames.SCISSORS)

def on_button_pressed_ab():
    pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def 右外黑0():
    if powerbrick.tracer(powerbrick.Ports.PORT3, powerbrick.Slots.A):
        return 0
    return 1
def rotaghtright(speed9: number, time8: number):
    powerbrick.motor_run_dual(speed9 * m1 / 100, speed9 * m1 / -100)
    if time8 == 0:
        return
    else:
        basic.pause(time8 * timefix)
        stop()
def 左外黑0():
    if powerbrick.tracer(powerbrick.Ports.PORT2, powerbrick.Slots.A):
        return 0
    return 1
def 循線2(speed10: number, time9: number):
    global start, breakflag
    basic.show_icon(IconNames.TARGET)
    front(speed10 * 0.7, 0)
    basic.show_icon(IconNames.GIRAFFE)
    start = input.running_time()
    breakflag = 0
    while breakflag == 0:
        if 左內黑0() == 1 and 右內黑0() == 1:
            front(speed10, 0)
        elif 左內黑0() == 0 and 右內黑0() == 1:
            left(speed10, 0)
        elif 左內黑0() == 1 and 右內黑0() == 0:
            right(speed10, 0)
        elif 左內黑0() == 0 and 右內黑0() == 0:
            front(speed10, 0)
        if 左外黑0() == 0:
            stop()
            breakflag = 1
breakflag = 0
start = 0
timefix = 0
m2 = 0
m1 = 0
basic.show_icon(IconNames.SQUARE)
powerbrick.GC_MODE(powerbrick.GCMode.PROXIMITY)
powerbrick.servo2_kg(powerbrick.Servos.S1, 10)
basic.pause(100)
powerbrick.motor_run(powerbrick.Motors.M1, 0)
basic.pause(100)
color = -1
m1 = -255
m2 = -220
power = 3.9
timefix = Math.map(power, 3.8, 4.2, 1.14, 1)
basic.show_icon(IconNames.CHESSBOARD)
# 綠150-180 light148-
# 紅330-360 light140-150 
# 藍198-202
# 黃50-60
# 白180-

def on_forever():
    pass
basic.forever(on_forever)
