# TODO backend application

REST API for simple TODO application built onto django-rest-framework

## Prerequisites

The application requires:
- docker (tested on version 27.3.1)
- docker-compose (tested on version 2.29.7)

## Setup

### Docker

To create and run containers with postgres and django you can run:

    docker-compose up

It will create two containers. First with postgres database and second
with django server on gunicorn. Database data is stored on a docker volume,
therefore it is persistent.

Django server will be available on port 8001.

    curl http://localhost:8001/todo/api/v1/tasks

### Local

If you want to run django server without docker and with sqlite database,
you need to setup environment like this:

    python3.11 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate

    python manage.py runserver 8001

## Usage

### API Resources

  - [GET /tasks](#get-tasks)
  - [GET /tasks/[id]](#get-tasksid)
  - [POST /tasks](#post-tasks)
  - [PUT /tasks/[id]](#put-tasksid)
  - [DELETE /tasks/[id]](#delete-tasksid)

#### GET /tasks

Example: http://localhost:8001/todo/api/v1/tasks

Response body:

    [
       {
          "id" : 1,
          "title" : "title",
          "description" : "desc",
          "done" : true
       },
       {
          "id" : 2,
          "title" : "title2",
          "description" : "desc2",
          "done" : false
       }
    ]

#### GET /tasks/[id]

Example: http://localhost:8001/todo/api/v1/tasks/[id]

Response body:

    {
       "id" : 3,
       "done" : false,
       "description" : "desc",
       "title" : "title"
    }


#### POST /tasks

Example: Create – POST  http://localhost:8001/todo/api/v1/tasks

Request body:

    {
       "title" : "title",
       "description" : "desc",
       "done" : false,
    }


#### PUT /tasks/[id]

Example: Update - PUT  http://localhost:8001/todo/api/v1/tasks/[id]

Request body:

    {
       "title" : "title",
       "description" : "desc",
       "done" : false,
    }


#### DELETE /tasks/[id]

Example: Delete - DELETE http://localhost:8001/todo/api/v1/tasks/[id]


### Curl examples

You may want to test the API from a command line.
Here are some curl examples to execute by yourself:

    curl -X POST -H 'Content-type: application/json' \
      -d '{"title": "t", "description": "d", "done": true}' \
      http://localhost:8001/todo/api/v1/tasks

    curl http://localhost:8001/todo/api/v1/tasks

    curl -X PUT \
      -H 'Content-type: application/json' \
      -d '{"title": "changed title", "description": "desc", "done": false}' \
      http://localhost:8001/todo/api/v1/tasks/3

    curl http://localhost:8001/todo/api/v1/tasks/1

    curl -X DELETE http://localhost:8001/todo/api/v1/tasks/1
