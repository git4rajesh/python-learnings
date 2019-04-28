def create_project(msg):
    # This is the outer enclosing function
    print('Creating Projects with name {}'.format(msg))
    project_id = 1

    def create_task():
        task_id = 2
        print('Creating Tasks under project_id {}'.format(project_id))
    return create_task


create_task = create_project("Auto")
create_task()


