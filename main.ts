function right (speed: number, time: number) {
    powerbrick.MotorRunDual(speed * m1 / 100, 0)
    if (time == 0) {
        return
    } else {
        basic.pause(time * timefix)
        stop()
    }
}
function back (speed: number, time: number) {
    powerbrick.MotorRunDual(speed * (m1 * -1) / 100, speed * (m2 * -1) / 100)
    if (time == 0) {
        return
    } else {
        basic.pause(time * timefix)
        stop()
    }
}
function Coior () {
    basic.showIcon(IconNames.Tortoise)
    powerbrick.Servo2KG(powerbrick.Servos.S1, 170)
    basic.pause(500)
    back(100, 900)
    rotaghtleft(100, 700)
    powerbrick.Servo2KG(powerbrick.Servos.S1, 30)
    basic.pause(500)
    back(100, 800)
    left(100, 500)
    basic.showIcon(IconNames.Confused)
    循線2(80, 0)
    rotaghtleft(100, 700)
    循線3(80, 0)
}
function 左內黑0 () {
    if (powerbrick.Tracer(powerbrick.Ports.PORT2, powerbrick.Slots.B)) {
        return 0
    }
    return 1
}
function front (speed: number, time: number) {
    powerbrick.MotorRunDual(speed * m1 / 100, speed * m2 / -100)
    if (time == 0) {
        return
    } else {
        basic.pause(time * timefix)
        stop()
    }
}
function left (speed: number, time: number) {
    powerbrick.MotorRunDual(0, speed * m2 / 100)
    if (time == 0) {
        return
    } else {
        basic.pause(time * timefix)
        stop()
    }
}
function stop () {
    powerbrick.MotorRunDual(0, 0)
}
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Heart)
    Coior()
    basic.showIcon(IconNames.Yes)
    stop()
    left(100, 1000)
})
function 循線 (speed: number, time: number) {
    basic.showIcon(IconNames.Target)
    while (!(powerbrick.Tracer(powerbrick.Ports.PORT3, powerbrick.Slots.B)) && !(powerbrick.Tracer(powerbrick.Ports.PORT2, powerbrick.Slots.A))) {
        basic.pause(10)
    }
    basic.showIcon(IconNames.Giraffe)
    start = input.runningTime()
    breakflag = 0
    while (breakflag == 0) {
        if (!(powerbrick.Tracer(powerbrick.Ports.PORT2, powerbrick.Slots.A)) && !(powerbrick.Tracer(powerbrick.Ports.PORT3, powerbrick.Slots.B))) {
        	
        } else if (powerbrick.Tracer(powerbrick.Ports.PORT2, powerbrick.Slots.A) && !(powerbrick.Tracer(powerbrick.Ports.PORT3, powerbrick.Slots.B))) {
            left(speed, 0)
        } else if (!(powerbrick.Tracer(powerbrick.Ports.PORT2, powerbrick.Slots.A)) && powerbrick.Tracer(powerbrick.Ports.PORT3, powerbrick.Slots.B)) {
            right(speed, 0)
        } else if (powerbrick.Tracer(powerbrick.Ports.PORT2, powerbrick.Slots.A) && powerbrick.Tracer(powerbrick.Ports.PORT2, powerbrick.Slots.B)) {
            stop()
            rotaghtleft(speed, 0)
        } else if (false && false) {
        	
        } else if (false && false) {
        	
        }
    }
}
function left2 (speed: number) {
    rotaghtleft(speed, 0)
    while (左內黑0() == 1) {
        basic.pause(100)
    }
    stop()
}
function 右內黑0 () {
    if (powerbrick.Tracer(powerbrick.Ports.PORT3, powerbrick.Slots.B)) {
        return 0
    }
    return 1
}
function rotaghtleft (speed: number, time: number) {
    powerbrick.MotorRunDual(speed * m1 / -100, speed * m2 / 100)
    if (time == 0) {
        return
    } else {
        music.play(music.stringPlayable("C5 B - - - - - - ", 120), music.PlaybackMode.InBackground)
        basic.pause(time * timefix)
        stop()
    }
}
function 循線3 (speed: number, time: number) {
    basic.showIcon(IconNames.Target)
    basic.showIcon(IconNames.Giraffe)
    start = input.runningTime()
    breakflag = 0
    while (breakflag == 0) {
        if (左內黑0() == 1 && 右內黑0() == 1) {
        	
        } else if (左內黑0() == 0 && 右內黑0() == 1) {
            left(speed, 0)
        } else if (左內黑0() == 1 && 右內黑0() == 0) {
            right(speed, 0)
        } else if (左內黑0() == 0 && 右內黑0() == 0) {
        	
        }
        if (左外黑0() == 0 && 左外黑0() == 0 && (右外黑0() == 0 && 右內黑0() == 0)) {
            stop()
            breakflag = 1
            basic.showIcon(IconNames.Scissors)
        }
    }
}
input.onButtonPressed(Button.AB, function () {
	
})
input.onButtonPressed(Button.B, function () {
    powerbrick.MotorRunDual(255, 255)
    music.play(music.tonePlayable(440, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
})
function 右外黑0 () {
    if (powerbrick.Tracer(powerbrick.Ports.PORT3, powerbrick.Slots.A)) {
        return 0
    }
    return 1
}
function rotaghtright (speed: number, time: number) {
    powerbrick.MotorRunDual(speed * m1 / 100, speed * m1 / -100)
    if (time == 0) {
        return
    } else {
        basic.pause(time * timefix)
        stop()
    }
}
function 左外黑0 () {
    if (powerbrick.Tracer(powerbrick.Ports.PORT2, powerbrick.Slots.A)) {
        return 0
    }
    return 1
}
function 循線2 (speed: number, time: number) {
    basic.showIcon(IconNames.Target)
    basic.showIcon(IconNames.Giraffe)
    start = input.runningTime()
    breakflag = 0
    while (breakflag == 0) {
        if (左內黑0() == 1 && 右內黑0() == 1) {
        	
        } else if (左內黑0() == 0 && 右內黑0() == 1) {
            left(speed, 0)
        } else if (左內黑0() == 1 && 右內黑0() == 0) {
            right(speed, 0)
        } else if (左內黑0() == 0 && 右內黑0() == 0) {
        	
        }
        if (左外黑0() == 0) {
            stop()
            breakflag = 1
        }
    }
}
let breakflag = 0
let start = 0
let timefix = 0
let m2 = 0
let m1 = 0
music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
let color = 0
m1 = 255
m2 = 220
let power = 4
timefix = Math.map(power, 3.8, 4.2, 1.14, 1)
// 綠150-180 light148-
// 紅330-360 light140-150 
// 藍198-202
// 黃50-60
// 白180-
basic.forever(function () {
	
})
