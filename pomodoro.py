import tkinter as tk
import pygame
minutes = 25
seconds = 0
music = ''
pause = False
timer_id = None
BACKGORUNDS = ["static/backgrounds/bg.png", "static/backgrounds/bg2.png", "static/backgrounds/bg3.png", "static/backgrounds/bg4.png", "static/backgrounds/bg5.png","static/backgrounds/bg6.png","static/backgrounds/bg7.png","static/backgrounds/bg8.png","static/backgrounds/bg9.png"]   
background_index = 0
break_count = False
PAUSE_IMG = "static/pause.png"
PLAY_IMG = "static/play.png"
RESET_IMG = "static/reset.png"
RAIN_IMG = "static/rain.png"
FLAME_IMG = "static/flame.png"
SETTINGS_IMG = "static/settings.png"
rain_musicbutton = 'stopped'
flame_musicbutton = 'stopped'
VOLUME_DOWN_IMG = "static/volume-down.png"
VOLUME_UP_IMG = "static/volume-up.png"
idk=0
hard_mode = False
settings_window=False
volume = 0.5
#def's
def btn_timechange():#change the time
    global minutes, seconds, hard_mode
    if minutes == 25:
        minutes = 50
        hard_mode = True
    elif minutes == 50:
        minutes = 25
        seconds = 0
        hard_mode = False
    canvas.itemconfig(main_text, text=f"{minutes:02d}:{seconds:02d}")
class CanvasButton:
    """Class to create a button on a Tkinter canvas."""
    def __init__(self, canvas, x, y, image_path, command):
        """
        Initialize the CanvasButton.
        
        Parameters:
        canvas (tk.Canvas): The canvas to place the button on.
        x (int): The x-coordinate of the button.
        y (int): The y-coordinate of the button.
        image_path (str): The file path to the button image.
        command (function): The function to call when the button is clicked.
        """
        x, y = canvas.canvasx(x), canvas.canvasy(y)  # Convert window to canvas coords.
        self.btn_image = tk.PhotoImage(file=image_path)
        self.canvas_btn_img_obj = canvas.create_image(x, y, anchor='nw', image=self.btn_image)
        canvas.tag_bind(self.canvas_btn_img_obj, "<Button-1>", lambda event: command())

    def update_image(self, new_image_path):
        """Update the button image."""
        self.btn_image = tk.PhotoImage(file=new_image_path)
        canvas.itemconfig(self.canvas_btn_img_obj, image=self.btn_image)
def button_change_theme():#change the background
    global background_index
    background_index += 1
    if background_index >= len(BACKGORUNDS):
        background_index = 0
    canvas_background.update_image(BACKGORUNDS[background_index])
    canvas_backroud_button.update_image(PLAY_IMG)
def btn_theme():#change the background
    global idk
    idk=0
    ##NEED TO BE HERE TO BACKGROUNDS WORK
def btn_rain():#play rain music
    """Load and play the background music."""
    global rain_musicbutton
    if rain_musicbutton=='running':
        rain_music.stop()
        rain_musicbutton='stopped'
    elif rain_musicbutton=='stopped':
        rain_music.play()
        rain_musicbutton='running'
def btn_flame():#play flame music
    """Load and play the background music."""
    
    global flame_musicbutton
    if flame_musicbutton=='running':
        flame_music.stop()
        flame_musicbutton='stopped'
    elif flame_musicbutton=='stopped':
        flame_music.play()
        flame_musicbutton='running'   
def play():#play the music
    """Load and play the background music."""
    pygame.mixer.music.load('static/lofi.mp3')
    pygame.mixer.music.play(-1)
def btn_pause():#pause the music and timer
    """Pause or resume the countdown timer."""
    global pause
    if music == 'running':
        if pause == False:
            pause = True
            canvas.itemconfig(upper_text, text='chilling')
            pygame.mixer.music.pause()
        elif pause == True:
            pause = False
            count_timer()
            canvas.itemconfig(main_text, text=f"{minutes:02d}:{seconds:02d}")
            pygame.mixer.music.unpause()
def btn_play():########TIMER SPAGETTI CODE#########
    """Start or reset the countdown timer."""
    global minutes, seconds, pause, music, timer_id
    if music == 'running':
        # Reset the timer
        print("Button play")
        if timer_id:
            root.after_cancel(timer_id)
        minutes = 25
        seconds = 0
        pause = False
        music = ''
        canvas.itemconfig(main_text, text=f"{minutes:02d}:{seconds:02d}")
        canvas.itemconfig(upper_text, text='chilling')
        pygame.mixer.music.stop()
        canvas_play.update_image(PLAY_IMG)
    elif music == '':
        # Start the timer
        music = 'running'
        count_timer()
        play()
        canvas_play.update_image(RESET_IMG)      
def count_timer():#I HATE THIS FUNCTION(its a timer)
    """Update the countdown timer every second."""
    global minutes, seconds, pause, music, timer_id,break_count
    if pause == False:
        if seconds == 0:
            if minutes > 0:
                minutes -= 1
                seconds = 59
            else:
                if break_count == True:#25 minutes back to work
                    #25 minutes break
                    minutes = 25
                    seconds = 0
                    break_count = False
                    canvas.itemconfig(upper_text, text='productive')
                elif break_count == False:
                #5 minutes break
                    if hard_mode == False:
                        minutes = 5
                    elif hard_mode == True:
                        minutes = 10
                    seconds = 0
                    break_count = True
                    canvas.itemconfig(upper_text, text='chilling_break')
                pygame.mixer.music.stop()
        else:
            seconds -= 1
        timer_id = root.after(1000, count_timer)
        canvas.itemconfig(upper_text, text='productive')
        canvas.itemconfig(main_text, text=f"{minutes:02d}:{seconds:02d}")
def show_setings():
    global settings_window
    if settings_window==False:
        canvas_setttings.place(x=0, y=0)
        print('settings')
        settings_window=True
    elif settings_window==True:
        canvas_setttings.place_forget()
        settings_window=False
def volume_up():
    global volume
    volume += 0.1
    pygame.mixer.music.set_volume(volume)
    flame_music.set_volume(volume)
    rain_music.set_volume(volume)
def volume_down():
    global volume
    volume -= 0.1
    pygame.mixer.music.set_volume(volume)
    flame_music.set_volume(volume)
    rain_music.set_volume(volume)
# Initialize the main application 

pygame.mixer.init()
pygame.mixer.music.set_volume(volume)
rain_music= pygame.mixer.Sound('static/rain.mp3')
flame_music= pygame.mixer.Sound('static/flame.mp3')
root = tk.Tk()
root.geometry("400x600")
root.resizable(False, False)
root.title("Pomodoro")
root.configure(bg="#ffffff")
# Create a canvas for the application
canvas = tk.Canvas(root, bg="#ffffff", height=1024, width=1440, bd=0,
                   highlightthickness=0, relief="ridge")#create the canvas
canvas.place(x=0, y=0)#place the canvas
canvas_setttings=tk.Canvas(root, bg="#ffffff", height=1024, width=1440, 
                           bd=0,highlightthickness=0,relief='ridge')#create the settings canvas
settings_bg = CanvasButton(canvas_setttings, 0, 0, BACKGORUNDS[4], btn_theme)
volume_settings_text = canvas_setttings.create_text(100, 50, text='Main_volume', font=('Helvetica', 14), fill="black")#create the settings text
settings_text = canvas_setttings.create_text(190, 20, text='settings', font=('Helvetica', 14), fill="black")#create the settings text
btn_volume_up = CanvasButton(canvas_setttings, 170, 35, VOLUME_UP_IMG, volume_up)#create the volume up button
btn_volume_down = CanvasButton(canvas_setttings, 215, 35, VOLUME_DOWN_IMG, volume_down)#create the volume down button
#################i just use button logic for background here################
canvas_background = CanvasButton(canvas, 0, 0, BACKGORUNDS[background_index], btn_theme)
canvas_backroud_button = CanvasButton(canvas, 360, 200, PLAY_IMG, button_change_theme)
########################################################################
# Create the timer text
main_text = canvas.create_text(190, 100, text=f"{minutes:02d}:{seconds:02d}", font=('Helvetica', 48), fill="black")
upper_text = canvas.create_text(190, 50, text='chilling', font=('Helvetica', 14), fill="black")
# Create buttons, bind them to the canvas, and set their commands
canvas_rain = CanvasButton(canvas, 360, 30, RAIN_IMG, btn_rain)
canvas_pause = CanvasButton(canvas, 150, 128, PAUSE_IMG, btn_pause)
canvas_play = CanvasButton(canvas, 200, 128, PLAY_IMG, btn_play)
canvas_flame = CanvasButton(canvas, 360, 65, FLAME_IMG, btn_flame)
canvas_timechange = CanvasButton(canvas, 360, 250, RESET_IMG, btn_timechange)
canvas_settings = CanvasButton(canvas, 360, 300, SETTINGS_IMG, show_setings)
canvas_back = CanvasButton(canvas_setttings, 360, 300, SETTINGS_IMG, show_setings)
# Start the main loop
root.mainloop()
print('end')