# CS50 Web Project 1:  "wiki"
This project is an assignment from the course: [CS50 Web Programming with Python and Javascript](https://cs50.harvard.edu/web/2020/).

## Assignment
Design a Wikipedia-like online encyclopedia.
Assignment details [here](https://cs50.harvard.edu/web/2020/projects/1/wiki/).

## Project Description
“Wiki” is an online encyclopedia made with Django. ”Markdown” is being used as the markup language for all entries of this wiki.
The webpage is divided in several subpages:
* *Home/Index*: Returns an overview of all existing wiki-entries. 
* *Create New Page*: Allows for the creation of new entries. Entries must be written in Markup.
* *Random Page*: Loads randomly an entry from the wiki.
One may edit an entry by clicking on the “Edit Entry”-link on an entry’s page. This will allow for the entries content to be edited and prefills the edit field with the already existing content. The entry’s title can’t be edited.

## Technical Description
Django handles all server request (in Python). Entries in this wiki are saved in the markup language ”Markdown”.\
The web app does not have a database; All entries are saved as Markup-files (.md) in the “Entries” folder.\
Markdown files are read using the markup-module for Python and are then returned to the client as template-data.

## Project Demo
Click [here](https://youtu.be/w1u6jE1Malg) to watch a demonstration of this project on YouTube.

## Distribution Code 
[Distribution Code](https://cdn.cs50.net/web/2020/spring/projects/1/wiki.zip).\
All further requirements and terminal commands to run this project are found on the [Project Assignment Page](https://cs50.harvard.edu/web/2020/projects/1/wiki/)
