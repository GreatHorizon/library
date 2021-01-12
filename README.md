# Desktop application for library

Our application is for library management for Universities, Schools, or something like this.
It makes work at the library much easier.
You can run it on Windows, Linux, MacOS.

## Technologies
 * Python + Tkinter
 * PostgreSQL

## To run it you need:
- Install Python
- Install PostgreSQL
- Clone this repository
```
  $ git clone https://github.com/GreatHorizon/library.git
  $ cd library
```
- Install required dependencies: 
```
  $ pip3 intall tkinter
  
  $ pip3 intall psycopg2
  
  $ pip3 intall dotenv
  
  $ pip3 intall tkcalendar
    
  $ pip3 intall datetime
```
- Create database and run library.sql
- Write your database config into .end file
```
  DB_NAME=<your db name>
  USER=<db user name>
  HOST=<localhost>
  PASSWORD=<your password>
```
## Thats all. Good luck!
