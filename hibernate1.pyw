
import PySimpleGUI as sg
import time
import datetime
import subprocess



class hibernate_class():
    '''
    goofy ahh hibernate thingy
    '''
    # hibernate cmd
    def hibernate():
        subprocess.Popen(['shutdown/h'],shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)

    # create new time
    def create_time():
        return datetime.datetime.now() + datetime.timedelta(minutes=2)

    # Create the window
    def create_main_win():
        layout = [[sg.Text("Do you want to hibernate?", size=(30,2), font=("consolas 14"))],
            [sg.Button('Yes', size=(10,3)),sg.Button('No', size=(10,3))],
                [sg.Button("Rescedule")],
                [sg.Text('', auto_size_text=True, font=('Helvetica', 10),
                    key='close')]]
        window = sg.Window('Window Title', layout, size= (350,200), location=(10,10), no_titlebar=True, keep_on_top=True)
        return window

    # init the window
    window = create_main_win()

    # open the sub-window for timer
    def open_window():
        window1 = sg.Window(title="sus",layout=[[sg.Text('Pls input ur time(in mins)', font='Poppins')],
                [sg.Input(key="in")],
                [sg.Text('', visible=False, font=("Arial 7 bold"), text_color="Red", key="-ERROR-" )],
                [sg.OK(), sg.Cancel()]], modal=True, no_titlebar=True)
        while True:
            event, values = window1.read()
            if event == "OK":
                # check for empty or str in time
                if values['in'] == '':
                    window1["-ERROR-"].update('Pls insert note',visible=True)  
                elif values['in'][-1] not in ('0123456789.-'):
                    window1["-ERROR-"].update('Pls number only',visible=True) 
                else:
                    window1.close()
                    return values['in']       
            else:
                window1.close()
                return None           

    # calculate the time end for the thing
    time_end = create_time()

        
    # Display and interact with the Window using an Event Loop
    while True:
        # timer events
        event, values = window.read(timeout=10)
        mins = time_end-datetime.datetime.now()
        td = str(mins).split('.')[0]
        h,m,s = td.split(':')
        window['close'].update(f'closing in {m}:{s} mins')

        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        elif event == "Yes":
            hibernate()
            break
        elif event == "No":
            break
        elif event == "Rescedule":
            # try to add float
            try:    
                sleep = float(open_window())
            except:
                sleep = None
                pass

            # check if empty str
            if sleep == None or sleep == '': 
                pass
            else:
                window.close()
                # prevent the window from counting sown to 0
                time_end = datetime.timedelta(weeks=999)
                try:
                    time.sleep((sleep*60)-120)
                    time_end = create_time()
                except ValueError:
                    time.sleep((sleep*60))
                    time_end = create_time()
                window = create_main_win()
                pass


        elif m=='00' and s == '00':
            window.close()
            hibernate()
            
        # Output a message to the window
        

    # Finish up by removing from the screen
    window.close()






a = hibernate_class()