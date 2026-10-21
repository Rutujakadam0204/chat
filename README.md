Real-Time Chat Application

A real-time chat application built with Django and Django Channels, enabling users to exchange messages through WebSockets. 
Chat messages are saved in the database so that message history can be maintained.

Overview

This project demonstrates how to implement real-time communication in a Django application using asynchronous WebSocket consumers and a channel layer.
When a user sends a message, the application saves the message history and broadcasts the message to connected clients in the corresponding chat room.

Tech Stack
Python — Application logic
Django 4.2 — Web framework and ORM
Django Channels 4 — WebSocket communication
Django REST Framework — REST API toolkit included in the project dependencies
WebSockets — Real-time, bidirectional communication
JSON — Message data exchange

Features

Real-time messaging using WebSockets
Room-based message broadcasting
Persistent message history using Django models
Asynchronous WebSocket connection handling
Integration with Django's user model

How It Works

A client establishes a WebSocket connection to a chat room.
Django Channels accepts the connection and adds it to the corresponding room group.
When a message arrives, the consumer extracts the message data.
The message is saved to the database with its associated room and sender.
The channel layer broadcasts the message to the room group.
Connected clients receive the message through the WebSocket connection.
