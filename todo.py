import json
from datetime import datetime


class TaskNote():
    def __init__(self, file_name = 'storage.json') -> None:
        self.file_name = file_name
        self.load_task()

    def load_task(self) -> None:
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                self.data = json.load(file)

            if not isinstance(self.data, dict):
                raise ValueError("Invalid JSON format: expected a dictionary.")
        except (FileNotFoundError, ValueError, json.JSONDecodeError):
            self.data = {}

    def add_task(self) -> None:
        title = input('Enter task name: ')
        description = input('Describe the task: ')
        deadline = input('deadlines: ')
        task_id = len(self.data) + 1
        creation_time = datetime.today().isoformat()
        dt = datetime.fromisoformat(creation_time)
        formatted_creation_time = dt.strftime('%d.%m.%Y %H:%M')
        self.data[task_id] = {
            'title': title,
            'description': description,
            'deadline': deadline,
            'complete': 'Not completed',
            'creation_time': formatted_creation_time,
        }

        self.save_task()

        print('Task added')

    def save_task(self) -> None:
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4)

    def remove_task(self) -> None:
        task_id = input('Enter task id: ')

        if task_id in self.data:
            del self.data[task_id]
            self.save_task()

    def edit_task(self) -> None:
        self.load_task()

        task_id = input('Enter task id: ')
        new_task_description = input('Enter new task description: ')
        if task_id in self.data:
            self.data[task_id]['description'] = new_task_description
            self.save_task()
            print(f'New task {task_id} description successfully added!')
        else:
            print(f'Task {task_id} not found...')

    def mark_task(self) -> None:
        self.load_task()

        task_id = input('Enter task id: ')
        print('1. Mark in progress')
        print('2. Mark as done')

        if task_id in self.data:
            action = int(input('Select action: '))
            if action == 1:
                self.data[task_id]['complete'] = 'In progress'
                self.save_task()
                print('The task is marked as in progress')
            elif action == 2:
                self.data[task_id]['complete'] = 'Completed'
                self.save_task()
                print(f'Task {task_id} successfully completed!')
        else:
            print(f'Task {task_id} not found...')

    def tasks_list(self) -> None:
        self.load_task()

        print('1. Display completed tasks')
        print('2. Display tasks in progress')
        print('3. Display uncompleted tasks')

        action = int(input('Select filter: '))

        sorted_task_list = {}
        for key, value in self.data.items():
            if action == 1:
                if self.data[key]['complete'] == 'Completed':
                    sorted_task_list[key] = value
            elif action == 2:
                if self.data[key]['complete'] == 'In progress':
                    sorted_task_list[key] = value
            elif action == 3:
                if self.data[key]['complete'] == 'Not completed':
                    sorted_task_list[key] = value
            else:
                print('Incorrect action input')

        print(sorted_task_list)
