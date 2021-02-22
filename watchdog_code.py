import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from test import read_file
from test import append_file
from test import erase_file

string = ""
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # print("Modified")
        # erase_file()
        string = read_file()
        if string == '':
            pass
        else:
            print("Modified")
            print string
        erase_file()


if __name__ == "__main__":
    erase_file()
    print("Watching Test Directory !")
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='test', recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(5)
            # erase_file()
            # append_file()
    except KeyboardInterrupt:
        observer.stop()
        erase_file()
    observer.join()