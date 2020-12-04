
# my screen resolution is 1440*900


from tkinter import Tk, Canvas, PhotoImage, Label, Button, messagebox
import random
import time

the_whole_item_FPS = 500
present_falling_FPS = 30
time_refresh_FPS = 1000
judge_man_and_present_FPS = 500
dict1 = {}   # to store the random item
left_bottom_y = {}
left_bottom_x = {}
right_top_x = {}
right_top_y = {}  # to record the coordinates

number = 0

game_time = 35  # game lasts for 35 seconds
man_x = 300  # the place of the man
score = 0

t = False
f = False
is_suspend = False

window = Tk()
window.title("Christmas present")
window.geometry("700x500")

canvas = Canvas(window, bg="light blue", width=500, height=700)

canvas.pack()

santa_claus = PhotoImage(file='santa_claus.png')
present = PhotoImage(file='present.png')
bomb = PhotoImage(file='bomb.png')


def time_refresh():
    global score
    global game_time
    global present_falling_FPS
    global the_whole_item_FPS
    # execute this code every second
    if game_time > 0:
        if not is_suspend:
            game_time -= 1
            Label(window, text=game_time,
                     width=2, height=1).place(x=60, y=5)
        window.after(time_refresh_FPS, time_refresh)
    # after 30 seconds the game will end
    else:
        del present_falling_FPS
        del the_whole_item_FPS
        messagebox.showinfo(title="Game ends!",
                               message="Your score is: " +
                               str(score) + " Happy Christmas!")
        window.destroy()


def judge_man_and_present():
    global t
    global f
    global score

    if f and t is False:
        score += 10
        Label(window, text=score, width=4, height=1).place(x=130, y=5)
        f = False
    elif t and f is False:
        score += 5
        Label(window, text=score, width=4, height=1).place(x=130, y=5)
        t = False
    elif t and f:
        score -= 30
        Label(window, text=score, width=4, height=1).place(x=130, y=5)
        f = False
        t = False
    window.after(judge_man_and_present_FPS, judge_man_and_present)


def present_falling():
    global dict1
    global man_x
    global t
    global f
    if not is_suspend:
        for i in list(dict1.keys()):
            # judge whether the item collides with the man
            if (man_x < left_bottom_x[i] < man_x + 40 or
                man_x < right_top_x[i] < man_x + 40) and (
                    460 < left_bottom_y[i] < 499 or 460 <
                    right_top_y[i] < 499):
                canvas.move(dict1[i], 0, 150)
                if i[0:2] == 'present':
                    t = True
                    f = False
                elif i[0:2] == 'bomb':
                    t = True
                    f = True
                else:
                    f = True
                    t = False
            if left_bottom_y[i] < 550:  # refresh the window to let items fall
                left_bottom_y[i] += 5
                canvas.move(dict1[i], 0, 5)
            else:  # let bottomed item disappear
                del dict1[i]
    window.after(present_falling_FPS, present_falling)

# create an item randomly


def the_whole_item():
    global item_number
    global number
    global santa_claus
    global present
    global bomb
    global score
    if not is_suspend:
        list1 = [santa_claus, present, bomb]
        item = random.choice(list1)
        # separate the items
        number = number + 1
        if item == santa_claus:
            item_number = 'santa_claus' + str(number)
        elif item == present:
            item_number = 'present' + str(number)
        else:
            item_number = 'bomb' + str(number)

        random_number = random.randint(0, 650)
        # let the item appear on the window randomly
        dict1[item_number] = canvas.create_image(random_number, 0,
                                                 anchor='sw', image=item)
        left_bottom_y[item_number] = 0
        left_bottom_x[item_number] = random_number
        if item == santa_claus:
            right_top_x[item_number] = random_number + 20
            right_top_y[item_number] = 0 - 40
        elif item == present:
            right_top_x[item_number] = random_number + 30
            right_top_y[item_number] = 0 - 20
        else:
            right_top_x[item_number] = random_number + 35
            right_top_y[item_number] = 0 - 30
    window.after(the_whole_item_FPS, the_whole_item)


def left(e):
    global man_x
    # stop when hitting the edge
    if man_x > 0:
        canvas.move(set_man, -10, 0)
        man_x = man_x-10


def right(w):
    global man_x
    if man_x < 460:
        canvas.move(set_man, 10, 0)
        man_x = man_x+10


def suspend(event):
    global is_suspend
    is_suspend = not is_suspend


def begin_click():
    global man
    global set_man
    global pre_score
    global is_suspend

    begin.destroy()
    if not is_suspend:
        remaining_time = Label(window,
                                  text='timeremain: ', width=8, height=1)
        remaining_time.place(x=-2, y=5)

        Label(window, text=game_time, width=2, height=1).place(x=60, y=5)

        pre_score = Label(window, text="Score: ", width=4, height=1)
        pre_score.place(x=90, y=5)

        Label(window, text=score, width=4, height=1).place(x=130, y=5)

        suspend = Label(window,
                           text="press 's' to pause", width=90, height=1)
        suspend.place(x=150, y=5)

        Label(window, width=16, height=1).place(x=160, y=5)

        man = PhotoImage(file="man.png")

        set_man = canvas.create_image(330, 460, anchor='nw', image=man)

        # use the_whole_item function every the_whole_item_FPS second
    window.after(the_whole_item_FPS, the_whole_item)
    window.after(present_falling_FPS, present_falling)
    window.after(time_refresh_FPS, time_refresh)
    window.after(judge_man_and_present_FPS, judge_man_and_present)
# trigger left or right event
canvas.bind_all("<KeyPress-Left>", left)
canvas.bind_all("<KeyPress-Right>", right)
# trigger suspend event
canvas.bind_all("<KeyPress-s>", suspend)

begin = Button(window, text="Begin!",
                  height=2, width=10, command=begin_click)
begin.place(x=300, y=220)


window.mainloop()
