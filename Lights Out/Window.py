from tkinter import*


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.window_width = 400
        self.window_height = 390
        self.x_gap = 10
        self.y_gap = 10
        self.color = 'white'
        self.buttons_per_side = 10
        self.gaps = self.buttons_per_side + 1
        self.box_width = (self.window_width - self.gaps * self.x_gap) / self.buttons_per_side
        self.box_height = (self.window_height - self.gaps * self.x_gap) / self.buttons_per_side
        self.list_length = self.buttons_per_side * self.buttons_per_side
        self.box_list1 = [] * self.list_length
        self.box_list2 = [] * self.list_length
        self.box_list3 = [] * self.list_length
        for item in range(self.list_length):
            self.box_list1.append(True)
            self.box_list2.append(self.color)

        self.build_list(self)
        self.init_window()

    @staticmethod
    def build_list(self):
        for i in range(self.buttons_per_side):
            for j in range(self.buttons_per_side):
                new_width = self.box_width
                new_height = self.box_height
                new_x_left = (j + 1) * self.x_gap + j * new_width
                new_y_left = (i + 1) * self.y_gap + i * new_height
                new_x_right = (j + 1) * self.x_gap + (j + 1) * new_width
                new_y_right = (i + 1) * self.y_gap + (i + 1) * new_height
                new_draw = (new_x_left, new_y_left, new_x_right, new_y_right, "yellow")

                self.box_list3.append(new_draw)

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
    for box in range(len(app.box_list3)):
        if (app.box_list3[box][0] < x_in < app.box_list3[box][2] and
                app.box_list3[box][1] < y_in < app.box_list3[box][3]) or \
                (app.box_list3[box][0] < x_in - app.box_width - app.x_gap < app.box_list3[box][2] and
                 app.box_list3[box][1] < y_in < app.box_list3[box][3]) or \
                (app.box_list3[box][0] < x_in + app.box_width + app.x_gap < app.box_list3[box][2] and
                 app.box_list3[box][1] < y_in < app.box_list3[box][3]) or \
                (app.box_list3[box][0] < x_in < app.box_list3[box][2] and
                 app.box_list3[box][1] < y_in - app.box_height - app.y_gap < app.box_list3[box][3]) or \
                (app.box_list3[box][0] < x_in < app.box_list3[box][2] and
                 app.box_list3[box][1] < y_in + app.box_height + app.y_gap < app.box_list3[box][3]):
            if app.box_list3[box][4] == 'yellow':
                app.box_list3[box] = (app.box_list3[box][0], app.box_list3[box][1], app.box_list3[box][2],
                                      app.box_list3[box][3], 'white')
            else:
                app.box_list3[box] = (app.box_list3[box][0], app.box_list3[box][1], app.box_list3[box][2],
                                      app.box_list3[box][3], 'yellow')

        new_box(app.box_list3[box][0], app.box_list3[box][1], app.box_list3[box][2],
                app.box_list3[box][3], app.box_list3[box][4])


root = Tk()
root.geometry("410x400")
drawer = Canvas(root, width=400, height=390, bg='black')
drawer.bind("<Button-1>", callback)
drawer.pack()
app = Window(root)

for k in app.box_list3:
    # print(k)
    new_box(k[0], k[1], k[2], k[3], k[4])
root.mainloop()
