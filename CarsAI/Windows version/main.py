import tkinter as tk
from tkinter import filedialog
from tkinter import *
from ultralytics import YOLO
from PIL import Image, ImageTk
import os, getpass
import shutil
import cv2
from vidgear.gears import ScreenGear

user = getpass.getuser()


def back1():
    if os.path.exists("runs"):
        shutil.rmtree('runs')
    window.destroy()
    start()
def back2():
    window22.destroy()
    start()

def window1():
    window0.destroy()
    def close():
        if os.path.exists("runs"):
            shutil.rmtree('runs')
        window.destroy()
    global window
    window = Tk()
    x1 = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 6.4
    y1 = (window.winfo_screenheight() - window.winfo_reqheight()) / 10
    window.wm_geometry("+%d+%d" % (x1, y1))
    window.iconbitmap(default="icon\\1.ico")
    window.geometry('1000x700')
    window.protocol('WM_DELETE_WINDOW',close)
    window.resizable(0,0)
    window.title('Car Detecter AI')

    def pr():
        try:
            image_path = filedialog.askopenfilename(filetypes=[("Image files", " .jpg .png .webp .jepg")])
            if os.path.exists("runs"):
                shutil.rmtree('runs')
            filename = f"{image_path}"
            name = os.path.basename(filename)
            print(name)
            model = YOLO('AI\\best.pt')
            model(f"{image_path}", conf=0.8, save=True)
            one_image(name)
        except Exception as e:
            e=str(e)
            label['text']=f"Ошибка обработки изображения: {e[90:]}"
            print(e)


    def one_image(file):
        label['text']=''
        save_button['text']="Сохранить изображение"
        global file0
        file0=file
        global image_path
        try:
            image = Image.open(f'runs\\detect\\predict\\{file}')
            (width, height) = image.size
            print(width, height)
            if width>990 and height<1500 and width<1500 or height>990 and height<1500 and width<1500:
                width = round(width/2)
                height = round(height/2)
            if width>1500 and width<2000 and height<2000 or height>1500 and width<2000 and height<2000:
                width = round(width/2.5)
                height = round(height/2.5)
            if width>2000 or height>2000:
                width = round(width/3)
                height = round(height/3)
            print(width, height)
            image = image.resize((width, height))
            image = ImageTk.PhotoImage(image)
            label.config(image=image)
            label.image = image
        except Exception as e:
            label['text']=f"Ошибка загрузки изображения: {e}"
    def save():
        try:
            shutil.copy2(f'runs\\detect\\predict\\{file0}', f'C:\\Users\\{user}\\Pictures\\{file0}')
            save_button['text']=f'Изображение сохранено в Изображения(C:\\Users\\{user}\\Pictures\\{file0})'
        except:
            label['text']='Нет обработанного изображения'

    update_button = tk.Button(window, text="Загрузить изображение", command=pr)
    update_button.pack()
    save_button = tk.Button(window, text="Сохранить изображение", command=save)
    save_button.pack()
    back_button = Button(window,text="Назад", command=back1)
    back_button.pack()
    label = tk.Label(window,text='')
    label.pack()

    window.mainloop()

def window2():
    window0.destroy()
    global window22
    window22 = Tk()
    x2 = (window22.winfo_screenwidth() - window22.winfo_reqwidth()) / 6.4
    y2 = (window22.winfo_screenheight() - window22.winfo_reqheight()) / 10
    window22.wm_geometry("+%d+%d" % (x2, y2))
    window22.iconbitmap(default="icon\\1.ico")
    window22.geometry('1000x700')
    window22.resizable(0,0)
    window22.title('Car Detecter AI')

    def vidio():
        model = YOLO('AI/best.pt')
        video_path = filedialog.askopenfilename(filetypes=[("Image files", ".mp4 .mov .gif .avi")])

        cap = cv2.VideoCapture(video_path)

        while cap.isOpened():
            success, frame = cap.read()

            if success:
                results = model.track(frame,conf=0.5, persist=True)

                annotated_frame = results[0].plot()

                cv2.imshow("CarDetecter vidio", annotated_frame)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                 break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()

    def live():
        model = YOLO('AI/best.pt')
        video_path=0
        cap = cv2.VideoCapture(video_path)

        while cap.isOpened():
            success, frame = cap.read()

            if success:
                results = model.track(frame,conf=0.5, persist=True)

                annotated_frame = results[0].plot()

                cv2.imshow("CarDetecter vidio", annotated_frame)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                 break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()
    
    def screen():
        stream = ScreenGear().start()
        model = YOLO('./AI/best.pt')
        while True:
            frame = stream.read()
            results = model.track(frame,conf=0.5, persist=True)
            annotated_frame = results[0].plot()
            cv2.imshow("CarDetecter vidio", annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break


    lab = Label(window22, text="ВИМАНИЕ ДЛЯ ВЫХОДА ИЗ ВИДИО НАЖМИТЕ Q(НЕ Й А Q)", font='50', fg='red')
    lab.pack()
    but0 = Button(window22,text="Загрузить видио", font=("Arial", 14), command=vidio)
    but0.pack()
    but1 = Button(window22,text="Обработать видио с веб камеры", font=("Arial", 14), command=live)
    but1.pack()
    but2 = Button(window22,text="Обработать видио с экрана компьютера", font=("Arial", 14), command=screen)
    but2.pack()
    back_button = Button(window22,text="Назад", font=("Arial", 14), command=back2)
    back_button.pack()
    window22.mainloop()

def start():
    global window0
    window0 = Tk()
    x = (window0.winfo_screenwidth() - window0.winfo_reqwidth()) / 6.4
    y = (window0.winfo_screenheight() - window0.winfo_reqheight()) / 10
    window0.wm_geometry("+%d+%d" % (x, y))
    window0.iconbitmap(default="icon\\1.ico")
    window0.geometry('300x210')
    window0.resizable(0,0)
    window0.title('Выбор нужды')

    button_win1 = tk.Button(window0, text="Обработка изображений", command=window1)
    button_win1.pack()
    button_win2 = tk.Button(window0, text="Обработка видио", command=window2)
    button_win2.pack()

    window0.mainloop()
start()
# Version 1.2.3 windows