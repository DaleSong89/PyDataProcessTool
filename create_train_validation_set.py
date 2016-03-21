import sys
import os
import random
import re
import argparse

import util

class RandomStrategy():
    def __init__(self, src, dst, ratio):
        self.__src_dir = src
        self.__dst_dir = dst
        self.__ratio = ratio
    def create_train_validation_set(self):
        subfolders_set = []
        if self.__src_dir in self.__dst_dir:
            print 'dst_dir can not be a subfolder of src_dir!'
            exit(1)
        train_set_dir = self.__dst_dir + os.sep + 'train' + os.sep
        validation_set_dir = self.__dst_dir + os.sep + 'validation' + os.sep
        util.check_train_validation_folder(train_set_dir, validation_set_dir)    
        for parent, subfolders, files in os.walk(self.__src_dir):
            print '%s %s' % (parent, subfolders)
            subfolders_set.append(parent)
            if files:
                images_list = util.pick_up_image_files(parent, files)
                RandomStrategy.__copy_image_to_train_validation_dir(self, images_list, train_set_dir, validation_set_dir, self.__ratio)
    def __copy_image_to_train_validation_dir(self, images_list, train_set_dir, validation_set_dir, train_validation_ratio):
        validation_sample_index = []
        image_list = images_list
	    #num = 10
        validation_samples_num = len(image_list) * float(train_validation_ratio)
    #    validation_samples_num = float(validation_samples_num)
        validation_samples_num = round(validation_samples_num)
        validation_samples_num = int(validation_samples_num)
        if len(image_list):
            for i in range(validation_samples_num):
                    validation_sample_index.append(random.randint(0, len(image_list) - 1))
                    validation_sample_image = image_list[validation_sample_index[-1]]
                
                    base_name = validation_sample_image[0 : -4]
                    text_file_name = base_name + '.txt'
                    if os.path.exists(validation_sample_image) and os.path.exists(text_file_name):
                            if util.copy_without_replace(validation_sample_image, text_file_name, validation_set_dir):
                                print 'Copying %s to %s' % (validation_sample_image, validation_set_dir)
                                print 'Copying %s to %s' % (text_file_name, validation_set_dir)
                                image_list[validation_sample_index[-1]] = ''
                            else:
                                exit(0)
                    else:
                            image_list[validation_sample_index[-1]] = ''
                            print 'image or text lost!'
                            continue
            for train_sample_image in image_list:
                if train_sample_image:
                    base_name = train_sample_image[0 : -4]
                    text_file_name = base_name + '.txt'
                    if os.path.exists(train_sample_image) and os.path.exists(text_file_name):
                        if util.copy_without_replace(train_sample_image, text_file_name, train_set_dir):
                            print 'Copying %s to %s' % (train_sample_image, train_set_dir)
                            print 'Copying %s to %s' % (text_file_name, train_set_dir)
                        else:
                            exit(0)
                    else:
                            print 'image or text lost!'
                            continue
class RuledStrategy():
    def __init__(self, src, dst, rule_txt, setlist, label = -1):
        self.__src_dir = src
        self.__dst_dir = dst
        self.__rule_txt = rule_txt
        self.__set_list = setlist
        self.__label = label
    def create_train_validation_set(self):
        if self.__src_dir in self.__dst_dir:
            print 'dst_dir can not be a subfolder of src_dir!'
            exit(1)
        set_list = self.__set_list 
        for set in set_list:
            folder = self.__dst_dir + os.sep + set
            util.check_folder_exist(folder)
        with open(self.__rule_txt, 'r') as f:
            for line in f.readlines():
                image_name = re.findall('\w+\.\w{3}', line)
                image_name = image_name[0].strip()
                flag = re.findall(' \d{1}', line)
                flag = int(flag[0].strip())

                full_image_path = self.__src_dir + os.sep + image_name
                txt_file_path = full_image_path[0 : -3] + "txt"
                
                if len(set_list) == 1:
                    label = self.__label
                    if -1 == label:
                        print "RuledStrategy's member __label must be set!"
                        exit(0)
                    if flag == self.__label:
                        dst_path = self.__dst_dir + os.sep + set_list[0].strip() + os.sep
                    else:
                        continue
                else:
                    dst_path = self.__dst_dir + os.sep + set_list[flag].strip() + os.sep

                if os.path.exists(full_image_path):
                    if util.copy_without_replace(full_image_path, txt_file_path, dst_path):
                        print 'Copying %s to %s' % (full_image_path, dst_path)
                    else:
                        exit(0)
class BalanceStratey():

class CreateTrainValSetCommand():
    def __init__(self, args):
        self.__method = args.method
        self.__src = args.src
        self.__dst = args.dst
        if self.__method == 'random_pick_with_ratio':
            self.__ratio = args.ratio
            self.__strategy = RandomStrategy(self.__src, self.__dst, self.__ratio)
        elif self.__method == 'pick_with_rule':
   #         self.__rule_txt = args.rule
            
            self.__strategy = RuledStrategy(self.__src, self.__dst, args.rule, args.set_list, int(args.label))
    def send(self):
        self.__strategy.create_train_validation_set()

def parse_args():
    usage = '''Create train and validation set using different methonds: 
                    1. "random_pick_with_ratio": randomly pick out images and its text file to train and validation folder seperately with a user-defined ratio
                    2. "pick_with_rule": pick out images with pre-defined rule'''
    parser = argparse.ArgumentParser(description = 'Create train and validation set using different methonds')
    parser.add_argument('src', help = 'The source image path')
    parser.add_argument('dst', help = 'The directory which the train and validation folder will be created')
    parser.add_argument('method',  help = 'The method name, including: 1. random_pick_with_ratio, 2. pick_with_rule')
    parser.add_argument('set_list',  type = str, nargs = '*', help = 'The set to be created and to place the images/txt')
    parser.add_argument('--ratio', type = float, default = 0.9)
    parser.add_argument('--rule', help = 'The rule of "pick_with_rule" method, namely, a text file indicating every images belong to train or validation folder')
    parser.add_argument('--label', help = 'The label for the set when only 1 set directory need to be created!')
    args = parser.parse_args()
    return args
          
if __name__ == '__main__':
    args = parse_args()
    command = CreateTrainValSetCommand(args)
    command.send()
    #create_train_validation_set(sys.argv[1], sys.argv[2], sys.argv[3])
     
