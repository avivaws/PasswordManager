this project is about a simple password manager application.
here we have the client and the server

the server: 
  we have 2 ways to run the server.
  the first easy way to run the server is using docker with docker-compose.yaml supplied
  it will open a mongodb server on port 27017 and the password manager server on port 8080
  and run them both in a docker container.
  
  the second way is to run a mongoDb server on port 27017.
  then run mvn compile on the main dir and run the file created this will run the password-manager server on port 8080.

the client:
  the client is python based, you can run login.py python file but it requires the tkinkter and cryptography packages.
  
  you can as well go into dist dir and run login.exe.
