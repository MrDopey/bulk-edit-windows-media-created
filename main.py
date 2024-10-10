from datetime import datetime
import os
import time
import pytz
from win32com.propsys import propsys, pscon
import pythoncom
from win32com.shell import shellcon

def set_file_creation_date(orig_path: str, file_path: str):
    # Extract the date from the filename
    base_name = os.path.basename(file_path)
    date_str = base_name.split('.')[0]  # Assuming the date is before the first dot
    date_format = "%Y%m%d %H%M%S"
    
    # Parse the date from file name
    creation_time = datetime.strptime(date_str, date_format)
    # Parse the date from the original file's modified time
    # creation_time = datetime.fromtimestamp(os.path.getmtime(orig_path))
    print(creation_time)
    # Convert to a timestamp
    creation_timestamp = time.mktime(creation_time.timetuple())
    
    # Set the creation and modification times
    os.utime(file_path, (creation_timestamp, creation_timestamp))
    
    print(pscon.PKEY_Media_DateEncoded)
    properties = propsys.SHGetPropertyStoreFromParsingName(file_path, None, shellcon.GPS_READWRITE, propsys.IID_IPropertyStore)
    # dt = properties.GetValue(pscon.PKEY_Media_DateEncoded).GetValue()
    the_date = creation_time.astimezone(pytz.timezone('Australia/Sydney'))

    prop_variant = propsys.PROPVARIANTType(the_date, pythoncom.VT_DATE)
    properties.SetValue(pscon.PKEY_Media_DateEncoded, prop_variant)
    properties.Commit()
    print(the_date)

# Example usage
# set_file_creation_date(rf"C:\Sandbox\test\orig\20170208_065102.mp4", rf"C:\Sandbox\test\stuff\20170208 065102.mp4")

directory_path =rf"stuff"
original_path =rf"orig"

# Loop through all files in the directory
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    # Handbrake will replace underscores with spaces, so this is the reverse to match the original file name
    original_mirrored_path = os.path.join(original_path, filename.replace(' ', '_'))
    if os.path.isfile(file_path) and os.path.isfile(original_mirrored_path):
        # print(file_path)
        set_file_creation_date(os.path.abspath(original_mirrored_path), os.path.abspath(file_path))
    else:
        print(f"### {file_path} not found")



