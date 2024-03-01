import secrets
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def main():
    root = tk.Tk()
    root.minsize(width=400, height=300)
    root.title('PassMan')
    root.config(pady=30, padx=30)

    logo_img = tk.PhotoImage(file='logo.png')
    canvas = tk.Canvas(root, width=200, height=200)
    canvas.grid(row=0, column=1, sticky='NEWS')
    canvas.create_image(100, 100, image=logo_img)

    website_lbl = tk.Label(root, text='Website:').grid(row=1, column=0, sticky='E')

    website_entry_var = tk.StringVar(root)
    website_entry = tk.Entry(root, textvariable=website_entry_var, width=50)
    website_entry.grid(row=1, column=1, columnspan=2, sticky='W')
    website_entry.focus()

    # -------------------------- User Name ----------------------------- #
    username_lbl = tk.Label(root, text='E-mail/Username:').grid(row=2, column=0, sticky='E')
    # ------- User Entry -------- #
    username_var = tk.StringVar(root)
    username_entry = tk.Entry(root, textvariable=username_var, width=50)
    username_entry.grid(row=2, column=1, columnspan=2, sticky='W')
    username_entry.insert(0, 'zasrus@gmail.com')
    # ---------------------------- Password -------------------------------- #
    pass_lbl = tk.Label(root, text='Password:').grid(row=3, column=0, sticky='E')

    pass_entry_var = tk.StringVar(root)
    pass_entry = tk.Entry(root, textvariable=pass_entry_var, width=33)
    pass_entry.grid(row=3, column=1, sticky='W')

    # ------------------ Buttons --------------------------- #
    passwrd_gen_btn = tk.Button(root, text='Generate Password', command=lambda: generate_passwrd(pass_entry))
    passwrd_gen_btn.grid(row=3, column=2, columnspan=2, sticky="W")
    add_btn = tk.Button(root, text='ADD', width=10,
                        command=lambda: confirm(website_entry_var.get(), username_var.get(), pass_entry_var.get(),
                                                website_entry, pass_entry))
    add_btn.grid(row=4, column=1)
    root.mainloop()


def confirm(website, username, password, web_txt, pass_txt):
    if website == '' or username == '' or len(password) == 0:
        messagebox.showinfo(title='PassMan', message='All field are required.')
        return
    gui_confirm = tk.Tk()
    gui_confirm.geometry('300x150')
    gui_confirm.title('Confirm Info')

    lbl_website = tk.Label(gui_confirm, text='Website: ').grid(row=0, column=0)
    lbl_website_txt = tk.Label(gui_confirm, text=website).grid(row=0, column=1)
    lbl_user = tk.Label(gui_confirm, text='username: ').grid(row=1, column=0)
    lbl_user_txt = tk.Label(gui_confirm, text=username).grid(row=1, column=1)
    lbl_pass = tk.Label(gui_confirm, text='password: ').grid(row=2, column=0)
    lbl_pass_txt = tk.Label(gui_confirm, text=password).grid(row=2, column=1)
    lbl_question = tk.Label(gui_confirm, text='Is this correct?').grid(row=3, column=2)

    btn_no = tk.Button(gui_confirm, text='No', command=gui_confirm.destroy)
    btn_no.grid(row=4, column=1)

    # Creating a button with more than one command using lambda
    # button = Button(master, text="Button", command=lambda: [fun1(), fun2()])
    btn_yes = tk.Button(gui_confirm, text='Yes',
                        command=lambda: [
                            add(website, username, password, gui_confirm),
                            web_txt.delete(0, 'end'), pass_txt.delete(0, 'end')])
    btn_yes.grid(row=4, column=2)


def generate_passwrd(pass_box):
    string_text = string.ascii_letters + string.digits + string.punctuation
    passwrd = ''.join(secrets.choice(string_text) for i in range(10))
    pass_box.insert(0, passwrd)
    pyperclip.copy(passwrd)
    messagebox.showinfo(title="PassMan", message="password copied to clipboard")

def add(web, user, passwrd, gui):
    """
    :param web:
    :param user:
    :param passwrd:
    :param gui: name of tkinter window to be closed
    """
    with open('pass.txt', 'a') as file:
        file.writelines(f'{web}, {user}, {passwrd}\n')

    gui.destroy()


if __name__ == '__main__':
    main()
