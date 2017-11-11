import glob
from random import shuffle

percent_training = 0.75
ELVISNET_BASE_DIR = ".."

all_50s_files = glob.glob("../data/elvi/50s/*")
all_60s_files = glob.glob("../data/elvi/60s/*")
all_70s_files = glob.glob("../data/elvi/70s/*")

def add_category(cat_name, cat_index, train_lines, test_lines) :
    all_files = glob.glob(ELVISNET_BASE_DIR + "/data/elvi/" + cat_name + "/*");
    total_files = len(all_files)
    counter = 0
    for one_file in all_files :
        counter = counter + 1
        if (counter < (percent_training * total_files)) : 
            train_lines.append(one_file + " " + str(cat_index) + "\n")
        else :
            test_lines.append(one_file + " " + str(cat_index) + "\n")



test_lines = []
train_lines = []

add_category("50s", 0, train_lines, test_lines)
add_category("60s", 1, train_lines, test_lines)
add_category("70s", 2, train_lines, test_lines)

# shuffle the lists
shuffle(train_lines)
shuffle(test_lines)

print("creating train_index.txt")
train_file = open("train_index.txt", "w")
for one_line in train_lines :
    train_file.write(one_line)
train_file.close()


print("create test_index.txt")
test_file = open("test_index.txt", "w")
for one_line in test_lines :
    test_file.write(one_line)
test_file.close()



