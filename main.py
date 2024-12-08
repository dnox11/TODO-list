from todo import TaskNote


task_note = TaskNote()


def main():
    while True:
        print('\nMenu:')
        print('1. Add task')
        print('2. Show tasks')
        print('3. Edit tasks')
        print('4. Remove task')
        print('5. End task')
        print('6. Exit')

        choose = int(input('Select action: '))

        if choose == 1:
            task_note.add_task()
        elif choose == 2:
            task_note.tasks_list()
        elif choose == 3:
            task_note.edit_task()
        elif choose == 4:
            task_note.remove_task()
        elif choose == 5:
            task_note.end_task()
        elif choose == 6:
            break
        else:
            print('Incorrect choose')


if __name__ == '__main__':
    main()




