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



CICD pipeline

This is a flowchart illustrating the roles of each program in this project. This allow you to see how the programs work together to ensure a safe and working application.

<img width="502" alt="Screenshot 2022-06-16 at 14 39 27" src="https://user-images.githubusercontent.com/104978039/174082880-da131eb4-4315-42d4-aa49-382fab48c054.png">



Flask Unit Testing

After completing my Flask CRUD application. I added a pytest series of tests to cover my work and ensure it is working as intended.
I created a new folder with a test_app.py file to store all the tests. I added a test database and sample answers to simulate my application and then delete the database to ensure that the live database is unaffected.
You can see the results of my pytest from Visual Studio Code screenshot below.

<img width="1199" alt="Screenshot 2022-06-16 at 14 14 40" src="https://user-images.githubusercontent.com/104978039/174079619-38550b8b-5771-41aa-ae36-4d94df0359e3.png">



Jenkins 

Once the pytest had been passed, the next step is to impliment automatic testing. Via Jenkins, I was able to create a pipeline using my GitHub link. I ran a build on Jenkins and the results are displayed below for this.

<img width="448" alt="Screenshot 2022-06-17 at 12 01 57" src="https://user-images.githubusercontent.com/104978039/174286736-8a9a2117-4a76-4bf7-9a2f-c87dcb9b8728.png">

Once the pytest had been passed, the next step is to impliment automatic testing. Via Jenkins, I was able to create a pipeline using my GitHub link. I ran a build on Jenkins and the results are displayed below for this.



Application design output

This section shows my CRUD application with all the pages when browsing through.

Home page

<img width="1439" alt="Screenshot 2022-06-17 at 12 25 25" src="https://user-images.githubusercontent.com/104978039/174289893-c0e5d122-80ed-482a-8e05-e47b03829df4.png">

Add director Page

<img width="1440" alt="Screenshot 2022-06-17 at 12 25 35" src="https://user-images.githubusercontent.com/104978039/174289956-00f4fa33-c605-4a4f-89f0-0c67de0ad107.png">

Add movie and assign director page

<img width="1440" alt="Screenshot 2022-06-17 at 12 25 45" src="https://user-images.githubusercontent.com/104978039/174290032-15d58928-48ea-4884-b58f-317a77bce193.png">

Read page

I added many names to this list.

<img width="1440" alt="Screenshot 2022-06-17 at 12 25 56" src="https://user-images.githubusercontent.com/104978039/174290114-8d23eaea-9ec3-4fd1-8a15-ffe9938b0c32.png">

The next screenshot shows the delete function at work. It has removed a director from this list.

<img width="1440" alt="Screenshot 2022-06-17 at 12 26 07" src="https://user-images.githubusercontent.com/104978039/174290224-f638093e-0cad-4af2-ac68-dc0173a5d03a.png">

The next and final screenshot shows the update function. It allows you to amend the directors name.

<img width="1440" alt="Screenshot 2022-06-17 at 12 26 24" src="https://user-images.githubusercontent.com/104978039/174290324-f4623cd3-0b30-4996-9f8e-e0703c90b248.png">

Known Application issues

In terms of the current build of this application, there are no bugs or issues when navigating.



Challenges Faced

As a notice in this industry, everything I learnt during this project was for the first time. I faced many challenges in python, flask, HTML and Jenkins code. I used my time to research and study techniques and solutions to the problems I ran into.

I really wanted this project to show that regardless of my lack of experience in this arena, I am still able to overcome any challenges and provide a rudamentary yet fully functioning application.

The biggest challenge that I faced was Jenkins. Specifically, Jenkis deployment. After spending hours and researching fixes. I was not able to successfully deploy my application via Jenkins in the given time. I would like to assure you that I will be spending a lot more time focusing on this topic and making sure I can master it. I believe eventhough I could not get past this hurdle now, in due time, I will have expanded my knowledge of this topic and learned how to impliment this into my application.

However, as the automatic testing and the webhook from Jenkins was successful as seen above, my application successfully runs from a virtual machine instance without fault.



Possible Future Updates

-Further developing this application, I would impliment a more sophisticated interface to make it more visually pleasing.
-I would look to add an additional update function to edit movie names. 
-Taking it even further by adding profiles to both classes. E.g. adding movie information such as runtime, budget, box office.
-Also, in regards to testing, I would aim to achieve a full 100% coverage on my already successful unit tests.
-Finally, overcome my biggest challenge, Jenkins deployment. I will definitely work on this in my free time to ensure I am improving myself and my knowledge of this industry.



Conclusion

To summarise, I would like to say that I am pleased with the outcome of this project. The dark cloud of the deployement failure will definitely shade me until I master that topic. However, based on my past experience being none, I believe that I have proved that I am open to learn and go the extra step to align myself with my other more experienced colleagues. I have an excellent understanding of Flask and I am excited about learning more about it. This is exactly the reason I accepted this role. I loved working on this project and seeing the little intricate details of these languages and how they work together has sparked a big interest for me and I am looking forward to developing my knowledge and challenging myself to exceed expectations especially for an author with no prior experience. I do believe that with my ambitioin and drive and defiinitely more experience, I ican prove myself to be a successful DevOps Engineer.
