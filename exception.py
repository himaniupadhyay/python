
def example_try_except_else():
    try:
        fh = open("testfile", "r")
        fh.write("This is my test file for exception handling!!")
    except IOError:
        return False
    else:
        return True


def example_finally():
    try:
        fh = open("testfile", "w")
        fh.write("This is my test file for exception handling!!")
    finally:
        return "In Finally"


def example_try_except():
    try:
        fh = open("testfile", "w")
        try:
            fh.write("This is my test file for exception handling!!")
        finally:
            fh.close()
    except IOError:
        print "Error:"