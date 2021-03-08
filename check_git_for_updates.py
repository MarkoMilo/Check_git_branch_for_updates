import os
import pathlib
import subprocess
SOURCE_PATH = os.path.normpath(os.getcwd() + os.sep + os.pardir)
EXAMPLE_PATH = os.getcwd()
CURRENT_BRANCH = "test_branch"
MERGE_BRANCH = "main"

test_path = pathlib.Path(__file__).resolve().parent


def git_stash():
    if os.name == 'nt':  # if OS Windows
        print('\n**********************  git stash  **********************\n')
        os.system('cmd /c git stash')
    else: 
        print('\n**********************  git stash  **********************\n')
        os.system('cmd git stash')


def git_stash_pop():
    if os.name == 'nt':  # if OS Windows
        print('\n**********************  cmd stash pop  **********************p\n')
        os.system('cmd /c git stash pop')
    else: 
        print('\n**********************  cmd stash pop  **********************p\n')
        os.system('cmd git stash pop')


def git_sheckout(branch):
    if os.name == 'nt':  # if OS Windows
        print('\n**********************  git checkout {}  **********************\n'.format(branch))
        os.system('cmd /c git checkout {}'.format(branch))
    else: 
        print('\n**********************  git checkout {}  **********************\n'.format(branch))
        os.system('cmd git checkout {}'.format(branch))


def check_git_branch(current_branch=CURRENT_BRANCH, merge_branch=MERGE_BRANCH):
    # os.chdir(test_path)
    if os.name == 'nt':  # if OS Windows
        print('\n**********************  git status  **********************\n')
        os.system('cmd /c git status')
        git_sheckout(current_branch)
        git_stash()
        git_sheckout(merge_branch)
        print('\n**********************  git remote update  **********************\n')
        os.system('cmd /c git remote update')
        print('\n**********************  git status -uno  **********************\n')
        return_val = 'cmd /c git status -uno'
        proc = subprocess.Popen(return_val, creationflags=subprocess.CREATE_NEW_CONSOLE, stdout=subprocess.PIPE)
        output = proc.communicate()[0]
        out = output.decode('utf-8')
        print(out)
        if 'Your branch is behind' in out:
            git_sheckout(current_branch)
            return True
        elif 'Your branch is up to date with' in out:
            git_sheckout(current_branch)
            git_stash_pop()
            return False
        else:
            git_sheckout(current_branch)
            git_stash_pop()
            return False
    else:  # if system Linux or MAC
        print('\n**********************  git status  **********************\n')
        os.system('cmd git status')
        git_sheckout(current_branch)
        git_stash()
        git_sheckout(merge_branch)
        print('\n**********************  git remote update  **********************\n')
        os.system('cmd git remote update')
        print('\n**********************  git status -uno  **********************\n')
        return_val = 'cmd git status -uno'
        proc = subprocess.Popen(return_val, creationflags=subprocess.CREATE_NEW_CONSOLE, stdout=subprocess.PIPE)
        output = proc.communicate()[0]
        out = output.decode('utf-8')
        print(out)
        if 'Your branch is behind' in out:
            print('\n**********************  git pull  **********************\n')
            os.system('cmd /c git pull')
            git_sheckout(current_branch)
            return True
        elif 'Your branch is up to date with' in out:
            git_sheckout(current_branch)
            git_stash_pop()
            return False
        else:
            git_sheckout(current_branch)
            git_stash_pop()
            return False


def do_something():  # Do something with a new code
    if check_git_branch():
        if os.name == 'nt':  # if OS Windows
            print('\n**********************  cmd pull origin {} **********************n \n'.format(MERGE_BRANCH))
            os.system('cmd /c git pull origin {}'.format(MERGE_BRANCH))
            git_stash_pop()
            print("\n\n {} is updated\n\n".format(MERGE_BRANCH))
        else:  # if system Linux or MAC
            print('\n**********************  cmd pull origin master **********************n \n')
            os.system('git pull origin master')
            git_stash_pop()
    else:
        git_stash_pop()


do_something()
