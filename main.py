import copy_files
import parameters as p

path_origin = p.path_origin
identify_file = p.identify_file
path_destination = p.path_destination

copy_files.copy(path_origin, identify_file, path_destination)