import os,sys,shutil

src_path = '/Users/macadmin/tests'
#your_path = '/Users/macadmin/OneDrive - Monster_AD/07_github_lazu/gitrepolazu/shellscripts'

for x in os.listdir(src_path): 
    #if x.endswith('.sh'):
    print(x)
    temp_dir_name = x.rsplit('.', 1)[0]
    print('temp dir    : ' + temp_dir_name)
    src_file = os.path.abspath(x)
    print('source file : ' + src_file)
    new_dir_name = os.path.join(src_path, temp_dir_name)
    print('new dir     : ' + new_dir_name)
    #os.mkdir(new_dir_name)
    #shutil.move(src_file,new_dir_name)

print('---')
#print(os.path.basename(src_path))