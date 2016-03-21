import os
import re
def create_single_face_label_txt(image_dir, list_file):
    with open(list_file, 'r') as f:
        lines = f.readlines()
        attributes_list = re.findall('\w+', lines[1])
        for line in  lines[2:]:
            imagename = re.findall('\w+\.jpg', line)
            labels = re.findall(' -?1', line)
            print "processing %s" % imagename
            if imagename and labels:
                with open(image_dir + os.sep + imagename[0].strip()[0 : -3] + 'txt', 'a') as ff:
                    new_lines = []
                    for i in range(40):
                        new_lines.append(attributes_list[i] + " " + labels[i].strip() + "\n")
                    ff.writelines(new_lines)

def create_single_face_landmark_txt(image_dir, list_file):
    with open(list_file, 'r') as f:
        lines = f.readlines()
        location_list = ['eye', 'nose', 'mouth']
        for line in  lines[2:]:
            imagename = re.findall('\w+\.jpg', line)
            coordinates = re.findall(' \d+', line)
            print "processing %s" % imagename
            if imagename and coordinates:
                with open(image_dir + os.sep + imagename[0].strip()[0 : -3] + 'txt', 'w+') as ff:
                    new_lines = []
                    new_lines.append(location_list[0] + " " + coordinates[0].strip() + " " + coordinates[1].strip() + " " + coordinates[2].strip() + " " + coordinates[3].strip() + "\n")
                    new_lines.append(location_list[1] + " " + coordinates[4].strip() + " " + coordinates[5].strip() + "\n")
                    new_lines.append(location_list[2] + " " + coordinates[6].strip() + " " + coordinates[7].strip() + " " + coordinates[8].strip() + " " + coordinates[9].strip() + "\n")
                    ff.writelines(new_lines)