# BritEdge_WebApp_Flexible_Cloud_Deployment_Source_Code

## Overview

BritEdge Job Management is a sample Flask web application designed for students and developers to explore flexible cloud deployment strategies. The application allows users to log in, create, track, and manage job entries (e.g., deliveries, engineering tasks). It demonstrates database flexibility and containerisation for various cloud configurations.

## Tech Stack

- **Flask**: Lightweight Python web framework for the backend.
- **Flask-Login**: User authentication.
- **Flask-SQLAlchemy**: ORM for database interactions.
- **PostgreSQL / SQLite**: Database support (local or cloud).
- **Docker**: Containerisation for easy deployment.
- **python-dotenv**: Environment variable management.

## Cloud Deployment Options

This application is designed for flexible deployment on major cloud platforms, including **Azure** and **AWS**.

- **Azure:**  
  Deploy using Azure App Service, Azure Container Instances, or Azure Web Apps for Containers. You can connect to Azure Database for PostgreSQL or Azure Cosmos DB (PostgreSQL API) for managed database hosting.

- **AWS:**  
  Deploy using AWS Elastic Beanstalk, Amazon ECS (with Docker), or EC2. You can connect to Amazon RDS for PostgreSQL or other managed database services.

**Note:**  
When deploying to any cloud platform, configure your environment variables (such as `SECRET_KEY` and `DATABASE_URL`) using the platform’s environment settings or secrets manager.  
The application is container-ready and can be built and run using Docker on any cloud provider that supports containers.

## How to Use This in the Cloud

- Run on a virtual machine with the inbuilt SQLite database.
- Run on a virtual machine with a separate database instance (e.g., PostgreSQL or Cosmos DB).
- Deploy as a Docker container on Azure or AWS.
- Connect to managed cloud databases for scalability and reliability.

## Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/BritEdge_WebApp_Flexible_Cloud_Deployment_Source_Code.git
   cd BritEdge_WebApp_Flexible_Cloud_Deployment_Source_Code
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Copy `.env.example` to `.env` and set your `SECRET_KEY` and `DATABASE_URL`.

5. **Run the application:**
   ```bash
   flask run
   ```

## Docker Usage

1. **Build the Docker image:**
   ```bash
   docker build -t britedge-app .
   ```

2. **Run the container:**
   ```bash
   docker run --env-file .env -p 5000:5000 britedge-app
   ```

## Example `.env` File

```
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///instance/site.db
```

## Key Features

- User registration and login
- Create, update, and delete job entries
- Track job completion status
- Flexible database backend (SQLite, PostgreSQL, Cosmos DB)
- Ready for containerisation and cloud deployment

## License

This project is for educational purposes and is provided as-is.
