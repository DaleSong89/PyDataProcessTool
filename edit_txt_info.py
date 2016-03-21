import sys
import os
import re

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
    
def parse_change_images_property(image_list, property_list):
    label_histogram = []
    for image_path in image_list:
        label_distribution = []
        print('processing: %s' % image_path)
        image_txt_path = image_path[0:-3] + 'txt'
        if os.path.exists(image_txt_path):
            with open(image_txt_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    label_description = scan_float_data(line])
                    key_word = scan_key(line)
#                    print '%f' % (label_description)
                    if key_word in property_list:
                        if 'Disgust' == key_word:
                            label_description = label_description * 0.5 + 0.5
                        else:
                            label_description = label_description * 0.5     
                        lines[line_num] = key_word + ' ' + str(label_description) + '\n'                                 
            with open(image_txt_path, 'w') as f:
                f.writelines(lines)
    return 

def module_test():
    image_list = ['G:\\ExpressionData\\train_val_expression_2_mouthopen\\train_uniform\\test\\10_341_2.jpg']
    expression = ['Anger', 'Contempt', 'Disgust', 'Fear', 'Happiness', 'Neutral', 'Sadness', 'Surprise']
    parse_change_images_property(image_list, expression)
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: change expression label description'
        module_test()
        exit(0)
        #exit(1)
    expression = ['Anger', 'Contempt', 'Disgust', 'Fear', 'Happiness', 'Neutral', 'Sadness', 'Surprise']
    image_list = list_images(sys.argv[1])
    parse_change_images_property(image_list, expression)