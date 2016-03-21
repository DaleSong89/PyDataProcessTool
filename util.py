import os
import shutil
import re


def check_folder_exist(dir):
    isExist = os.path.exists(dir)
    if not isExist:
        os.mkdir(dir)
        print dir + ' created success!'
        return 1
    else:
        print dir + ' already exists!'
        return 0

def pick_up_image_files(root_dir, files):
    image_list = []
    for image_name in files:
        if image_name.endswith(('.jpg', '.bmp', '.JPG', '.BMP')):
            image_list.append(os.path.join(root_dir, image_name))
    return image_list

def list_images(src):
    print 'sourc dir: %s' % (src)
    images_list = []
    for parent, dirnames, filenames in os.walk(src):
     #   print '%s' % (filenames[0])
        for file_name in filenames:
            if file_name.endswith(('.jpg', '.bmp', '.JPG', '.BMP')):
                image = os.path.join(parent, file_name)
     #           print '%s' % (image)
                images_list.append(image)
    return images_list

def copy_without_replace(sample_image, text_file_name, dst_dir):
    ''' copy sample_image and its info file 'text_file_name' to dst_dir'''
    if sample_image:
        rename_sample_image = dst_dir + sample_image[sample_image.rfind(os.sep) + len(os.sep):]
        while os.path.exists(rename_sample_image):
            rename_sample_image = rename_sample_image[0 : -4] + '_r' + sample_image[-4:]
        shutil.copyfile(sample_image, rename_sample_image)
    if text_file_name and os.path.exists(text_file_name):
        rename_sample_text = dst_dir + text_file_name[text_file_name.rfind(os.sep) + len(os.sep):]
        while os.path.exists(rename_sample_text) :
            rename_sample_text = rename_sample_text[0 : -4] + '_r' + '.txt'
        shutil.copyfile(text_file_name, rename_sample_text)
    else:
        print "%s do not exist!" % text_file_name
    return True

def scan_float_data(string):
    float_data_list = []
    element = -1
    elements = re.findall('(\d+(\.\d+)?(e-?\d+)?)', string)
    # elements = re.findall('(\d+(\.\d+)?e-\d+)', string)
    '''
    for element in elements:
        element = element.strip()
        float_data_list.append(float(element))
    '''
    if elements:
        element_tuple = elements[0]
        element = float(element_tuple[0])
    return element

def scan_key(line):
    key_word = re.findall('^\S*', line)
    return key_word[0].strip()