# Desktop application for library

Our application is for library management for Universities, Schools, or something like this.
It makes work at the library much easier.
You can run it on Windows, Linux, MacOS.

## Technologies
 * Python + Tkinter
 * PostgreSQL

To run it you need:
- Install Python
- Install PostgreSQL
- Install required dependencies: 
```
  tkinter
  
  datetime
  
  psycopg2
  
  dotenv
  
  tkcalendar
```
- Create database and run library.sql
- Write your database config into .end file
```
  DB_NAME=<your db name>
  USER=<db user name>
  HOST=<localhost>
  PASSWORD=<your password>
```
Thats all. Good luck!
