import time
from check_git_for_updates import do_something

# something Update


def main():
    do_something()


if __name__ == "__main__":
    while True:
        main()
        time.sleep(3600)  # check repository every 1 hour
