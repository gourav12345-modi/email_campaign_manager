# Email campaign management system

This project is a Django-based Email Campaign Manager. It provides a user-friendly interface for managing subscribers, creating and scheduling email campaigns, and handling unsubscriptions.

## Table of Contents

- [Email Campaign](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Setup](#setup)
    - [Create a Virtual Environment](#create-a-virtual-environment)
    - [Activate the Virtual Environment](#activate-the-virtual-environment)
    - [Install Dependencies](#install-dependencies)
  - [Running the Project](#running-the-project)
    - [Run the Django Server](#run-the-django-server)
    - [Run the Celery Worker](#run-the-celery-worker)
    - [Run the Celery Beat](#run-the-celery-beat)
  - [Managing Subscribers and Campaigns](#managing-subscribers-and-campaigns)
  - [Unsubscribing from Emails](#unsubscribing-from-emails)

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

