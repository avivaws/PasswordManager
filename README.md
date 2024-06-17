# Password Manager Application

Welcome to the Password Manager Application! This project includes both a server and a client for managing and storing passwords securely.

## Table of Contents

- [Overview](#overview)
- [Server](#server)
  - [Running the Server with Docker](#running-the-server-with-docker)
  - [Running the Server Manually](#running-the-server-manually)
- [Client](#client)
  - [Running the Client with Python](#running-the-client-with-python)
  - [Running the Client Executable](#running-the-client-executable)
- [Dependencies](#dependencies)

## Overview

This project provides a simple yet secure password manager application. It consists of two main components: a server and a client.

- **Server**: Manages password storage and retrieval.
- **Client**: Provides a user interface for interacting with the server to manage passwords.

## Server

There are two ways to run the server:

### Running the Server with Docker

The easiest way to run the server is by using Docker. This method uses the provided `docker-compose.yaml` file to set up both a MongoDB server and the password manager server.

1. Ensure you have Docker and Docker Compose installed on your system.
2. Navigate to the directory containing the `docker-compose.yaml` file.
3. Start the servers as instructed in the Docker documentation.

This will start the MongoDB server on port `27017` and the password manager server on port `8080` within Docker containers.

### Running the Server Manually

If you prefer to run the server without Docker, follow these steps:

1. Ensure MongoDB is installed and running on port `27017`.
2. Navigate to the main directory of the project.
3. Compile the project using Maven.
4. Run the compiled server file to start the password manager server on port `8080`.

## Client

There are two ways to run the client application:

### Running the Client with Python

The client is written in Python and requires a few dependencies to be installed.

1. Ensure you have Python installed on your system.
2. Install the required Python packages: `tk`, `cryptography`.
3. Navigate to the client directory and run the `login.py` file.

### Running the Client Executable

Alternatively, you can run the pre-compiled executable version of the client:

1. Navigate to the `dist` directory.
2. Execute the `login.exe` file.

## Dependencies

- **Server Dependencies**:
  - MongoDB
  - Maven

- **Client Dependencies**:
  - Python
  - `tkinter` (Python package)
  - `cryptography` (Python package)

Ensure all dependencies are installed and properly configured to run the application smoothly.

