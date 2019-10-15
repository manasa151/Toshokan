import sys
import os
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import time
import datetime
from watchdog.events import PatternMatchingEventHandler

file_to_watch = 'request_species.csv'
directory_to_watch = ''

if __name__ == '__main__':
    path = 'C:\\Users\\jmentore\\Downloads'
    patterns = '*'
    ignore_patterns = ''
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(
        patterns, ignore_patterns, ignore_directories, case_sensitive)


def on_created(event):
    file_created = time.ctime(os.path.getctime(event.src_path))
    when_script_started = time.ctime()

    print(f"hey, {event.src_path} has been created!")
    print("Created on: %s" % file_created)

    if file_created > when_script_started:
        os.remove(os.path.join(path, event.src_path))
    else:
        print('No file was deleted')


my_event_handler.on_created = on_created
go_recursively = False
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)
my_observer.start()

try:
    while True:
        time.sleep(120)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
