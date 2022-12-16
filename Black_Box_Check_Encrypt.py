import calculate_entropy as ce

ENTROPY_LIST = []
COMPARED_LIST = ["jpeg", "pdf", "png","jpg"]
TEXT_LIST = []
ASCII_LIST = ["txt"]

COMMON_ENCRYPTED_EXTENSION = ['micro', 'zepto', 'cerber', 'locky', 'cerber3', 'cryp1', 'mole', 'onion', 'axx', 'osiris',
                              'crypz', 'crypt', 'locked', 'odin', 'ccc', 'cerber2', 'sage', 'globe', 'exx', 'good',
                              'wallet', '1txt', 'decrypt2017', 'encrypt', 'ezz', 'zzzzz', 'MERRY', 'enciphered', 'r5a',
                              'aesir', 'ecc', 'enigma', 'cryptowall', 'encrypted', 'loli', 'breaking_bad', 'coded',
                              'ha3', 'damage', 'wcry', 'lol!', 'cryptolocker', 'dharma', 'MRCR1', 'sexy', 'crjoker',
                              'fantom', 'keybtc@inbox_com', 'rrk', 'legion', 'kratos', 'LeChiffre', 'kraken', 'zcrypt',
                              'maya', 'enc', 'file0locked', 'crinf', 'serp', 'potato', 'ytbl', 'surprise',
                              'angelamerkel', 'windows10', 'lesli', 'serpent', 'PEGS1', 'dale', 'pdcr', 'zzz', 'xyz',
                              '1cbu1', 'venusf', 'coverton', 'thor', 'rnsmwr', 'evillock', 'R16m01d05', 'wflx',
                              'nuclear55', 'darkness', 'encr', 'rekt', 'kernel_time', 'zyklon', 'Dexter', 'locklock',
                              'cry', 'VforVendetta', 'btc', 'raid10', 'dCrypt', 'zorro', 'AngleWare', 'EnCiPhErEd',
                              'purge', 'realfs0ciety@sigaint.org.fs0ciety', 'shit', 'atlas', 'exotic', 'crypted',
                              'padcrypt', 'xxx', 'hush', 'bin', 'vbransom', 'RMCM1', 'cryeye', 'unavailable',
                              'braincrypt', 'fucked', 'crypte', 'AiraCropEncrypted', 'stn', 'paym', 'spora', 'dll',
                              'RARE1', 'alcatraz', 'pzdc', 'aaa', 'encrypted', 'ttt', 'odcodc', 'vvv', 'ruby', 'pays',
                              'comrade', 'enc', 'abc', 'xxx', 'antihacker2017', 'herbst', 'szf', 'rekt', 'bript',
                              'crptrgr', 'kkk', 'rdm', 'BarRax', 'vindows', 'helpmeencedfiles', 'hnumkhotep',
                              'CCCRRRPPP', 'kyra', 'fun', 'rip', '73i87A', 'bitstak', 'kernel_complete', 'payrms',
                              'a5zfn', 'perl', 'noproblemwedecfiles​', 'lcked', 'p5tkjw', 'paymst', 'magic', 'payms',
                              'd4nk', 'SecureCrypted', 'paymts', 'kostya', 'lovewindows', 'madebyadam',
                              'powerfulldecrypt', 'gefickt', 'kernel']


def check_files(path1, path2):
    with open(path1, 'rb') as f1, open(path2, 'rb') as f2:
        while True:
            b1 = f1.read(4096)
            b2 = f2.read(4096)
            if b1 != b2:
                return 2
            if not b1:
                return 0


def checkIfLengthOfWordIsOverX(file):
    count = 0
    with open(file, 'r') as f:
        # Read the entire file into a string
        text = f.read()

        # Iterate over the characters in the string
        for ch in text:
            # Print each character
            if ch == " ":
                count = 0
            else:
                count = count + 1
            if count == 50:
                return True, 1
    return False, 0


# check if exist an character that is not in the ASCII table in the file
# get path and return true or false
# check
def check_valid_ascii(path):
    with open(path, 'rb') as f:
        while True:
            b1 = f.read(4096)
            for i in b1:
                if i > 127:
                    return 1
            if not b1:
                return 0

def check_name_htn(path):
    extension = path.split(".")
    # print(extension[-1])
    # print(extension[-2])
    if "htn" in str(path):
        print(path)
        return 10
    return 0

def black_box(path1, path2):
    extension = path2.split(".")[-1]

    sum_anomaly = 0

    if "2_world192" in str(path2):
        print("check")

    sum_anomaly += check_name_htn(path2)

    if extension in COMPARED_LIST:
        sum_anomaly += check_files(path1, path2)

    # if extension in ENTROPY_LIST:
    sum_anomaly += ce.check_files_entropy(path1, path2)

    if sum_anomaly >= 1.002:
        return True, sum_anomaly
    else:
        return False, 0

    # if extension in ASCII_LIST:
    #     bool1, temp = check_valid_ascii(path1)
    #     sum_anomaly += temp
    #
    # if extension in COMMON_ENCRYPTED_EXTENSION:
    #     sum_anomaly += 1

