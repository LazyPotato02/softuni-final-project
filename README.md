# softuni-final-project

Color Pallets
#00E6F6
#1F6CAB
#082A3A
#FFFFFF

General Requirements

Your Web application should use the following technologies, frameworks, and development techniques:

· The application must be implemented using Django Framework

    o The application must have at least 10 web pages:

        § Can be created using function-based views or/and class based-views;

        § At least 5 of them must be class-based views.

    o The application must have at least 5 independent models (models created by extending, inheritance, and one-to-one relation is considered one model).

    o The application must have at least 5 forms.

    o The application must have at least 5 templates.

· Use PostgreSQL as a Database Service

    o Optionally, you can use multiple storages (including PostgreSQL), e.g., files, other Web services, databases (e.g., MySQL/MariaDB/Oracle / etc.)

· Use Django Template Engine or make the Front-End using JavaScript.

· Templates (your views must return HTML files) - the same template could be re-used/ used multiple times (with the according to adjustments, if such needed).

· Implement Web Page Design based on Bootstrap / Google Material Design, or design your own.

· The application must have login/register/logout functionality.

· The application must have a public part (A part of the website, which is accessible by everyone - un/authenticated users and admins).

· The application must have a private part (accessible only by authenticated users and admins).

· The application must have a customized admin site (accessible only by admins):

    o Add at least 5 custom options (in total) to the admin interface (e.g., filters, list display, ordering, etc.).

· Unauthenticated users (public part) have only 'get' permissions, e.g., landing page, details, about page, and login/ register 'post' permissions.

· Authenticated users (private part) have full CRUD for all their created content.

· Admins - at least 2 groups of admins:

    o One must have permission to do full CRUD functionalities (superusers);

    o The other/s have permission to do limited CRUD functionalities (staff).

    o User roles could be manageable from the admin site.

    o Make sure the role management is secured and error-safe.

· Implement Exception Handling and Data Validation to avoid crashes when invalid data is entered (both client-side and server-side)

    o When validating data, show appropriate messages to the user