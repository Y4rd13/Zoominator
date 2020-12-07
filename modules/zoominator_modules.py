import subprocess
import os
import time
import datetime
from collections import defaultdict
from tqdm import tqdm
import os

alert = ['No mover el mouse, ni teclear cuando termine la barra de progreso.',
         ' De lo contrario, el programa no funcionará correctamente.',
         '¿Continuar con los procesos?\nEsto no afectará a la clase actual']


try:
    os.system('color a')
    os.system('py -m pip install --upgrade pip')
    os.system('py -m pip install -r requirements.txt')
#    os.system('py -m pip install tqdm')
#    os.system('py -m pip install pyautogui')
#    os.system('py -m pip install psutil')
except ImportError:
    print('\n> Error, Module ModuleName is required')
    raise IOError('\nCannot find: path or modules')
finally:
    import pandas as pd
    import pyautogui as gui
    import psutil


def display_logo(x):
    if x == 0:
        print('''
    ███████╗ ██████╗  ██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ████████╗ ██████╗ ██████╗ 
    ╚══███╔╝██╔═══██╗██╔═══██╗████╗ ████║██║████╗  ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
      ███╔╝ ██║   ██║██║   ██║██╔████╔██║██║██╔██╗ ██║███████║   ██║   ██║   ██║██████╔╝
     ███╔╝  ██║   ██║██║   ██║██║╚██╔╝██║██║██║╚██╗██║██╔══██║   ██║   ██║   ██║██╔══██╗
    ███████╗╚██████╔╝╚██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██║  ██║   ██║   ╚██████╔╝██║  ██║
    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝                                                                                  
    -------------------------------------------------------------------------------------
    ''')
    elif x == 1:
        print('''
     █████╗ ██╗   ██╗████████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗██╗ ██████╗
    ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝██║██╔════╝
    ███████║██║   ██║   ██║   ██║   ██║██╔████╔██║███████║   ██║   ██║██║     
    ██╔══██║██║   ██║   ██║   ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██║██║     
    ██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║ ╚═╝ ██║██║  ██║   ██║   ██║╚██████╗
    ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝
    ------------------------------------------------------------------------------
    ''')
    elif x == 2:
        print('''
    ███╗   ███╗ █████╗ ███╗   ██╗██╗   ██╗ █████╗ ██╗     
    ████╗ ████║██╔══██╗████╗  ██║██║   ██║██╔══██╗██║     
    ██╔████╔██║███████║██╔██╗ ██║██║   ██║███████║██║     
    ██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██╔══██║██║     
    ██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝██║  ██║███████╗
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
    ----------------------------------------------------------                                                  
    ''')


def loading_bar(r2, r1=0, s=1, text='\nWaiting for process...'):
    print(text)
    for __ in tqdm(range(r1, r2)):
        time.sleep(s)


class handle_process:
    def __init__(self, PROCNAME):
        self.PROCNAME = PROCNAME

    def kill(self):
        print(f'\nKill process: {self.PROCNAME}')
        for proc in psutil.process_iter():
            try:
                if proc.name().lower() == self.PROCNAME.lower():
                    proc.kill()
                    print('Killed: ', True)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                print('Killed: ', False)
                os.system("taskkill /f /im Zoom.exe")
        loading_bar(r2=100, s=0.01, text=f'Killing process... {self.PROCNAME}')

    def check(self):
        boolean_check_process = []
        for proc in psutil.process_iter():
            try:
                if proc.name().lower() == self.PROCNAME.lower():
                    boolean_check_process.append(True)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                boolean_check_process.append(False)
        return boolean_check_process


class P_SUTIL:
    def __init__(self, audio, video):
        self.audio = audio
        self.video = video

    def audio_video(self):
        if self.audio == 'y' and self.video == 'y':
            gui.press(['tab'], presses=2)
            gui.press(['tab'])
        elif self.audio == 'y' and self.video == 'n':
            gui.press(['tab'], presses=2)
            gui.press(['tab', 'enter'])
        elif self.audio == 'n' and self.video == 'y':
            gui.press(['tab'], presses=2)
            gui.press(['enter'])
            gui.press(['tab'])
        elif self.audio == 'n' and self.video == 'n':
            gui.press(['tab'], presses=2)  # sin audio
            gui.press(['enter'])  # sin audio
            gui.press(['tab', 'enter'])  # sin video

    def initialize(self, file, root, student_name, ID_class):
        posx, posy = gui.size()
        x, y = int(posx / 2), int(posy / 2)
        print(
            f'\nTamaño de la pantalla: {posx}, {posy}\nPunto medio: {x}, {y}')

        gui.hotkey('win', 'd')
        print(f'\nOpening executable: {file}...\n')
        os.startfile(root + file)

        checking, counted = False, 1
        while checking == False and counted != 6:
            print(
                'La barra de progreso de demorará más dependiendo de la velocidad de su computador.')
            loading_bar(
                r2=70 * 1, s=0.1, text=f'Trying to check process {file}, tries: {counted}, waiting: {(70 * counted * 0.1)} sec.')
            if True in handle_process(file).check():
                print(f'\nProcess checked as: {handle_process(file).check()}')
                time.sleep(1)
                gui.click(x=x, y=y, button='left')
                time.sleep(1)
                gui.press(['tab', 'enter'])
                time.sleep(1)
                gui.write(ID_class)
                gui.press(['tab'], presses=2)
                gui.hotkey('ctrl', 'a')
                gui.write(student_name)
                P_SUTIL(self.audio, self.video).audio_video()
                time.sleep(1)
                gui.press(['tab', 'enter'])
                checking = True
            else:
                print(f'{file} process is not running.')
                print(handle_process(file).check())
                counted += 1


class utils:
    def __init__(self):
        pass

    def get_sec(self, time_str, day_str):
        if len(time_str.split(':')) < 3:
            time_str = time_str + ':00'

        h, m, s = time_str.split(':')
        day_sec, d = 86000, int(day_str)

        if d == 0:
            dx = day_sec * 7
        else:
            dx = day_sec * d
        return dx - (day_sec - (int(h) * 3600 + int(m) * 60))

    def hours_left(self, class_sec, date_sec):
        hours_left = int((int(class_sec) / 3600) - (int(date_sec) / 3600))
        min_left = ((class_sec - int(class_sec)) * 60) - \
            ((date_sec - int(date_sec)) * 60)
        return f'{hours_left}:{min_left}'

    def dictionary_2_OrderedList(self, d):
        l = []
        for key, values in d.items():
            for value in values:
                l.append((key, value))

        l.sort(key=lambda x: x[1])
        return l

    def alert(self):
        global alert
        gui.alert(text=alert[0] + alert[1], button='Continuar')


class handle_CSV:
    def __init__(self, path, csv):
        self.path = path
        self.csv = csv

    def display_csv(self):
        path_csv = self.path + self.csv
        df = pd.read_csv(path_csv)
        return df

    def csv_2_dict(self):
        path_csv = self.path + self.csv

        df = pd.read_csv(path_csv, usecols=[0, 1, 2])
        dd = defaultdict(list)

        idx = [str(i) for i in df['id']]
        time_str = [str(i) for i in df['hora']]
        day_str = [str(i) for i in df['dia']]
        zipped = zip(idx, time_str, day_str)

        loading_bar(r2=100, s=0.015, text='\nCargando datos del csv: ')

        for idx, j, k in zipped:
            class_hour = utils().get_sec(j, k)
            dd[idx].append(class_hour)
        return dd


class check_CSV:
    def __init__(self):
        pass

    def check_exist_csv_file(self, CSV_SAVE_FILENAME):
        try:
            x = False
            if os.path.exists(CSV_SAVE_FILENAME):
                while x == False:
                    print('\n¿Desea modificar el nombre del archivo.csv? Y o N')
                    op_csv = input('> ').lower()

                    if op_csv == 'y':
                        csv_file = input('\nIngrese SuArchivo.csv: ')
                        with open(CSV_SAVE_FILENAME, 'w') as f:
                            f.write(csv_file)
                        print('\ncambiado exitosamente...')
                        x = True
                    elif op_csv == 'n':
                        x = True
                    else:
                        print('\nError en la opción ingresada.')
            else:
                while x == False:
                    csv_file = input(
                        '\nIngrese nombre del archivo.csv: ').strip()
                    if csv_file.endswith('.csv'):
                        with open(CSV_SAVE_FILENAME, 'w') as f:
                            f.write(csv_file)
                        x = True
                    else:
                        print('Debe ingresar formato .csv, ejemplo: archivo.csv')
        except:
            return False
        finally:
            with open(CSV_SAVE_FILENAME, 'r') as f:
                csv_name = f.readline()
            return csv_name

    def check_csv_content(self, CSV_FILENAME):
        df = (pd.read_csv(CSV_FILENAME))
        validar = '#BORRAR ESTA LINEA PARA VALIDAR ARCHIVO'
        if validar in df:
            print('validar')
            os.startfile(CSV_FILENAME)
            gui.alert(
                text=f'Por favor, hacer válido su {CSV_FILENAME} csv antes de continuar', button='Acepto')


'''
def find_path(csv_file, path):
  for root, dirs, files in os.walk(path):
    for file in files:
      if file == csv_file:
        return os.path.abspath(os.path.join(root, file))
'''
