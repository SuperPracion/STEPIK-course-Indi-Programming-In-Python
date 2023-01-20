def file_read(file_name):
    data = open(file_name, encoding='utf-8')
    print(data.read())
