# Email campaign manager

This project is a Django-based Email Campaign Manager. It provides a user-friendly interface for managing subscribers, creating and scheduling email campaigns, and handling unsubscriptions.

## Table of Contents

- [Email_campaign_manager](#email_campaign_manager)
  - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Setup](#setup)
    - [Create a Virtual Environment](#create-a-virtual-environment)
    - [Activate the Virtual Environment](#activate-the-virtual-environment)
    - [Install Dependencies](#install-dependencies)
  - [Configuration](#configuration)
  - [Running the Project](#running-the-project)
    - [Run the Django Server](#run-the-django-server)
    - [Run the Celery Worker](#run-the-celery-worker)
    - [Run the Celery Beat](#run-the-celery-beat)
  - [Managing Subscribers and Campaigns](#managing-subscribers-and-campaigns)
  - [Unsubscribing from Emails](#unsubscribing-from-emails)

## Requirements
Before setting up and running the project, ensure you have the following requirements installed:
- **Python:** You'll need Python installed on your system. You can download Python from the [official Python website](https://www.python.org/downloads/).

- **Redis Server:** This project relies on Redis for celery broker. Make sure to install and run Redis on your system. You can download Redis from the [official Redis website](https://redis.io/download) or use a package manager for your operating system.

## Setup

### Create a Virtual Environment

  Before running the project, it's recommended to set up a virtual environment to isolate dependencies:

  ```bash
  # Create a virtual environment (replace 'venv' with your preferred name)
  python -m venv venv
  ```
### Activate the Virtual Environment
  Activate the virtual environment based on your operating system:
  **Windows:**
  ```bash
  venv\Scripts\activate
  ```
  **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```
### Install Dependencies
  Install the project dependencies using the provided requirements.txt file:
  ```bash
  pip install -r requirements.txt
  ```
## Configuration
### Create a .env File
Before running the project, create a `.env` file in the root folder of the project. This file will store following configuration variables.
```env
EMAIL_HOST_USER = your_gmail_address
EMAIL_HOST_PASSWORD = your_gmail_app_key
```
## Running the Project
### Run the Django Server
  To start the Django development serve:
  ```bash
  python manage.py runserver
  ```

### Run the Celery Worker
  To run the Celery worker for background tasks:
  ```bash
  celery -A email_campaign_manager worker -l info
  ```
### Run the Celery Beat
To run the Celery beat scheduler for scheduled tasks (e.g., sending emails at 8 AM):

```bash
celery -A email_campaign_manager beat -l info
```
By default, the project is configured to send emails at 8 AM daily. You can adjust the schedule by modifying the settings in celery.py.

## Managing Subscribers and Campaigns
- You can add subscribers and campaign details using the Django admin panel.

- To access the Django admin panel, run the development server and visit http://localhost:8000/admin/. Log in with your admin credentials.

## Unsubscribing from Emails
To unsubscribe from emails, you can use the following URL pattern:
```bash
GET /email/unsubscribe/your_email_id
```
Replace your_email_id with the actual email address you want to unsubscribe.

