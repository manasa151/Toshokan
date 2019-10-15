
import platform
import sys
import os
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import time
from watchdog.events import PatternMatchingEventHandler

if __name__ == '__main__':
    path = '/home/pi/.cache/chromium/Default/Cache'
    patterns = '*'
    ignore_patterns = ''
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(
        patterns, ignore_patterns, ignore_directories, case_sensitive)


def on_created(event):
    print(f"hey, {event.src_path} has been created!")

    if get_size() > 550414728:
        folder_contents = os.listdir(path)

        for file in folder_contents:
            if file != 'index-dir':
                os.remove(os.path.join(path, file))

    # os.remove(event.src_path)


def on_deleted(event):

    print(f'what the f**k! Someone deleted {event.src_path} !')


def on_moved(event):

    print(f'ok ok ok, someone moved {event.src_path} to {event.dest_path}')


def on_modified(event):

    print(f'hey buddy, {event.src_path} has been modified')


def get_size(start_path=path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime


print(get_size(), 'bytes')


my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved


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
