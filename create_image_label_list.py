import util as ut

def create_image_label_list(src):
    image_list = ut.list_images(src)
    for image in image_list:
        image_txt_file = 