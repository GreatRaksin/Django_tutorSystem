# Django tutor management system

<p>This web app allows you to create and conveniently manage teachers of a training center / school / university. </p>
<p>There is a filter on the main page of the application that allows you to filter teachers by branch and subject. The functionality is being finalized.</p>

<hr>
<p>If you want to test this app, you need:</p>

* Open your terminal and run <code>git clone https://github.com/GreatRaksin/Django_tutorSystem.git</code>
* Then <code>pip install -r reqirements.txt</code>
* Add environment variables <code>SECRET_KEY</code> and variables for DB user (if you want to use MySQL or PostgreSQL databases instead of SQLite)
* Run <code>python manage.py makemigrations</code>
* Then run <code>python manage.py migrate</code>
* Enjoy!