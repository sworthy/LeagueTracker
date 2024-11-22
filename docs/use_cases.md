# Use Cases

## Purpose

This section outlines the use cases for PostgreSQL and Cassandra in the Game Stats Tracker project. It highlights the strengths of each database type and their roles in the overall architecture.

## PostgreSQL Use Cases

PostgreSQL is used as the relational database solution for storing structured, highly-normalized data. It supports:

1. **Player Profiles**:
   - Store player-specific information like player names, ranks, and regions.
   - Enable complex queries to retrieve player details, filter by rank, or region.
2. **Match Metadata**:
   - Store match-level details like timestamps, durations, and match IDs.
   - Perform joins and aggregations across multiple tables to analyze trends.
3. **Relational Queries**:
   - Joins between tables (e.g., `Players` and `Matches`).
   - Aggregations (e.g., average player KDA, longest match durations).
4. **Data Integrity**:
   - Enforce relationships between entities using foreign keys.
   - Use constraints and validations to ensure data consistency.

## Cassandra Use Cases

Cassandra is used as the NoSQL solution for handling high-volume, write-intensive, and distributed data. It excels in:

1. **Match Event Logs**:

   - Store event-level data such as kills, deaths, and assists during matches.
   - Optimize for high write throughput with low latency.

2. **Aggregated Metrics**:

   - Maintain pre-aggregated statistics like champion win rates or player performance across multiple games.
   - Enable fast retrieval of summaries.

3. **High Availability**:

   - Leverage Cassandra’s replication and distributed architecture to ensure data availability and fault tolerance.

4. **Scalable Read/Write Operations**:
   - Designed for distributed queries with high-speed reads and writes.
