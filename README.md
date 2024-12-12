# League of Legends Game Stats Tracker

## Overview

The Game Stats Tracker project demonstrates workflows using relational (SQL) and NoSQL databases. It integrates data from the Riot Games API to provide insightful statistics and dashboards for League of Legends players and matches.

## Features

- Fetch data from Riot Games API.
- Store and manage data in both SQL (PostgreSQL) and NoSQL (Cassandra) databases.
- Analyze match statistics, player performance, and team objectives.
- Highlight the differences between relational and NoSQL database workflows.

## Documentation

Below are links to the documentation included in this project:

1. [API Endpoints](docs/api_endpoints.md)  
   Details all Riot Games API endpoints used in the project, including parameters and query workflows.

2. [Database Schema (SQL)](docs/database_schema_SQL.md)  
   Defines the SQL schema, relationships, and primary keys.

3. [Database Schema (NoSQL)](docs/database_schema_NoSQL.md)  
   Details the NoSQL schema, optimized for high-read and write throughput.

4. [Project Goals](docs/project_goals.md)  
   Explains the objectives, technologies, and intended outcomes of the project.

5. [Use Cases](docs/use_cases.md)  
   Describes the scenarios, queries, and workflows implemented in the project.

## Next Steps

- Build data pipelines to fetch and store data from Riot Games API.
- Create dashboards and visualizations for the stored data.
- Document setup instructions for database and API integration.

---
## Local Setup with Docker

This project uses Docker to simplify the setup of local PostgreSQL and Cassandra environments.

### Prerequisites
- Docker installed on your system. [Get Docker](https://docs.docker.com/get-docker/)

### Running the Services
1. Navigate to the `Docker/` folder:
2. Run the following command to start both PostgreSQL and Cassandra:
   ```bash
   docker-compose up -d
   ```
---

### Contact

If you have any questions or suggestions, feel free to reach out!
