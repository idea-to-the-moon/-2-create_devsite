#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_directory(dirpath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dirpath))

def rename(filepath, newname):
    os.rename(os.path.join(PROJECT_DIRECTORY, filepath), os.path.join(PROJECT_DIRECTORY, newname), )   

def move(dirpath, dst):
    shutil.move(os.path.join(PROJECT_DIRECTORY, dirpath), os.path.join(PROJECT_DIRECTORY, dst))



if __name__ == '__main__':

    move('reveal', '{{ cookiecutter.project_slug }}_devsite/assets')


    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE.rst')

    # Create the communication tools
    if 'n' == '{{ cookiecutter.create_devsite }}':
        remove_directory('{{ cookiecutter.project_slug }}_devsite')

    if 'y' == '{{ cookiecutter.create_doc }}':
        os.system("cd docs && make html && cd..")

    # Create the collaboration tools
    if 'y' == '{{ cookiecutter.create_trello }}':
        os.system("cd tools_generator && lets_work && cd..")

    if 'y' == '{{ cookiecutter.create_git }}':
        os.system("git init && git flow init")
