import threading
import tkinter as tk
import time
import winsound

seconds=0
milliseconds=0
    
def update_clock():
    global milliseconds
    global seconds
    current_time = time.time()
    milliseconds = int((current_time - int(current_time)) * 1000)
    current_time = time.localtime(current_time)
    hours, minutes, seconds = current_time.tm_hour, current_time.tm_min, current_time.tm_sec
    clock_display = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
    label.config(text=clock_display)
        
 
    # Schedule the function to run after 1 millisecond
    root.after(1, update_clock)
 

 
 
root = tk.Tk()
root.title("Millisecond Clock")
root.resizable(width=False, height=False)

label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='yellow')
label.pack(anchor='center')


def soundplay():
    
    if int(seconds) == 0 and int(milliseconds) < 300:
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
    
    root.after(1,soundplay )


if __name__ =="__main__":
    t1 = threading.Thread(target=update_clock)
    t2 = threading.Thread(target=soundplay)

    t1.start()
    t2.start()



                           
root.mainloop()

t1.join()
t2.join()


