def example_file_read_write():
    with open('helloworld.txt', 'r') as f:
        content = f.readlines()

    content = [x.upper() for x in content]

    with open('helloworld.txt', 'w') as f:
        for line in content:
            f.write(line)


def reset():
    with open('helloworld.txt', 'r') as f:
        content = f.readlines()

    content = [x.lower() for x in content]

    with open('helloworld.txt', 'w') as f:
        for line in content:
            f.write(line)
