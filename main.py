from todo import TaskNote


task_note = TaskNote()


class ListInit:

    def __init__(self) -> None:
        self.output()

    def output(self) -> None:
        while True:
            print('\nMenu:')
            print('1. Add task')
            print('2. Show tasks')
            print('3. Edit tasks')
            print('4. Remove task')
            print('5. Mark task')
            print('6. Exit')

            self.choose = int(input('Select action: '))

            if self.choose == 1:
                task_note.add_task()
            elif self.choose == 2:
                task_note.tasks_list()
            elif self.choose == 3:
                task_note.edit_task()
            elif self.choose == 4:
                task_note.remove_task()
            elif self.choose == 5:
                task_note.mark_task()
            elif self.choose == 6:
                break
            else:
                print('Incorrect choose')


if __name__ == '__main__':
    ListInit()




