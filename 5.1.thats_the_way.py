import os


def thats_the_way(path):      # from 5.1
    res = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            file_name = os.path.basename(file_path)
            if file_name.startswith("deep"):
                res.append(file_name)
    return res


if __name__ == '__main__':
    print(thats_the_way('C:/Users/tamar/excellenteam/stuff'))