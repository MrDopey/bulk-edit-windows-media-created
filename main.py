import os
import time
from datetime import datetime

def set_file_creation_date(file_path):
    # Extract the date from the filename
    base_name = os.path.basename(file_path)
    date_str = base_name.split('.')[0]  # Assuming the date is before the first dot
    date_format = "%Y%m%d %H%M%S"
    
    try:
        # Parse the date
        creation_time = datetime.strptime(date_str, date_format)
        # Convert to a timestamp
        creation_timestamp = time.mktime(creation_time.timetuple())
        
        # Set the creation and modification times
        os.utime(file_path, (creation_timestamp, creation_timestamp))
        print(f"Creation date of {file_path} set to {creation_time}")
    except ValueError:
        print(f"Filename {base_name} does not match the format {date_format}")

# Example usage
file_path = '20170208 065102.mp4'
set_file_creation_date(file_path)

