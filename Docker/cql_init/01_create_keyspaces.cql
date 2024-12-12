CREATE KEYSPACE IF NOT EXISTS LeagueTracker
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE KEYSPACE IF NOT EXISTS GameAnalytics
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE KEYSPACE IF NOT EXISTS Logging
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
