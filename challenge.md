Backend Challenge: Task Management System


This project is a task management system built with Django and Django Rest Framework (DRF). It lets users manage tasks and labels, with the ability to create, update, delete, and view tasks or simply CRUD.


Features
- User Authentication: Users need to log in to manage their tasks.
- Task & Label Management: Users can create, view, edit, and delete tasks and labels.
- Admin Panel: For staff users to manage all tasks and labels.
- API Access: Tasks and labels are managed via API.


How to Set Up the Project Locally
1. Clone the Project (Optional)
If you're using Git, clone the repository to your local machine: by doing this command -> git clone <repository-url>
                                                                                       -> cd backend-challenge


2. Create a Virtual Environment -> python -m venv env

 - For Windows -> .\env\Scripts\Activate
 - For Mac or Linux -> source env/bin/activate


3.  Install Project Dependencies -> pip install -r requirements.txt


4. Set Up the Database -> python manage.py migrate


5. Create a Superuser/isStaff (note* that only Superusers can see the others tasks or create,update,delete.)

   To access the Django admin panel, create a superuser by running -> python manage.py createsuperuser
   

6. Start the Server following this command-> python manage.py runserver
   The server will start running at http://127.0.0.1:8000/ -- by default I put the djangorestframework login page in order to log in to your tasks.


7. Access the API
   
   You can access the API endpoints in your browser or API tools like Postman:


Tasks: http://127.0.0.1:8000/api/tasks/
Labels: http://127.0.0.1:8000/api/labels/

8. Testing
   
   To run tests for the project, use this command -> python manage.py test



--File Structure--

task_management_system/ -> The Django project directory with settings and URLs.


tasks/ -> The app where the models, views, serializers, and URLs for tasks and labels are located.


manage.py -> The command-line tool for running the project.


requirements.txt -> List of required packages to run the project.
