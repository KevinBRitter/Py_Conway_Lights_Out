from tkinter import*


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.x_start = 10
        self.y_start = 10
        self.color = 'white'
        self.buttons_per_side = 10
        self.gaps = self.buttons_per_side + 1
        self.list_length = self.buttons_per_side * self.buttons_per_side
        self.box_list1 = [] * self.list_length
        self.box_list2 = [] * self.list_length
        self.box_list3 = [] * self.list_length
        for item in range(self.list_length):
            self.box_list1.append(True)
            self.box_list2.append(self.color)

        self.init_window()

    def init_window(self):

        self.master.title("Lights Out")
        self.pack(fill=BOTH, expand=1)

        menu_group = Menu(self.master)
        self.master.config(menu=menu_group)

        file = Menu(menu_group)
        file.add_command(label='New', command=self.client_exit)
        file.add_command(label='Load', command=self.client_exit)
        file.add_command(label='Save', command=self.client_exit)
        file.add_command(label='Exit', command=self.client_exit)

        edit = Menu(menu_group)
        edit.add_command(label='Undo')
        edit.add_command(label='Redo')

        menu_group.add_cascade(label='File', menu=file)
        menu_group.add_cascade(label='Edit', menu=edit)

    @staticmethod
    def client_exit():

        exit()


def new_box(x_left, y_left, x_right, y_right, fill_in):
    drawer.create_rectangle(x_left, y_left, x_right, y_right, fill=fill_in)


def callback(event):
    mouse_x = event.x
    mouse_y = event.y
    flip_lights(mouse_x, mouse_y)


def flip_lights(x_in, y_in):
    for box in app.box_list3:
        if box[0] < x_in < box[2] and box[1] < y_in < box[3]:
            if box[4] == 'yellow':
                box.pop(4)
                box.append('white')
            else:
                box.pop(4)
                box.append('yellow')
            # TODO flip_lights function has issues with tuple attributes.  trying to rewrite box[4] the color.


root = Tk()
root.geometry("410x400")
drawer = Canvas(root, width=400, height=390, bg='black')
drawer.bind("<Button-1>", callback)
drawer.pack()
app = Window(root)

for i in range(app.buttons_per_side):
    for j in range(app.buttons_per_side):
        new_width = (400 - app.gaps * app.x_start)/app.buttons_per_side
        new_height = (390 - app.gaps * app.x_start) / app.buttons_per_side
        new_x_left = j * app.x_start + app.x_start + j * new_width
        new_y_left = i * app.x_start + app.x_start + i * new_height
        new_x_right = j * app.x_start + app.x_start + j * new_width + new_width
        new_y_right = i * app.x_start + app.x_start + i * new_height + new_height
        new_draw = (new_x_left, new_y_left, new_x_right, new_y_right, "yellow")

        app.box_list3.append(new_draw)

for k in app.box_list3:
    # print(k)
    new_box(k[0], k[1], k[2], k[3], k[4])
root.mainloop()
