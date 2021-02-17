# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals 
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]
LEFT = False
RIGHT = True
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_mov = 0
paddle2_mov = 0
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0


# initializes ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel 
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == RIGHT:
        ball_vel = [random.randrange(3, 6), -random.randrange(3, 6)]
    elif direction == LEFT:
        ball_vel = [-random.randrange(3, 6), -random.randrange(3, 6)]

# new game is created
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2  
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    if RIGHT == True:
        spawn_ball(RIGHT)
    elif LEFT == True:
        spawn_ball(LEFT)
        
# downwards movement of paddles       
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_mov, paddle2_mov
    paddle1_vel = 15
    paddle2_vel = 15
    if key == simplegui.KEY_MAP["w"]:
        paddle1_mov -= paddle1_vel
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_mov += paddle1_vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_mov -= paddle2_vel
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_mov += paddle2_vel
        
# upwards movement of paddles
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle1_mov, paddle2_mov
    if key == simplegui.KEY_MAP["w"]:
        paddle1_mov = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_mov = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_mov = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_mov = 0

# drawing the lines, ball, and paddles
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos
    global ball_pos, ball_vel
    global RIGHT, LEFT
    
    # position of ball and paddles is updated
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    paddle1_pos += paddle1_mov
    paddle2_pos += paddle2_mov
        
    # mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # reflection of ball when it hits the upper and lower boundaries
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= HEIGHT - BALL_RADIUS):
        ball_vel[0] = ball_vel[0]
        ball_vel[1] = -ball_vel[1]
     
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # paddle's vertical position is updated to make sure it is within the screen
    if paddle1_pos < PAD_HEIGHT/2:
        paddle1_pos = PAD_HEIGHT/2
    elif paddle1_pos > HEIGHT - PAD_HEIGHT/2:
        paddle1_pos = HEIGHT - PAD_HEIGHT/2
                
    if paddle2_pos < PAD_HEIGHT/2:
        paddle2_pos = PAD_HEIGHT/2
    elif paddle2_pos > HEIGHT - PAD_HEIGHT/2:
        paddle2_pos = HEIGHT - PAD_HEIGHT/2
        
    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos - HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT), (0, paddle1_pos + HALF_PAD_HEIGHT)], 2, "White") 
    canvas.draw_polygon([(WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH, paddle2_pos + HALF_PAD_HEIGHT), (WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT)], 2, "White")  
    
    # determines whether paddle and ball collide    
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if (ball_pos[1] < paddle1_pos - PAD_HEIGHT/2) or (ball_pos[1] > paddle1_pos + PAD_HEIGHT/2):
            RIGHT = True
            LEFT = False
            spawn_ball(RIGHT)
            score2 += 1
        else:
            ball_vel[0] = -(1.1 * ball_vel[0])
            ball_vel[1] = ball_vel[1]
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if (ball_pos[1] < paddle2_pos - PAD_HEIGHT/2) or (ball_pos[1] > paddle2_pos + PAD_HEIGHT/2):
            RIGHT = False
            LEFT = True
            spawn_ball(LEFT)
            score1 +=1
        else:
            ball_vel[0] = -(1.1* ball_vel[0])
            ball_vel[1] = ball_vel[1]
    
    # draw scores
    canvas.draw_text(str(score1), [70, 60], 36, "White")
    canvas.draw_text(str(score2), [530, 60], 36, "White")
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# add Restart button
frame.add_button("Restart", new_game, 100)

# start frame
frame.start()






