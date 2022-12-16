import tkinter
import customtkinter
from PIL import Image
import time
import create_graph_dist
import calculate_entropy
import Create_Dict_Snap as create

def open_alert_window(list_files):
    window = customtkinter.CTkToplevel()
    window.geometry("800x800")
    textbox = customtkinter.CTkTextbox(master=window, width=800, height=800, font=("Roboto", 40), text_color="red")
    textbox.grid(row=0, column=0)

    text_out = "Warning!\n\n Your Database Has Been Partly Encrypted\n\n"
    for line in list_files:
        text_out += line
        text_out += "\n"
    textbox.insert("0.0", text_out)  # insert at line 0 character 0
    text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

    textbox.configure(state="disabled")

def open_scan_window():
    window = customtkinter.CTkToplevel()
    window.geometry("400x400")

    # create label on CTkToplevel window
    label = customtkinter.CTkLabel(window, text="Anomaly index")
    label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

    graph_img = customtkinter.CTkImage(dark_image=Image.open("graph.jpg"),
                                  size=(380, 380))

    img = customtkinter.CTkButton(window, text='',image=graph_img)
    # img.pack(padx=0, pady=0)
    img.place(relx=0.5, rely=0, anchor=tkinter.N)
    
def quick_scan():
    print("Test_quick")
    progressbar= customtkinter.CTkProgressBar(master=app, fg_color="black", progress_color="purple",determinate_speed=1.4)
    progressbar.place(relx=0.48, rely=0.7, anchor=tkinter.N)
    progressbar.set(0)
    
    progressbar.start()
    create.main()
    list = []
    with open("Output1.txt") as out1:
        for line in out1:
            list.append(line)
    with open("Output2.txt") as out1:
        for line in out1:
            list.append(line)    
    with open("Output3.txt") as out1:
        for line in out1:
            list.append(line)    
    open_alert_window(list)
    app.after(3000, open_scan_window)
    


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green




app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("650x500")


bg_image = customtkinter.CTkImage(dark_image=Image.open("bg.jpeg"),
                                  size=(800, 330))
bg = customtkinter.CTkButton(app, border_width=0 ,corner_radius=0, state="disabled",text='',image=bg_image)
bg.place(relx=0, rely=0, anchor=tkinter.NW)


welcome_txt = customtkinter.CTkLabel(master=app, text="Welcome to CymerScan", font=("Roboto", 30))
welcome_txt.pack(pady=12, padx=10)
# welcome_txt.place(relx=0.5, rely=0.5, anchor=tkinter.N)

quick_button = customtkinter.CTkButton(master=app, height=50, width=140,text="Run Scan", command=quick_scan)
quick_button.place(relx=0.37, rely=0.5, anchor=tkinter.W)



app.mainloop()

