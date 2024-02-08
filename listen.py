import os
import time
import threading
import patoolib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            file_extension = os.path.splitext(file_path)[1]
            if file_extension == '.rar' or file_extension == '.zip':
                print(f"New archive file created: {file_path}")
                # Extract the archive file
                self.extract_archive(file_path)

    def extract_archive(self, archive_path):
        folder_path = os.path.dirname(archive_path)
        patoolib.extract_archive(archive_path, outdir=folder_path)
        print(f"Archive file extracted: {archive_path}")

        # Get the name of the extracted folder
        extracted_folder_name = os.path.splitext(os.path.basename(archive_path))[0]

        # Delete the extracted archive file
        extracted_file_path = os.path.join(folder_path, extracted_folder_name)
        os.remove(extracted_file_path)
        print(f"Extracted archive file deleted: {extracted_file_path}")

        print(f"Extracted folder name: {extracted_folder_name}")


# Specify the directory to monitor
directory_to_watch = "C:\\Users\\Dell\\Downloads"

# Create the event handler and observer
event_handler = FileChangeHandler()
observer = Observer()
observer.schedule(event_handler, directory_to_watch, recursive=False)
observer.start()

def start_observer():
    observer.join()

# Start the observer thread
observer_thread = threading.Thread(target=start_observer)
observer_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

# Clean up
observer_thread.join()