from datetime import datetime
import os
import time
#
# from hachoir.parser import createParser
# from hachoir.editor import createEditor
# from hachoir.field import writeIntoFile
# from hachoir.metadata import extractMetadata
#
from mutagen.mp4 import MP4
from pymkv import MKVFile
from exif import Image

import pytz
from win32com.propsys import propsys, pscon
import pythoncom
from win32com.shell import shellcon

# Initialize COM library
# win32com.client.pythoncom.CoInitialize()
# propsys = win32com.client.Dispatch("propsys.SHGetPropertyStoreFromParsingName")

# if not isinstance(dt, datetime.datetime):
#     # In Python 2, PyWin32 returns a custom time type instead of
#     # using a datetime subclass. It has a Format method for strftime
#     # style formatting, but let's just convert it to datetime:
#     dt = datetime.datetime.fromtimestamp(int(dt))
#     dt = dt.replace(tzinfo=pytz.timezone('UTC'))
def set_file_creation_date(file_path: str):
    # Extract the date from the filename
    base_name = os.path.basename(file_path)
    date_str = base_name.split('.')[0]  # Assuming the date is before the first dot
    date_format = "%Y%m%d %H%M%S"
    
    # Parse the date
    creation_time = datetime.strptime(date_str, date_format)
    # Convert to a timestamp
    creation_timestamp = time.mktime(creation_time.timetuple())
    
    # Set the creation and modification times
    os.utime(file_path, (creation_timestamp, creation_timestamp))
    # Open the video file
    # parser = createParser(file_path)
    # # metadata = extractMetadata(parser)
    # 
    # # Extract metadata
    # metadata = extractMetadata(parser)
    # if not metadata:
    #     print("Unable to extract metadata")
    #     exit(1)
    #
    # # Print all metadata
    # for item in metadata.eportPlaintext():
    #     print(item)

    # mkv = MKVFile(file_path)
    # for track in mkv.tracks:
    #     print(track)
    #
    
    
    print(creation_time)
    print(datetime.fromtimestamp(os.path.getctime(file_path)))
    # Open the image file
    # with open(file_path, 'rb') as image_file:
    #     img = Image(image_file)
      
    print(pscon.PKEY_Media_DateEncoded)
    print(file_path)
    properties = propsys.SHGetPropertyStoreFromParsingName(file_path, None, shellcon.GPS_READWRITE, propsys.IID_IPropertyStore)
    # dt = properties.GetValue(pscon.PKEY_Media_DateEncoded).GetValue()
    the_date = creation_time.astimezone(pytz.timezone('Australia/Sydney'))

    prop_variant = propsys.PROPVARIANTType(the_date, pythoncom.VT_DATE)
    properties.SetValue(pscon.PKEY_Media_DateEncoded, prop_variant)
    properties.Commit()
    print(the_date)



    
    # if img.has_exif:
    #     pass
        # for field in img.list_all():
        #     print(f"{field}")
            # print(f"{field}: {getattr(img, field)}")
    # Modify EXIF tags


    # Save the changes
    # with open(file_path, 'wb') as new_image_file:
    #     new_image_file.write(img.get_file())
    
    # # Load the MP4 file
    # video = MP4(file_path)
    #
    # # Print all metadata
    # for key, value in video.tags.items():
    #     if isinstance(value, list) and len(value) > 0 and isinstance(value[0], bytes):
    #         value = [ v.decode('utf-8', 'ignore') for v in value ]
    #     print(f"{key}: {value}")
    # 
    # print(video.info.codec)
    # print(video.info.codec_description)
    # # https://mutagen.readthedocs.io/en/latest/api/mp4.html#mutagen.mp4.MP4Tags
    # video['\xa9nam'] = 'bobby here'
    # video.pprint()
    # video.info.pprint()
    # # video['purd'] = creation_timestamp 
    # video.save()
    #
    # for key, value in video.tags.items():
    #     print(f"{key}: {value}")

    # Edit the metadata
    # editor = createEditor(parser)
    # editor.setValue('creation_date', '2023-01-01 12:00:00')
    # print(editor.array())
    # writeIntoFile(editor, file_path)
    # editor.write()
    print(f"Creation date of {file_path} set to {creation_time}")

# Example usage
# file_path = '20170208 065102.mp4'
# set_file_creation_date(file_path)

# set_file_creation_date(rf"C:\Sandbox\test\stuff\20170208 065102.mp4")
# Specify the absolute directory path
directory_path =rf"stuff"

# Loop through all files in the directory
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path):
        # print(file_path)
        set_file_creation_date(os.path.abspath(file_path))


