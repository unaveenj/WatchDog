import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from test import read_file
from test import append_file
from test import erase_file

string = ""
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("Modified")
        string = read_file()
        print string


if __name__ == "__main__":
    erase_file()
    print("Watching Test Directory !")
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='test', recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
            append_file()
    except KeyboardInterrupt:
        observer.stop()
        erase_file()
    observer.join()