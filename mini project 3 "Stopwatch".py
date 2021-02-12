# "Stopwatch: The Game"

import simplegui

# define global variables

counter = 0
total_clicks = 0
correct_clicks = 0
stopwatch_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    global stopwatch_running
    global decimal
    minute = int(t / 600)
    second = int((t % 600) / 10)
    decimal = t % 10
    if t == 0:
        return "0:00.0"
    else:
        if second <= 9:
            return str(minute) + ":" + "0" + str(second) + "." + str(decimal)
        else:
            return str(minute) + ":" + str(second) + "." + str(decimal)
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    global stopwatch_running
    stopwatch_running = True
    timer.start()
    
def stop():
    global decimal
    global total_clicks
    global correct_clicks
    global stopwatch_running
    timer.stop()
    if stopwatch_running == True:
        stopwatch_running = False
        total_clicks += 1
        if decimal == 0:
            correct_clicks += 1
    
def reset():
    global counter
    global total_clicks
    global correct_clicks
    global stopwatch_running
    counter = 0
    stopwatch_running = False
    total_clicks = 0
    correct_clicks = 0

# define event handler for timer with 0.1 sec interval

def tick():
    global counter
    if stopwatch_running == True:
        counter += 1
    
# define draw handler

def draw(canvas):
    canvas.draw_text(str(format(counter)), [150, 100], 28, "White")
    canvas.draw_text(str(correct_clicks) + "/" + str(total_clicks), [350, 50], 28, "Green")

# create frame

frame = simplegui.create_frame("Stopwatch", 400, 200)

# register event handlers

frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)

# start frame

frame.start()
timer.start()


