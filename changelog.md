# Changelog

## Version History

### [Unreleased]

- Initial steps in progress.

---

### [0.1.0] - 2024-11-21

#### Added

- **GitHub Repository**

  - Organized `docs/` folder with Markdown files:
    - `api_endpoints.md`
    - `database_schema_NoSQL.md`
    - `database_schema_SQL.md`
    - `project_goals.md`
    - `use_cases.md`
  - Initial `README.md` with links to all documentation.

- **Database Schema Designs**

  - Finalized relational (SQL) schema in `database_schema_SQL.md`.
  - Finalized NoSQL schema in `database_schema_NoSQL.md`.
  - Exported diagrams of both schemas as PNGs for documentation.

- **API Reference**
  - Documented Riot API endpoints, including paths, parameters, and workflows, in `api_endpoints.md`.

#### Summary

Phase 1 established a strong foundation for the project with comprehensive planning, documentation, and schema designs. The GitHub repository is fully organized for future development.

---

### [Future Versions]

#### Planned

- **Setup of Core Tools and Technologies**

  1. **Programming Languages**

     - Python: For API integration, ETL scripts, and orchestration.
     - SQL: For relational database interaction and queries (PostgreSQL).
     - CQL: For NoSQL database interaction and queries (Cassandra).

  2. **Data Pipeline and Orchestration**

     - Apache Airflow (Free): For managing workflows and scheduling ETL jobs.
     - DBT (Free Tier): For data transformation and modeling.
     - PySpark (Free): For distributed data processing, mimicking Databricks.

  3. **Cloud Infrastructure (AWS Free Tier)**

     - Amazon RDS: Use PostgreSQL for relational database setup.
     - Amazon S3: Store raw API responses or preprocessed data.
     - AWS Lambda: Automate tasks like triggering API calls or loading data.
     - Amazon EC2: Host orchestration tools like Airflow.

  4. **Data Visualization**
     - Tableau Public (Free): Build visually appealing reports (optional).

- **Build Initial API Pipeline**

  - Fetch summoner data using Riot Games API.
  - Store raw data in Amazon S3 for archival purposes.
  - Process and load data into Cassandra and PostgreSQL.

- **Database Integration**

  - Implement database schemas in PostgreSQL and Cassandra.
  - Validate data consistency and queries across both database types.

- **Visualization Dashboards**
  - Create interactive dashboards using Tableau Public or another free tool to analyze:
    - Player statistics
    - Team performance
    - Match outcomes
