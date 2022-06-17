QA Project 1

Project objective:

- To create a CRUD application with utilisation of supporting tools,
  methodologies and technologies that encapsulate all core modules
  covered during training.
 
Application:


Trello Kanban Board

I made this simple overview kanban board at the start of my project to order my steps.

<img width="1403" alt="Screenshot 2022-06-16 at 14 55 40" src="https://user-images.githubusercontent.com/104978039/174086090-bc66aa77-83b4-4813-b77f-91ee4e4270e0.png">



Risk Assessment 

Before starting a new project, it is important to identify, analyse and solve any potential risks that can occur.

<img width="1201" alt="Screenshot 2022-06-13 at 16 26 47" src="https://user-images.githubusercontent.com/104978039/173389191-4013c9b9-19cc-4200-a2bf-907c9fecb923.png">


ERD

For the theme of the project, I chose a topic of interest for me. This being cinema. I decided to create a director database which stores information
about directors. The most basic information being their name and their work. The tables show that a director can have many movies, however a movie can only
have one director. This one to many relationship is illustrated below.

<img width="773" alt="Screenshot 2022-06-15 at 16 04 28" src="https://user-images.githubusercontent.com/104978039/173861060-27d05e7f-4a00-4c45-9035-6c4456462298.png">


CI-DI pipeline

This is a flowchart illustrating the roles of each program in this project. This allow you to see how the programs work together to ensure a safe and working application.

<img width="502" alt="Screenshot 2022-06-16 at 14 39 27" src="https://user-images.githubusercontent.com/104978039/174082880-da131eb4-4315-42d4-aa49-382fab48c054.png">

Application Design Output



Flask Unit Testing

After completing my Flask CRUD application. I added a pytest series of tests to cover my work and ensure it is working as intended.
I created a new folder with a test_app.py file to store all the tests. I added a test database and sample answers to simulate my application and then delete the database to ensure that the live database is unaffected.
You can see the results of my pytest from Visual Studio Code screenshot below.

<img width="1199" alt="Screenshot 2022-06-16 at 14 14 40" src="https://user-images.githubusercontent.com/104978039/174079619-38550b8b-5771-41aa-ae36-4d94df0359e3.png">

Jenkins 

Once the pytest had been passed, the next step is to impliment automatic testing. Via Jenkins, I was able to create a pipeline using my GitHub link. I ran a build on Jenkins and the results are displayed below for this.

<img width="448" alt="Screenshot 2022-06-17 at 12 01 57" src="https://user-images.githubusercontent.com/104978039/174286736-8a9a2117-4a76-4bf7-9a2f-c87dcb9b8728.png">

Once the pytest had been passed, the next step is to impliment automatic testing. Via Jenkins, I was able to create a pipeline using my GitHub link. I ran a build on Jenkins and the results are displayed below for this.


