from setuptools import setup, find_packages

setup(
    name="LeagueTracker",
    version="0.1",
    packages=find_packages(),  # Automatically find 'python' and subpackages
    include_package_data=True,  # Include non-code files like .env or data
    install_requires=[  # Add dependencies here
        "requests",
        "python-dotenv",
        "psycopg2",  # If needed for PostgreSQL
        "cassandra-driver"  # If needed for Cassandra
    ],
    entry_points={  # Optional: Add scripts for easy execution
        "console_scripts": [
            "leaguetracker=python.__main__:main",
        ],
    },
    python_requires=">=3.8",  # Specify minimum Python version
)
