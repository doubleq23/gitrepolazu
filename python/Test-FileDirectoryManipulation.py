import os,shutil

src_path = '/Users/macadmin/tests/'

def list_files(src_path):
    for file in sorted(os.listdir(src_path)):
        if os.path.isfile(os.path.join(src_path,file)):
            yield file

for file in list_files(src_path):
    print(file)
    src_file = os.path.join(src_path, file)
    print('source file : ' + src_file)
    temp_dir_name = file.rsplit('.', 1)[0]
    new_dir_name = os.path.join(src_path, temp_dir_name)
    print('destination : ' + new_dir_name)

    if not os.path.exists(new_dir_name):
        print("Create new directory " + temp_dir_name)
        os.mkdir(new_dir_name)
    else:
        print("Directory " + temp_dir_name + " exist")

    print("Move " + file + " to " + new_dir_name)
    shutil.move(src_file,new_dir_name,copy_function = shutil.copytree)
    
"""
for x in os.listdir(src_path):
    #if x.endswith('.sh'):
    src_file = src_path + x
    print('source file : ' + src_file)
    temp_dir_name = x.rsplit('.', 1)[0]
    #print('tmp dirname : ' + temp_dir_name)
    new_dir_name = os.path.join(src_path, temp_dir_name)
    print('destination : ' + new_dir_name)
    
    #os.mkdir(new_dir_name)
    #shutil.move(src_file,new_dir_name,copy_function = shutil.copytree)

    if not os.path.exists(new_dir_name):
        print("Create new directory " + temp_dir_name)
    else:
        print("Directory " + temp_dir_name + " exist")
"""