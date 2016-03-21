###### parse_change_images_property ######
'''
import edit_txt_info as ei

image_list = ei.list_images('G:\\ExpressionData\\train_val_expression_2_mouthopen\\train_uniform\\test\\')
expression = ['Anger', 'Contempt', 'Disgust', 'Fear', 'Happiness', 'Neutral', 'Sadness', 'Surprise']
ei.parse_change_images_property(image_list, expression)
'''
###### create_train_validation_set ######
'''
import argparse
import create_train_validation_set as ctv
'''
'''Create train and validation set using different methonds: 
        1. "random_pick_with_ratio": randomly pick out images and its text file to train and validation folder seperately with a user-defined ratio
        2. "pick_with_rule": pick out images with pre-defined rule'''
'''
parser = argparse.ArgumentParser(description = 'Create train and validation set using different methonds')
parser.add_argument('src', help = 'The source image path')
parser.add_argument('dst', help = 'The directory which the train and validation folder will be created')
parser.add_argument('method',  help = 'The method name, including: 1. random_pick_with_ratio, 2. pick_with_rule')
parser.add_argument('set_list',  type = str, nargs = '*', help = 'The set to be created and to place the images/txt')
parser.add_argument('--ratio', type = float, default = 0.9)
parser.add_argument('--rule', help = 'The rule of "pick_with_rule" method, namely, a text file indicating every images belong to train or validation folder')
parser.add_argument('--label', help = 'The label for the set when only 1 set directory need to be created!')

args = parser.parse_args(['--rule=G:\\celeba\\list_eval_partition.txt', '--label=2', 'G:\\celeba\\img_celeba\\', 'D:\\face_attributes\\org\\',   'pick_with_rule', 'test'])
Command = ctv.CreateTrainValSetCommand(args)
Command.send()
'''
###### create_single_face_info_txt ######
'''
import create_single_face_info_txt as csfit

csfit.create_single_face_label_txt('G:\celeba\img_celeba', 'G:\celeba\list_attr_celeba.txt')
'''
###### parse_plot_samples_distribution ######

import parse_plot_samples_distribution as ppld

ppld.plot_images_property_distribution("D:\\face_attributes\\org\\test", ['Arched_Eyebrows', 'Attractive', 'Bags_Under_Eyes', 'Bald', 'Bangs', 'Big_Lips', 'Big_Nose', 'Black_Hair', 'Blond_Hair', 'Blurry', 'Chubby', 'Brown_Hair',  'Bushy_Eyebrows', 'Double_Chin', 'Eyeglasses', 'Goatee', 'Gray_Hair', 'Heavy_Makeup', 'High_Cheekbones', 'Male', 'Mouth_Slightly_Open', 'Mustache', 'Narrow_Eyes', 'No_Beard', 'Oval_Face', 'Pale_Skin', 'Pointy_Nose', 'Receding_Hairline', 'Rosy_Cheeks',  'Sideburns', 'Smiling', 'Straight_Hair', 'Wavy_Hair', 'Wearing_Earrings', 'Wearing_Hat', 'Wearing_Lipstick', 'Wearing_Necklace', 'Wearing_Necktie', 'Young'])
