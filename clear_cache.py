import sys
import os
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import time
import datetime
from watchdog.events import PatternMatchingEventHandler
#  “\AppData\Local\Google\Chrome\User Data\Default\Cache.”
file_to_watch = 'request_species.csv'

when_script_started = time.time()

if __name__ == '__main__':
    directory_to_watch = 'C:\\Users\\jmentore\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache'
    patterns = '*'
    ignore_patterns = ''
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(
        patterns, ignore_patterns, ignore_directories, case_sensitive)


def on_created(event):

    file_created = os.path.getctime(event.src_path)
    #formatted_time = time.time(file_created)

    print(f"hey, {event.src_path} has been created!")
    print(f"file created:{file_created} ago!")
    print(f"This Script started, {when_script_started} ago!")
    print(f'Elapse time: {when_script_started-file_created}')

    if (file_created > when_script_started):
        os.remove(os.path.join(directory_to_watch, event.src_path))
        print(f"Jelton, {event.src_path} has been deleted!")

    else:
        print('No file was deleted')


my_event_handler.on_created = on_created
go_recursively = False
my_observer = Observer()
my_observer.schedule(my_event_handler, directory_to_watch,
                     recursive=go_recursively)
my_observer.start()

try:
    while True:
        time.sleep(120)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
