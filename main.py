# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess
import sys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    my_pipe = subprocess.run('ls -la\n'.split(), stdout=subprocess.PIPE)

    print((my_pipe.stdout))

    sys.stdout.write('print to screen...\n\n')

    # sti = sys.stdin.readline()
    # sys.stdout.write('here\'s {}'.format(sti))
    print('done')
    # sys.stderr.write('an error has occcc')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
