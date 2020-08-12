import os
import time
import datetime
import pandas as pd
from modules.zoominator_modules import display_logo, loading_bar, handle_process, P_SUTIL, utils, handle_CSV, check_CSV
#############################################################################

#############################################################################
# student name, audio, video, filename
loading_bar(r2=100, s=0.009, text='\nCleanning (ctrl+c to stop)...')
check = False
while check == False:
    os.system('cls')
    display_logo(0)
    name_input = input(
        '\n> Ingrese nombre y apellido: ').lower().strip().split(' ')

    if len(name_input) == 2:
        name, last_name = name_input[0].capitalize(
        ), name_input[1].capitalize()
        print(f'\nnombre: {name}, apellido: {last_name}')

        if name.isalpha() and last_name.isalpha():
            student_name = (name + ' ' + last_name)

            if len(student_name) <= 30:
                print('\n¿Entrar con audio?')
                audio = input('Y o N: ').lower()
                print('\n¿Entrar con video?')
                video = input('Y o N: ').lower()

                if audio == 'y' or audio == 'n':
                    if video == 'y' or video == 'n':
                        csv_file = check_CSV().check_exist_csv_file('root_csv.txt')
                        # check_CSV().check_csv_content('horario zoom.csv') # !
                        check = True

                    else:
                        print('Ingrese una opción válida')
                        time.sleep(2)
                else:
                    print('Ingrese una opción válida')
                    time.sleep(2)
            else:
                print('\nEl largo es mayor a 30 carácteres')
                time.sleep(3)
        else:
            print('\nNombre ingresado no es alfabético')
            time.sleep(3)
    else:
        print(
            f'\nIngresar nombre y apellido (2 elementos)\nElementos detectados: {len(name_input)}')
        time.sleep(4)
#############################################################################

# initialize_variables
user = os.getlogin()
root = f'C:/Users/{user}/AppData/Roaming/Zoom/bin/'
file = 'Zoom.exe'

root_csv = str(os.path.dirname(os.path.abspath(__file__))
               ).replace(chr(92), '/') + '/'
utils().alert()

# create dict from csv
registro_clases = handle_CSV(root_csv, csv_file).csv_2_dict()

####################### L ## O ## O ## P ####################################
TL_registro_clases = utils().dictionary_2_OrderedList(registro_clases)
check, count, w, main_w = False, 0, 0, True
while main_w == True:
    while w == 0:
        os.system('cls')
        display_logo(0)
        print('\n\t1. Modo automático\n\t2. Entrar por id\n\t3. Para salir')
        try:
            menu_op = int(input('\n\t> '))
        except:
            print('\nError en el input.')

        if menu_op == 1:
            w = 1
        elif menu_op == 2:
            w = 2
        elif menu_op == 3:
            os.system('cls')
            main_w = False
            w = False
            break
        else:
            print('\nError en el input.')
            time.sleep(3)

    while w == 1:
        os.system('cls')
        display_logo(0)
        display_logo(1)
        print(handle_CSV(root_csv, csv_file).display_csv())

        for ID_class, class_hour in TL_registro_clases:
            # date variables
            date = datetime.datetime.now()
            current_day = date.strftime('%w')
            current_hour = date.strftime('%X')

            # date to seconds
            date_sec = utils().get_sec(current_hour, current_day)
            sunday_sec = utils().get_sec('23:59:59', 7)

            ###
            if (class_hour < date_sec) and count < 100:
                count += 1
                pass
            elif count == 100:  # (len(TL_registro_clases) * 3)
                print('Semana finalizada con éxito\n')
                print('Esperando para el comienzo de la siguiente semana: ')
                print(date_sec, sunday_sec)
                loading_bar(r1=date_sec, r2=sunday_sec, text='')
                time.sleep(1)
                count = 0
            else:
                # cycle
                print(f'\n' + '#' * 50)
                print(f'### Barra de progreso para la siguiente clase ###')
                print('#' * 50)
                print(date.strftime(f'Hora actual (de inicio): %X,\tFecha %x'))
                fiveMin_intoSecs = 300
                loading_bar(r1=date_sec, r2=(class_hour - fiveMin_intoSecs),
                            text=f'ID siguiente clase: {ID_class}')

                # kill & initialize
                handle_process(PROCNAME='Zoom.exe').kill()
                P_SUTIL(audio=audio, video=video).initialize(
                    file, root, student_name, ID_class)

                # reiniciando
                loading_bar(r2=30)
                print(f'\n# R # E # I # N # I # C # I # A # N # D  O #')
                print(pd.read_csv(root_csv + csv_file))
                loading_bar(r2=100, s=0.1,
                            text='Preparando siguiente clase...')

    while w == 2:
        os.system('cls')
        display_logo(0)
        display_logo(2)
        csv_display_1 = handle_CSV(path=root_csv, csv=csv_file).display_csv()
        len_csv = len(csv_display_1)
        print(csv_display_1)
        print('\nSeleccionar por índice la id a la que desea entrar (el primero es 0):')
        try:
            select_id = int(input('\t> '))
        except:
            print('Opción inválida.')

        id_count = 0
        for ID_class, class_hour in TL_registro_clases:
            if select_id <= (len_csv - 1):
                if id_count == select_id:
                    # kill & initialize
                    handle_process(PROCNAME='Zoom.exe').kill()
                    P_SUTIL(audio=audio, video=video).initialize(
                        file, root, student_name, ID_class)
                    w = False
            else:
                print('\nÍndice fuera de rango.')
                time.sleep(3)
            id_count += 1
