import sys
import os
import re
import matplotlib.pyplot as plt
import numpy as np
import util as u

def parse_images_property(image_list, property_dimension):
    label_histogram = []
    property_dimension = int(property_dimension)
    for idx in range(property_dimension):
        label_histogram.append(0)
    for image_path in image_list:
        label_distribution = []
        image_txt_path = image_path[0:-3] + 'txt'
        if os.path.exists(image_txt_path):
            with open(image_txt_path, 'r') as f:
                for line in f:
                    label_description = scan_float_data(line)
#                    print '%f' % (label_description)
                    if label_description >= 0:
                        label_distribution.append(label_description)
            label = label_distribution.index(max(label_distribution))
            label_histogram[label] += 1 
    return label_histogram

def get_label_histogram(image_list, properties):
    label_histogram = []
    for i in range(len(properties)):
        label_histogram.append(0)
    for image in image_list:
        image_txt_path = image[0 : -3] + 'txt'
        with open(image_txt_path, 'r') as f:
                for line in f:
                    key = re.search('\w+', line)
                    key = key.group(0).strip()
                    if key in properties:
                        value = re.search('-?1', line)
                        value = int(value.group(0).strip())
                        if 1 == value:
                            idx = properties.index(key)
                            label_histogram[idx] = label_histogram[idx] + 1
    return label_histogram                    

def get_property_name():
    properties = ('Anger', 'Contempt', 'Disgust', 'Fear', 'Happiness', 'Neutral', 'Sadness', 'Surprise')
    return properties

def plot_images_property_distribution(src, properties):
    image_list = u.list_images(src)
    print "properties number: %d" % len(properties)
    label_histogram = get_label_histogram(image_list, properties)
    label_histogram1 = label_histogram[0 : len(properties)/2]
    label_histogram2 = label_histogram[len(properties)/2 : ]
    x_axis1 = properties[0 : int(len(properties)/2)]
    x_axis2 = properties[int(len(properties)/2) : ]
    rect1 = np.arange(int(len(properties)/2))
    r2_num = len(properties) - int(len(properties)/2)
    rect2 = np.arange(r2_num)
    width = 0.1

    fig, (ax1, ax2) = plt.subplots(nrows = 2, sharex = False)
    ax1.bar(rect1, label_histogram1, width, color = 'r')
    ax1.set_xticks(rect1)
    ax1.set_xticklabels(x_axis1)
    print "%d %d" % (len(rect2), len(label_histogram2))
    ax2.bar(rect2, label_histogram2, width, color = 'r')
    ax2.set_xticks(rect2)
    ax2.set_xticklabels(x_axis2)
    #ax2.set_xtickslabels_size(0.1)
  #  plt.plot(properties, label_histogram)
    plt.xlabel('attributes')
    plt.ylabel('num')
    plt.show()
def module_test():
    # list_images('G:\\ExpressionData\\validation')
    images = ['G:\\ExpressionData\\train\\000215.jpg', 'G:\\ExpressionData\\validation\\000281.jpg']
    parse_images_property(images, 8)
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('''Usage: parse_samples_distribution.py source_dir label_list
                 Notes: plot the label histogram of images in the source_dir''')
        #print '%s' % (sys.argv[0])
       # exit(1)
        module_test()
    plot_images_property_distribution(sys.argv[1], sys.argv[2])
        
