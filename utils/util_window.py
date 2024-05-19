# This function is used to center the window
def window_center(window, width, height):
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()
    x = int((window_width/2) - (width/2))
    y = int((window_height/2) - (height/2))
    window.geometry("%dx%d+%d+%d" % (width, height, x, y))