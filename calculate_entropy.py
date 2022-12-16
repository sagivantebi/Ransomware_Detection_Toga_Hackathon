import math


# make entropy of files to determent which file is corrupted and which is ok
# if the entropy is close to 8 is ok
# else is close to 0 something is wrong with the file
def entropy(file_name):
    with open(file_name, "rb") as f:
        byte_array = f.read()
        byte_counts = [0] * 256

        # Count the number of occurrences of each byte value
        for byte in byte_array:
            byte_counts[byte] += 1

        # Calculate the entropy
        entropy = 0
        for count in byte_counts:
            if count > 0:
                probability = count / len(byte_array)
                entropy -= probability * math.log2(probability)

        return entropy


def check_files_entropy(path1, path2):
    ent = entropy(path1)
    ent2 = entropy(path2)
    dist = math.pow((ent - ent2), 2)
    if dist > 0.001:
        return dist
    else:
        return dist
