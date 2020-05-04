#!/usr/bin/python3
"""
Returns information about a given employee's TODO list progress.
"""
from argparse import ArgumentParser
from json import dump
from os import path
from requests import get
from sys import argv

API = 'https://jsonplaceholder.typicode.com'
USERS = 'https://jsonplaceholder.typicode.com/users'
TODOS = 'https://jsonplaceholder.typicode.com/todos'

if __name__ == '__main__':
    with open('todo_all_employees.json', 'w') as ostream:
        dump({
            str(user['id']): [{
                "username": user['username'],
                "task": task['title'],
                "completed": task['completed'],
            } for task in get(TODOS, params={'userId': user['id']}).json()]
            for user in get(USERS).json()
        }, ostream)
