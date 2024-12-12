# **Local Setup Documentation**

This document provides a comprehensive guide for setting up the local development environment for the **Game Stats Tracker** project. It explains how to use Docker to set up PostgreSQL and Cassandra databases, configure environment variables, and test Riot API connections.

---

## **Prerequisites**

Before you begin, ensure you have the following installed:
- **Docker**: [Get Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: Included with Docker Desktop or install it separately if needed.
- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)

---

## **Steps to Set Up the Local Environment**

### **1. Clone the Repository**
If you haven't already cloned the repository:
```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

### **2. Install Package**
Navigate to the root directory and install package
```bash
pip install -e .
```