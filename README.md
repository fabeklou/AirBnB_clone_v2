# AirBnB_clone

<p>
    <img size="400" src="https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step2.png">
</p>

## Description of the project

This is the first step towards building my first full web application: the AirBnB clone. This first step is very important because i will use what i build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration...

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/justinmajetich/AirBnB_clone/tree/dev/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/__init__.py) [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) [/models/place.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/place.py) [/models/city.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/city.py) [/models/amenity.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/amenity.py) [/models/state.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/state.py) [/models/review.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>
<br>

## Part 1 : The console

In this first part, the console (which is simillar to a sandbox usually used for testing new feature and troubleshooting) was implemented.

This givs us the ability to perfom CRUD operations by entring pre defined commands.

It indefinitely displays a prompt asking the user to enter a command.
The command is then read, analyzed and executed using the Cmd class (which works miracles) and the set of predefined methods that accompany it.

Most of them were overwritten in our user defined class which inherit from the Cmd class.

More simply, we will be able to :

- create new objects
- retrieve an object from the database (file storage)
- perform some operations on the objects 
- update attributes of an object 
- destroy/delete an object

Using the following commands :

- `show` - Shows an object based on class and UUID
- `create` - Creates an instance based on given class
- `update` - Updates existing attributes an object based on class name and UUID
- `destroy` - Destroys an object based on class and UUID
- `count` - Shows the number of objects
- `all` - Shows all objects the program has access to, or all objects of a given class
- `quit` - Exits the program (EOF will as well)

To make the use of the console more user-friendly, other commands are also available :

- help
- exit
- 

## How to get the console on your local machine ?

### What you need

- git
- python3 
- ...

## How to run/start it ?


## How to use it ?

### a few examples

## Testing 

## Authors

Fabrice Eklou | twitter : [fabeklou](https://www.twitter.com/fabeklou)
                linkedin : [Fabrice Eklou](https://www.linkedin.com/in/fabrice-eklou-989678129/)
                