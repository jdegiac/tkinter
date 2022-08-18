# Image viewer with status bar
from tkinter import *
from PIL import ImageTk, Image

# root widget, has to happen before anything else
root = Tk()
root.title("Learn to Code with me")
root.iconbitmap('/Users/jordan/Projects/tkinterTutorial/python.svg')

my_img = ImageTk.PhotoImage(Image.open('/Users/jordan/Pictures/Screen Shot 2021-12-11 at 3.03.32 PM.png'))
my_img2 = ImageTk.PhotoImage(Image.open('/Users/jordan/Pictures/Screen Shot 2021-12-09 at 9.10.27 PM.png'))
my_img3 = ImageTk.PhotoImage(Image.open('/Users/jordan/Pictures/Screen Shot 2022-08-05 at 11.54.55 AM.png'))
my_img4 = ImageTk.PhotoImage(Image.open('/Users/jordan/Pictures/Screen Shot 2021-12-11 at 3.03.32 PM.png'))
my_img5 = ImageTk.PhotoImage(Image.open('/Users/jordan/Pictures/Screen Shot 2022-08-05 at 1.39.29 PM.png'))

image_list = [my_img, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)


# FUNCTIONS
def forward(img_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[img_num-1])
    button_forward = Button(root, text=">>", command=lambda:forward(img_num+1))
    button_back = Button(root, text="<<", command=lambda:back(img_num-1))
    
    # Grey out when last photo
    if img_num == 5:
        button_forward = Button(root, text=">>", state= DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Update Status Bar
    status = Label(root, text="Image " + str(img_num) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(img_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[img_num-1])
    button_forward = Button(root, text=">>", command=lambda:forward(img_num+1))
    button_back = Button(root, text="<<", command=lambda:back(img_num-1))
    
    # Grey out when first photo
    if img_num == 1:
        button_back = Button(root, text="<<", state= DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Update Status Bar
    status = Label(root, text="Image " + str(img_num) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back= Button(root,text="<<", command=lambda:back(), state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward= Button(root,text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=5)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# main loop
root.mainloop()

