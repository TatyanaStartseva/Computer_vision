import os
import shutil
def get_last_numeric_folder(path):
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(
        path,f))]
    numeric_folders = [int(f) for f in folders if f.isdigit()]
    if not numeric_folders:
        return None
    return max(numeric_folders)
def move_and_create_new_folder(path,path_tdata):
    last_num_folder = get_last_numeric_folder(path)
    if last_num_folder is None:
        folder_name = 1
    else:
        folder_name = last_num_folder+1
    new_folder = os.path.join(path,str(folder_name))
    os.makedirs(new_folder, exist_ok=True)
    if path_tdata and os.path.exists(path_tdata):
        tdata_path = os.path.join(path_tdata, "tdata")
        shutil.move(tdata_path,new_folder)
        print(f"Папка 'tdata' перемещена в '{new_folder}'")
    else:
        print("Папка 'tdata' не найдена.")