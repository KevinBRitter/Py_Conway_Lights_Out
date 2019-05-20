from tkinter import*


class Conways(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.conways = False
        self.window_width = 600
        self.window_height = 590
        self.x_gap = 2
        self.y_gap = 2
        self.color = 'blue'
        self.buttons_per_side = 40
        self.gaps = self.buttons_per_side + 1
        self.box_width = (self.window_width - self.gaps * self.x_gap) / self.buttons_per_side
        self.box_height = (self.window_height - self.gaps * self.x_gap) / self.buttons_per_side
        self.list_length = self.buttons_per_side * self.buttons_per_side
        self.box_list1 = [] * self.list_length
        self.box_list2 = [] * self.list_length
        self.box_list3 = [] * self.list_length
        self.box_list4 = [] * self.list_length
        for item in range(self.list_length):
            self.box_list1.append(True)
            self.box_list2.append(self.color)
            self.box_list4.append(self.color)

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

        self.master.title("Conway's Game of Life")
        self.pack(fill=BOTH, expand=1)

        menu_group = Menu(self.master)
        self.master.config(menu=menu_group)

        file = Menu(menu_group)
        file.add_command(label='New', command=self.new_game)
        file.add_command(label='Load', command=self.load_game)
        file.add_command(label='Save', command=self.save_game)
        file.add_command(label='Exit', command=self.client_exit)

        edit = Menu(menu_group)
        edit.add_command(label='Undo')
        edit.add_command(label='Redo')

        time = Menu(menu_group)
        time.add_command(label='Start', command=self.start_animation)
        time.add_command(label='Stop', command=self.stop_animation)

        menu_group.add_cascade(label='File', menu=file)
        menu_group.add_cascade(label='Edit', menu=edit)
        menu_group.add_cascade(label='Time', menu=time)

    @staticmethod
    def client_exit():

        exit()

    @staticmethod
    def new_game():
        for box in range(len(app.box_list3)):
            app.box_list3[box] = (app.box_list3[box][0], app.box_list3[box][1], app.box_list3[box][2],
                                  app.box_list3[box][3], 'red')

            new_box(box, app.box_list3[box][0], app.box_list3[box][1], app.box_list3[box][2],
                    app.box_list3[box][3], app.box_list3[box][4])

    @staticmethod
    def load_game():
        # TODO create a load game method to recover a saved game state
        exit()  # temp code place holder

    @staticmethod
    def save_game():
        # TODO create a save state to save games between plays
        exit()  # temp code place holder

    @staticmethod
    def start_animation():
        change_conways_state(True)
        right_click(None)

    @staticmethod
    def stop_animation():
        change_conways_state(False)


def new_box(index_in, x_left, y_left, x_right, y_right, fill_in):
    app.box_list2[index_in] = drawer.create_rectangle(x_left, y_left, x_right, y_right, fill=fill_in)


def re_draw(index_in):
    drawer.delete(app.box_list2[index_in])
    app.box_list2[index_in] = drawer.create_rectangle(app.box_list3[index_in][0], app.box_list3[index_in][1],
                                                      app.box_list3[index_in][2], app.box_list3[index_in][3],
                                                      fill=app.box_list3[index_in][4])


def left_click(event):
    mouse_x = event.x
    mouse_y = event.y
    flip_lights(mouse_x, mouse_y)


def right_click(event):
    app.conways = True
    # for num in range(10):
    while app.conways:
        app.after(200)
        run_conways()
        app.update()


def flip_lights(x_in, y_in):
    for box in range(len(app.box_list3)):
        if (app.box_list3[box][0] < x_in < app.box_list3[box][2] and
                app.box_list3[box][1] < y_in < app.box_list3[box][3]):
            if app.box_list3[box][4] == 'red':
                app.box_list3[box] = (app.box_list3[box][0], app.box_list3[box][1], app.box_list3[box][2],
                                      app.box_list3[box][3], 'blue')
            else:
                app.box_list3[box] = (app.box_list3[box][0], app.box_list3[box][1], app.box_list3[box][2],
                                      app.box_list3[box][3], 'red')

        re_draw(box)


def change_conways_state(bool_in):
    app.conways = bool_in


def run_conways():
    for cell in range(len(app.box_list3)):
        app.box_list4[cell] = life_evaluator(cell)

    for cell in range(len(app.box_list3)):
        if app.box_list3[cell][4] != app.box_list4[cell]:
            app.box_list3[cell] = (app.box_list3[cell][0], app.box_list3[cell][1], app.box_list3[cell][2],
                                   app.box_list3[cell][3], app.box_list4[cell])

            re_draw(cell)

    # TODO this time delay is lagging out the screen.
    # app.after(500)


def life_evaluator(index_in):
    live_neighbors = 0
    # Rules - 1. if dead, 3 live neighbors = live, 2. if alive, 2 or 3 live neighbors = live
    # 3. if 4 neighbors = overcrowded/ die, 4. if alive, 1 or 0 neighbors = lonely/ die

    # Check West
    if index_in - 1 > -1 and index_in % app.buttons_per_side != 0:
        # If there is a cell 'left of' and it's not on the right wall, making them non adjacent
        if app.box_list3[index_in - 1][4] == 'red':
            # If that cell is also alive
            live_neighbors += 1

    # Check North West
    if index_in - app.buttons_per_side - 1 > -1 and index_in % app.buttons_per_side != 0:
        # If there is a cell above left
        if app.box_list3[index_in - app.buttons_per_side - 1][4] == 'red':
            # If that cell is also alive
            live_neighbors += 1

    # Check North
    if index_in - app.buttons_per_side > -1:
        # If there is a cell above
        if app.box_list3[index_in - app.buttons_per_side][4] == 'red':
            # If that cell is also alive
            live_neighbors += 1

    # Check North East
    if index_in - app.buttons_per_side + 1 > -1 and (index_in + 1) % app.buttons_per_side != 0:
        # If there is a cell above right
        if app.box_list3[index_in - app.buttons_per_side + 1][4] == 'red':
            # If that cell is also alive
            live_neighbors += 1

    # Check East
    if index_in + 1 < app.list_length and (index_in + 1) % app.buttons_per_side != 0:
        # if there is a cell 'right of' and it's not on the left wall, making them non adjacent
        if app.box_list3[index_in + 1][4] == 'red':
            # If that cell is also alive
            live_neighbors += 1

    # Check South West
    if index_in + app.buttons_per_side - 1 < app.list_length and index_in % app.buttons_per_side != 0:
        # If there is a cell below left
        if app.box_list3[index_in + app.buttons_per_side - 1][4] == 'red':
            # If that cell is also alive
            live_neighbors += 1

    # Check South
    if index_in + app.buttons_per_side < app.list_length:
        # If there is a cell below
        if app.box_list3[index_in + app.buttons_per_side][4] == 'red':
            # If that cell is also alive
            live_neighbors += 1

    # Check South East
    if index_in + app.buttons_per_side + 1 < app.list_length and (index_in + 1) % app.buttons_per_side != 0:
        # If there is a cell below left
        if app.box_list3[index_in + app.buttons_per_side + 1][4] == 'red':
            # If that cell is also alive
            live_neighbors += 1

    if live_neighbors >= 4:
        return 'blue'
    elif live_neighbors == 3:
        return 'red'
    elif live_neighbors == 2:
        if app.box_list3[index_in][4] == 'red':
            return 'red'
        else:
            return 'blue'
    else:
        return 'blue'


# root is the master for the tkinter
root = Tk()
root.geometry("610x600")

# drawer is the new canvas using root(master)
drawer = Canvas(root, width=600, height=590, bg='black')
# add mouse click as an input to the canvas
drawer.bind("<Button-1>", left_click)
drawer.bind("<Button-3>", right_click)
# pack adds the canvas to the window
drawer.pack()
app = Conways(root)

root.mainloop()
root.destroy()
