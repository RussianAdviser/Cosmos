import tkinter as tk
import pygame
from tkinter import Tk, Label, PhotoImage

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title('Crusader Queens I')

        # Загрузка изображения
        self.background_image = PhotoImage(file="pictures/background.png")
        self.background2_image = PhotoImage(file="pictures/background2.png")
        self.background3_image = PhotoImage(file="pictures/background3.png")  # Добавлено
        self.button_image = PhotoImage(file="pictures/texture.png")
        self.button2_image = PhotoImage(file="pictures/texture2.png")  # Добавлено
        self.background4_image = PhotoImage(file="pictures/background4.png")
        self.background5_image = PhotoImage(file="pictures/background5.png")

        # Создание стартового экрана
        self.start_screen()
        self.game_modes_frame = tk.Frame(self.root)  # Добавлено
        self.choose_frame = tk.Frame(self.root)  # Добавлено

        # Задайте размер окна и сделайте его неизменяемым
        self.root.geometry('1000x700')  # Задайте размер окна здесь
        self.root.resizable(False, False)

        pygame.mixer.init()
        pygame.mixer.music.load('music/Main Theme.mp3')  # Укажите путь к вашему музыкальному файлу здесь
        pygame.mixer.music.set_volume(0.5)  # Установите громкость здесь
        pygame.mixer.music.play(-1)

        self.unit_types = ['Легкая пехота', 'Тяжелая пехота', 'Пикинеры', 'Лучники', 'Легкая кавалерия', 'Тяжелая кавалерия']

    def start_screen(self):
        self.start_frame = tk.Frame(self.root)
        self.start_frame.grid(row=0, column=0, sticky='nsew')  # Изменено

        # Установка фона
        background_label = Label(self.start_frame, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Создание кнопок с текстурой и расположение их по центру
        tk.Button(self.start_frame, text='Начать игру', image=self.button_image, compound='center', command=self.game_modes, font=('Times New Roman', 14), fg='white').pack(pady=20)
        tk.Button(self.start_frame, text='Настройки', image=self.button_image, compound='center', command=self.settings, font=('Times New Roman', 14), fg='white').pack(pady=20)
        tk.Button(self.start_frame, text='Выход', image=self.button_image, compound='center', command=self.root.quit, font=('Times New Roman', 14), fg='white').pack(pady=20)

    def game_modes(self):
        

        self.game_modes_frame.grid(row=0, column=0, sticky='nsew')  # Изменено

        # Установка фона
        background_label = Label(self.game_modes_frame, image=self.background5_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Создание кнопок с текстурой и расположение их по центру
        tk.Button(self.game_modes_frame, text='Одиночная игра', image=self.button2_image, compound='center', state='disabled', font=('Times New Roman', 14), fg='white').pack(pady=20)
        tk.Button(self.game_modes_frame, text='Мультиплеер', image=self.button2_image, compound='center', command=self.choose_sides, font=('Times New Roman', 14), fg='white').pack(pady=20)

    #Создание настроек
    def settings(self):
        self.start_frame.pack_forget()

        self.settings_frame = tk.Frame(self.root)
        self.settings_frame.pack(fill="both", expand=True)

        # Установка фона
        background_label = Label(self.settings_frame, image=self.background4_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Создание контейнера для центрирования элементов
        settings_container = tk.Frame(self.settings_frame)
        settings_container.place(relx=0.5, rely=0.5, anchor='center')

        # Установка фона для settings_container
        background_label2 = Label(settings_container, image=self.background4_image)
        background_label2.place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(settings_container, text='Настройки').pack()
        tk.Label(settings_container, text='Громкость музыки').pack()
        self.volume_scale = tk.Scale(settings_container, from_=0, to=100, orient='horizontal', command=self.update_volume)
        self.volume_scale.set(int(pygame.mixer.music.get_volume() * 100))  # Установите начальное значение здесь
        self.volume_scale.pack()

        self.mute_button = tk.Checkbutton(settings_container, text='Отключить звук', command=self.toggle_mute)
        self.mute_button.pack()

            # Расположение кнопки "Назад" ниже
        tk.Button(settings_container, text='Назад', image=self.button2_image, compound='center', command=self.back_to_start_from_settings, font=('Times New Roman', 14), fg='white').pack(pady=50)

    def update_volume(self, volume):
        pygame.mixer.music.set_volume(int(volume) / 100)

    def toggle_mute(self):
        if pygame.mixer.music.get_volume() > 0:
            pygame.mixer.music.set_volume(0)
        else:
            pygame.mixer.music.set_volume(self.volume_scale.get() / 100)

    def back_to_start_from_settings(self):
        self.settings_frame.pack_forget()
        self.start_screen()

    
   
   
    def choose_sides(self):
        
        self.game_modes_frame.grid_remove()  # Изменено
        self.choose_frame.grid(row=0, column=0, sticky='nsew')  # Изменен

        # Установка фона
        background2_label = Label(self.choose_frame, image=self.background2_image)
        background2_label.place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(self.choose_frame, text='Выберите стороны конфликта:', image=self.button2_image, compound='center', fg='white', font=('Times New Roman', 12)).place(relx=0.5, rely=0.3, anchor='center')  # Изменено

        self.countries = ['Французкое королевство', 'Королевство Англия', 'Королевство Испания', 'Королевство Португалия']
        self.player1_country = tk.StringVar(self.root)
        self.player1_country.set(self.countries[0]) # default value
        self.player2_country = tk.StringVar(self.root)
        self.player2_country.set(self.countries[1]) # default value

        tk.OptionMenu(self.choose_frame, self.player1_country, *self.countries).place(relx=0.3, rely=0.4, anchor='center')
        tk.OptionMenu(self.choose_frame, self.player2_country, *self.countries).place(relx=0.7, rely=0.4, anchor='center')

        # Установите изображение текстуры кнопки
        tk.Button(self.choose_frame, text='Далее', command=self.enter_numbers, image=self.button_image, compound="center", fg='white', font=('Times New Roman', 12)).place(relx=0.5, rely=0.5, anchor='center')  # Изменено
        tk.Button(self.choose_frame, text='Назад', command=self.back_to_start, image=self.button_image, compound="center", fg='white', font=('Times New Roman', 12)).place(relx=0.5, rely=0.6, anchor='center')  # Изменено


    def enter_numbers(self):
        self.choose_frame.pack_forget()

        self.enter_frame = tk.Frame(self.root)
        self.enter_frame.pack(fill="both", expand=True)  # Изменено

        # Установка фона
        background_label = Label(self.enter_frame, image=self.background3_image)  # Изменено
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Центрирование виджетов
        widget_frame = tk.Frame(self.enter_frame)
        widget_frame.place(relx=0.5, rely=0.5, anchor='center')  # Изменено

        tk.Label(widget_frame, text='Введите численность войск:').pack()

        self.player1_entries = self.create_entries(widget_frame, self.player1_country.get())
        self.player2_entries = self.create_entries(widget_frame, self.player2_country.get())

        self.battle_button = tk.Button(widget_frame, text='В бой!', image=self.button2_image, compound='center', command=self.battle_screen, state='disabled', font=('Times New Roman', 12), fg='white')  # Изменено
        self.battle_button.pack(side='bottom')

        self.battle_locations = ['Гастингс', 'Иерусалим', 'Дорога на Рим', 'Окситания', 'За валом Адриана']
        self.battle_location = tk.StringVar(self.root)
        self.battle_location.set(self.battle_locations[0]) # default value
        tk.Label(widget_frame, text='Место битвы:').pack()
        tk.OptionMenu(widget_frame, self.battle_location, *self.battle_locations).pack(pady=10)  # Изменено

        self.seasons = ['Лето', 'Осень', 'Зима','Весна']
        self.season = tk.StringVar(self.root)
        self.season.set(self.seasons[0]) # default value
        self.season.trace('w', self.update_weather_conditions)
        tk.Label(widget_frame, text='Сезон:').pack()
        tk.OptionMenu(widget_frame, self.season, *self.seasons).pack(pady=10)  # Изменено

        self.weather_conditions = ['Ясно', 'Туман', 'Дождь', 'Гроза', 'Снег', 'Метель']
        self.weather_condition = tk.StringVar(self.root)
        self.weather_condition.set(self.weather_conditions[0]) # default value
        self.weather_option_menu = tk.OptionMenu(widget_frame, self.weather_condition, *self.weather_conditions)
        self.weather_option_menu.pack(pady=10)  # Изменено

        tk.Button(widget_frame, text='Назад', image=self.button2_image, compound='center', command=self.back_to_choose, font=('Times New Roman', 12), fg='white').pack(side='bottom')  # Изменено
    
    def update_weather_conditions(self, *args):

        season = self.season.get()
        if season == 'Зима':
            self.weather_conditions = ['Снег', 'Метель', 'Ясно']
        else:
            self.weather_conditions = ['Ясно', 'Туман', 'Дождь', 'Гроза']

        self.weather_condition.set(self.weather_conditions[0]) # default value

        # update the option menu choices
        menu = self.weather_option_menu['menu']
        menu.delete(0, 'end')
        for condition in self.weather_conditions:
            menu.add_command(label=condition, command=tk._setit(self.weather_condition, condition))

    def create_entries(self, frame, country):
        unit_frame = tk.Frame(frame)
        unit_frame.pack(side='left')

        tk.Label(unit_frame, text=country).pack()

        entries = []
        for unit_type in self.unit_types:
            tk.Label(unit_frame, text=unit_type).pack()
            entry = tk.Entry(unit_frame)
            entry.bind('<KeyRelease>', lambda event: self.check_battle_button_state())
            entry.pack()
            entries.append(entry)

        return entries

    def battle_screen(self):
        if self.check_entries(self.player1_entries) and self.check_entries(self.player2_entries):
            self.enter_frame.pack_forget()

            self.battle_frame = tk.Frame(self.root)
            self.battle_frame.pack()

            tk.Label(self.battle_frame, text='Битва началась!').pack()

            # Импортируйте Battle здесь
            from battle import Battle
            self.battle = Battle(self)  # Создайте экземпляр класса Battle
        else:
            tk.messagebox.showerror("Ошибка", "У каждой стороны должен быть хотя бы один боец!")

    def check_entries(self, entries):
        for entry in entries:
            if entry.get().isdigit() and int(entry.get()) > 0:
                return True
        return False

    def check_battle_button_state(self):
        if self.check_entries(self.player1_entries) and self.check_entries(self.player2_entries):
            self.battle_button['state'] = 'normal'
        else:
            self.battle_button['state'] = 'disabled'

    def back_to_start(self):
        self.choose_frame.pack_forget()
        self.start_screen()

    def back_to_choose(self):
        self.enter_frame.pack_forget()
        self.choose_sides()

root = tk.Tk()
game = Game(root)
root.mainloop()
