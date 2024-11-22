# Database Schema

## Summoners

Stores summoner information, including API-provided identifiers and geographical location.

- **SummonerID**: `int` [Primary Key, Auto Increment] - Internal unique identifier.
- **PUUID**: `varchar` [Unique, Not Null] - Unique identifier from the API.
- **SummonerName**: `varchar` [Not Null] - Player's in-game username.
- **Level**: `int` [Not Null] - Summoner level.
- **LocationID**: `int` - References the `Location` table.

---

## Location

Stores geographical location details.

- **LocationID**: `int` [Primary Key, Auto Increment] - Unique identifier for the location.
- **Name**: `varchar` - Location name.
- **Abbreviation**: `varchar` - Abbreviation (e.g., NA, EU, BR).

---

## LeagueRank

Stores rank information for summoners.

- **LeagueRankID**: `int` [Primary Key, Auto Increment] - Unique identifier for league rank.
- **SummonerID**: `int` - References the `Summoners` table.
- **LeagueID**: `int` - References the `League` table.
- **QueueID**: `int` - References the `Queue` table.
- **Rank**: `varchar` - Rank (e.g., Gold, Platinum).
- **LeaguePoints**: `int` - Points in current rank.
- **Wins**: `int` - Number of wins.
- **Losses**: `int` - Number of losses.

---

## League

Stores league-specific details.

- **LeagueID**: `int` [Primary Key] - Unique identifier from the API.
- **QueueID**: `int` - References the `Queue` table.
- **LocationID**: `int` - References the `Location` table.
- **Name**: `varchar` - League name.
- **Division**: `varchar` - Division within the league.
- **StartDate**: `date` - Start date of the league division.
- **EndDate**: `date` - End date of the league division.

---

## Queue

Stores queue types (e.g., ranked solo, normal).

- **QueueID**: `int` [Primary Key, Auto Increment] - Unique identifier for queue.
- **Name**: `varchar` - Name of the queue.
- **Description**: `varchar` - Additional context for the queue.

---

## Matches

Stores match-level metadata.

- **MatchID**: `bigint` [Primary Key] - Unique identifier for the match.
- **GameMode**: `varchar` - Type of the game (e.g., CLASSIC).
- **GameType**: `varchar` - Matchmaking type (e.g., MATCHED_GAME).
- **GameCreation**: `timestamp` - When the match was created.
- **GameStart**: `timestamp` - When the match started.
- **GameEnd**: `timestamp` - When the match ended.
- **GameDuration**: `int` - Total match duration in seconds.
- **MapID**: `int` - References the `Maps` table.
- **GameVersion**: `varchar` - Game version during the match.
- **EndOfGameResult**: `varchar` - Final match result (e.g., GameComplete).

---

## Players

Stores details for players participating in matches.

- **PlayerID**: `int` [Primary Key, Auto Increment] - Unique identifier for the participant.
- **MatchID**: `bigint` - References the `Matches` table.
- **SummonerID**: `int` - References the `Summoners` table.
- **TeamID**: `int` - Team identifier (e.g., 100 or 200).
- **ChampionID**: `int` - References the `Champions` table.
- **TeamPosition**: `varchar` - Lane or position played (e.g., TOP, MID).
- **Role**: `varchar` - Specific role (e.g., CARRY, JUNGLE).
- **Win**: `boolean` - Whether the player’s team won the match.

---

## Performance

Stores performance metrics for players in matches.

- **PerformanceID**: `int` [Primary Key, Auto Increment] - Unique identifier for performance record.
- **PlayerID**: `int` - References the `Players` table.
- **Kills**: `int` [Default: 0] - Number of kills.
- **Deaths**: `int` [Default: 0] - Number of deaths.
- **Assists**: `int` [Default: 0] - Number of assists.
- **TotalDamageDealt**: `int` - Total damage dealt.
- **TotalDamageTaken**: `int` - Total damage taken.
- **VisionScore**: `int` - Vision contribution score.
- **GoldEarned**: `int` - Total gold earned by the player.
- **TurretsDestroyed**: `int` [Default: 0] - Number of turrets destroyed.
- **WardsPlaced**: `int` [Default: 0] - Number of wards placed.
- **MinionsKilled**: `int` [Default: 0] - Number of minions killed.
- **NeutralMinionsKilled**: `int` [Default: 0] - Number of neutral creeps killed.

---

## Champions

Stores champion-specific details.

- **ChampionID**: `int` [Primary Key, Auto Increment] - Unique identifier for champions.
- **Version**: `varchar` - Version of champion.
- **Name**: `varchar` - Champion's name.
- **Title**: `varchar` - Champion's title.

---

## Maps

Stores map-specific details.

- **MapID**: `int` [Primary Key, Auto Increment] - Unique identifier for maps.
- **Name**: `varchar` - Name of the map.
