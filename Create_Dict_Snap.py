import os
import time
import glob
from Black_Box_Check_Encrypt import black_box
from create_graph_dist import create_the_graph

volumes = {1: "db/vol_1/", 2: "db/vol_2/", 3: "db/vol_3/"}


def create_props(file_path):
    timestamp_str = time.strftime('%m/%d/%Y-%H:%M:%S', time.gmtime(os.path.getmtime(file_path)))
    file_stats = os.stat(file_path)
    size_file = file_stats.st_size
    only_name_and_type = file_path.split("\\")
    only_name_and_type = only_name_and_type[-1]
    if "." in only_name_and_type:
        type_file = only_name_and_type.split(".")
        file_name_no_type = ".".join(type_file[:-1])
        type_file = type_file[-1]
    else:
        file_name_no_type = only_name_and_type
        # NEED TO CHECK WHAT TO PUT IF IT'S NOT SPECIFIC
        type_file = ""
    return [file_name_no_type, timestamp_str, type_file, size_file]


def create_dict_files(path):
    # DOC:
    # get a map in this format:
    # file name : [ Date + Time last modified , Type , Size]
    map_snap = {}
    # Get list of all files only in the given directory
    list_of_files = filter(os.path.isfile, glob.glob(path + '*'))
    # Iterate over sorted list of files and print file path
    # along with last modification time of file
    for file_path in list_of_files:
        list_to_append = create_props(file_path)
        map_snap[list_to_append[0]] = list_to_append[1:]

    return map_snap


def scan_volume(volume, file_dict):
    snap_dict = {}
    path = volumes[volume]
    print(path)
    for i in range(2, 11):
        curr_path = path + f'snapshot_{i}/'
        for file in os.listdir(curr_path):
            mod_time = time.strftime('%m/%d/%Y-%H:%M:%S', time.gmtime(os.path.getmtime(curr_path + file)))
            full_file_name_with_path = file
            file_name = file.split(".")
            file_type = file_name[-1]
            file_name = ".".join(file_name[:-1])
            origin_file = file_dict.get(file_name, None)
            if origin_file:
                if mod_time != file_dict[file_name][0]:
                    file_list = snap_dict.get(file_name)
                    if file_list:
                        file_dict[file_name][0] = mod_time
                        snap_dict[file_name].append((i, file_type))
                    else:
                        file_dict[file_name][0] = mod_time
                        snap_dict[file_name] = [(i, file_type)]

            else:
                new_file = create_props(curr_path + file)
                file_dict[new_file[0]] = new_file[1:]
                # need to append to main dict like sagiv version

    return snap_dict


def print_dict(dict):
    for k, v in dict.items():
        print(f' {k}: {v}')
    print("\n\n")


def check_if_encrypted(list_of_scan_dicts, list_of_map_snaps):
    # Content: {volume num : [file name (just name and end) , the snap that got infected first]}
    dict_of_encrypted_files = {}
    distance_list = []

    list_names_for_test = []

    snap_path_1 = "snapshot_1/"
    for i, scan_dict in enumerate(list_of_scan_dicts):
        # for each vol the i will be (i+1)
        rel_path = "db/vol_" + str(i + 1) + "/"
        list_of_encrypted = []
        for file_name, list_snaps in scan_dict.items():
            fist_file_type_snap_1 = list_of_map_snaps[i][file_name][1]
            path1_to_check = rel_path + snap_path_1 + file_name + "." + fist_file_type_snap_1
            for tup in list_snaps:
                # print(i)
                snap_path_j = "snapshot_" + str(tup[0]) + "/"
                type_path_2 = str(tup[1])
                if type_path_2 != "":
                    path2_to_check = rel_path + snap_path_j + file_name + "." + type_path_2
                else:
                    path2_to_check = rel_path + snap_path_j + file_name
                # 0 - True/False | 1 - Distance
                is_encrypted, dist = black_box(path1_to_check, path2_to_check)
                # WANT TO CHECK THE ENTROPY THRASH HOLD
                distance_list.append(dist)
                if is_encrypted:
                    if fist_file_type_snap_1 != "":
                        list_of_encrypted.append((str(file_name + "." + fist_file_type_snap_1), str(tup[0])))
                    else:
                        list_of_encrypted.append((str(file_name), str(tup[0])))
                path1_to_check = path2_to_check
        dict_of_encrypted_files[i + 1] = list_of_encrypted
    return dict_of_encrypted_files, distance_list


def write_encrypted_to_file(dict_of_encrypted_files):
    for i in range(1, 4):
        with open('Output' + str(i) + ".txt", 'w') as f:
            for encrypted_file in dict_of_encrypted_files[i]:
                f.write(str(encrypted_file[0]) + "\t" + "snap_" + str(encrypted_file[1]))
                f.write('\n')
            f.write('\n')


def main():
    map_snap1 = create_dict_files('db/vol_1/snapshot_1/')
    map_snap2 = create_dict_files('db/vol_2/snapshot_1/')
    map_snap3 = create_dict_files('db/vol_3/snapshot_1/')

    # create the dict with the files that changed
    scan_dict1 = scan_volume(1, map_snap1)

    scan_dict2 = scan_volume(2, map_snap2)

    scan_dict3 = scan_volume(3, map_snap3)

    list_of_scan_dicts = [scan_dict1, scan_dict2, scan_dict3]

    list_of_map_snaps = [map_snap1, map_snap2, map_snap3]
    dict_of_encrypted_files, distance_list = check_if_encrypted(list_of_scan_dicts, list_of_map_snaps)

    print(dict_of_encrypted_files)

    write_encrypted_to_file(dict_of_encrypted_files)

    # create_the_graph(distance_list)


if __name__ == "__main__":
    main()
