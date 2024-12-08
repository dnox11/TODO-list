import json
import os
from datetime import datetime


class TaskNote():
    def __init__(self, file_name = 'storage.json') -> None:
        self.file_name = file_name
        self.load_task()

    def load_task(self):
        try:
            if not os.path.exists(self.file_name):
                self.data = {}
                return

            if os.path.getsize(self.file_name) == 0:
                self.data = {}
                return

            with open(self.file_name, 'r', encoding='utf-8') as file:
                self.data = json.load(file)

            if not isinstance(self.data, dict):
                raise ValueError("Invalid JSON format: expected a dictionary.")
        except (FileNotFoundError, ValueError, json.JSONDecodeError):
            self.data = {}



    def add_task(self):
        title = input('Enter task name: ')
        description = input('Describe the task: ')
        deadline = input('deadlines: ')
        task_id = str(len(self.data) + 1)
        creation_time = datetime.today().isoformat()
        self.data[task_id] = {
            'title': title,
            'description': description,
            'deadline': deadline,
            'complete': False,
            'creation_time': creation_time,
        }
        self.save_task()
        print('Task added')


    def save_task(self):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4)


    def remove_task(self):
        task_id = input('Enter task id: ')
        # with open(self.file_name, 'r') as file:
        #     data = json.load(file)
        if task_id in self.data:
            del self.data[task_id]
            self.save_task()

        # self.save_task(data)


    def edit_task(self):
        self.load_task()


        task_id = input('Enter task id: ')
        new_task_description = input('Enter new task description: ')
        if task_id in self.data:
            self.data[task_id]['description'] = new_task_description
            self.save_task()
            print(f'New task {task_id} description successfully added!')
        else:
            print(f'Task {task_id} not found...')


    def end_task(self):
        self.load_task()


        task_id = input('Enter task id: ')
        if task_id in self.data:
            self.data[task_id]['complete'] = True
            self.save_task()
            print(f'Task {task_id} successfully completed!')
        else:
            print(f'Task {task_id} not found...')


    def tasks_list(self):
        self.load_task()


        print(self.data)









