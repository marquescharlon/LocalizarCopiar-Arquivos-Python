import create_folder
import copy_files
import parameters as p

if __name__ == '__main__':

    create_folder.folder(p.path_destination, delete=True)
    copy_files.copy(p.path_origin, p.identify_file, p.path_destination)