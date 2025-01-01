import tkinter as tk
from queue import Queue
from threading import Thread
import time

class EventManager:
    def __init__(self):
        self._observers = []
        self._filter = None

    def subscribe(self, observer):
        """Add an observer to the list"""
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer):
        #remove an obsever from the list
        if observer in self._observers:
            self._observers.remove(observer)
    
    def set_filter(self, filter_func):
        #set a filter to filter events
        self._filter = filter_func

    def notify(self,event):
        #notify rge observers about the event 
        if self._filter and not self._filter(event):
            return #skip that event that dont pass the filter 
        for observer in sorted(self._observers, key=lambda obs:getattr(obs, "priority",0), reverse= True):
            observer.update(event)


class Observer:
    def update(self,event):
        #Handle the event must be implemented by concrete observers 
        raise NotImplementError("Subclass must Implement'update' method.")



class Logger(Observer):
    def update(self, event):
        print(f"[Logger] Receieved event: {event}")

class EmailNotifier(Observer):
    def update(self, event):
        print(f"[EmailNotifier] Sending email for event: {event}")

class DataSaver(Observer):
    def update(self, event):
        print(f"[DataSaver] Saving event data: {event}")

class Event:
    def __init__(self, name, data, priority = 0):
        self.name = name
        self.data = data
        self.priority = priority

    def __str__(self):
        return f"Event(name={self.name}, data={self.data}, priority={self.priority})"


class EventVisualizer(tk.Tk):
    def __init__(self, event_manager):
        super().__init__()
        self.event_manager = event_manager
        self.event_queue = Queue()
        self.title("Event Visualizer")
        self. geometry("500x400")

        #gui componenets

        self.text_display =tk.Text(self, state = "disabled", wrap = "word")
        self.text_display.pack(expand=True, fill ="both")

        self.filter_entry = tk.Entry(self)
        self.filter_entry.pack(fill = "x")
        self.filter_button = tk.Button(self, text="Set Filter", command = self.set_filter)
        self.filter_button.pack()

        #start the processing thread
        self.running = True 
        self.event_thread = Thread(target = self.process_events, daemon = True)
        self.event_thread.start()

    def set_filter(self):
        """Set an event filter based on the users input"""
        filter_text = self.filter_entry.get()
        if filter_text:
            self.event_manager.set_filter(lambda e: filter_text.lower() in e.name.lower())
        else:
            self.event_manager.set_filter(None)

    def process_events(self):
        #continiously process events from the queue
        while self.running:
            if not self.event_queue.empty():
                event = self.event_queue.get()
                self.display_event(event)


    def display_event(self, event):
        #display an event in the text area

        self.text_display.config(state ="normal")
        self.text_display.insert("end", f"{event}\n")
        self.text_display.config(state ="disabled")

    def add_event(self, event):
        #add an event to the queue for the display
        self.event_queue.put(event)

    def on_close(self):
        """stop the event loop and the close the appplication"""
        self.running = False
        self.destroy()




"""COMBINING ALL OBJECTS AND TRIGGER POINTS"""
def main():
    #Create the event manager

    event_manager = EventManager()
    app = EventVisualizer(event_manager)

    class GUIObserver:
        def __init__(self, app, priority=0):
            self.app = app 
            self.priority = priority

        def update(self, event):
            self.app.add_event(event)

    #attach GUI AS an observer
    gui_observer = GUIObserver(app)
    event_manager.subscribe(gui_observer)

    #simulate event generation
    def generate_events():
        events = [
            Event("UserLogin", {"username": "johndoe"}, priority=1),
            Event("FileUploaded", {"filename": "report.pdf"}, priority=2),
            Event("ErrorOccurred", {"error_code": 500}, priority=3),
            Event("UserLogout", {"username": "janedoe"}, priority=1),
        ]

        for event in events:
            event_manager.notify(event)
            time.sleep(2)

    event_thread = Thread(target = generate_events, daemon = True)
    event_thread.start()

    app.protocol("WM_DELETE_WINDOW", app.on_close)
    app.mainloop()


    # #create observers 

    # logger = Logger()
    # email_notifier = EmailNotifier()
    # data_saver = DataSaver()

    # #Subscribe observers

    # event_manager.subscribe(logger)
    # event_manager.subscribe(email_notifier)
    # event_manager.subscribe(data_saver)

    # #Trigger Events
    # event1 = Event("UserLogin",{"username": "john", "time": "2025-01-01 12:00"})
    # event_manager.notify(event1)

    # event2 = Event("FileUploaded", {"filename": "report.pdf", "size": "2MB"})
    # event_manager.notify(event2)

    # #unsubscribe an observer
    # event_manager.unsubscribe(email_notifier)

    # event3 = Event("ErrorOccurred", {"error_code": 500, "meesage": "server error"})
    # event_manager.notify(event3)


if __name__ == "__main__":
    main()