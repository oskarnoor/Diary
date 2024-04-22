import customtkinter


def done():
    print(today.get())


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.geometry("550x380")


today_frame = customtkinter.CTkFrame(master=root)
today_frame.pack(pady=10,padx=10,fill="both",expand=True)


today = customtkinter.CTkEntry(master=today_frame,placeholder_text = "Tell me about your day")
today.pack(pady=12, padx=10)

doneButton = customtkinter.CTkButton(master=today_frame,text="Done",command=done)
doneButton.pack(pady=12,padx=10)
root.mainloop()


