# Database Schema

## Summoner Profiles

Stores basic summoner information.

- **SummonerID**: `UUID` [Primary Key] - Unique identifier for the summoner.
- **PUUID**: `TEXT` - Unique identifier from the API.
- **SummonerName**: `TEXT` - Player's in-game username.
- **ProfileIcon**: `INT` - Profile icon ID from API.
- **Level**: `INT` - Summoner level.
- **Location**: `TEXT` - Geographical location.

---

## League Rankings

Stores a summoner's rank details across multiple queues and leagues.

- **SummonerID**: `UUID` - References the `SummonerProfiles` table.
- **QueueID**: `TEXT` - Queue type (e.g., Ranked Solo).
- **LeagueID**: `TEXT` - League identifier.
- **Rank**: `TEXT` - Rank (e.g., Gold, Platinum).
- **LeaguePoints**: `INT` - Points in the current rank.
- **Wins**: `INT` - Number of wins.
- **Losses**: `INT` - Number of losses.
- **Veteran**: `BOOLEAN` - Indicates if the player is a veteran.
- **FreshBlood**: `BOOLEAN` - Indicates if the player is new to the division.
- **HotStreak**: `BOOLEAN` - Indicates if the player is on a hot streak.
- **Inactive**: `BOOLEAN` - Indicates if the player is inactive.

**Primary Key**: (`SummonerID`, `QueueID`, `LeagueID`)

---

## Matches

Stores metadata for matches.

- **MatchID**: `UUID` [Primary Key] - Unique identifier for the match.
- **GameMode**: `TEXT` - Type of the game (e.g., CLASSIC).
- **GameType**: `TEXT` - Matchmaking type (e.g., MATCHED_GAME).
- **GameCreation**: `TIMESTAMP` - When the match was created.
- **GameStart**: `TIMESTAMP` - When the match started.
- **GameEnd**: `TIMESTAMP` - When the match ended.
- **GameDuration**: `INT` - Total match duration in seconds.
- **MapID**: `UUID` - Identifier for the game map.
- **GameVersion**: `TEXT` - Game version during the match.
- **QueueID**: `TEXT` - References the queue type.
- **EndOfGameResult**: `TEXT` - Final match result (e.g., GameComplete).

---

## Match Teams

Stores team details within a match.

- **MatchID**: `UUID` - References the `Matches` table.
- **TeamID**: `INT` - Team identifier (e.g., 100 or 200).
- **Win**: `BOOLEAN` - Whether the team won the match.
- **FirstBlood**: `BOOLEAN` - Whether the team achieved first blood.
- **FirstTower**: `BOOLEAN` - Whether the team destroyed the first tower.
- **TeamPosition**: `TEXT` - Position of the team (e.g., Red or Blue).

**Primary Key**: (`MatchID`, `TeamID`)

---

## Team Objectives

Stores objectives achieved by teams during a match.

- **MatchID**: `UUID` - References the `Matches` table.
- **TeamID**: `INT` - References the `MatchTeams` table.
- **ObjectiveType**: `TEXT` - Type of objective (e.g., Baron, Dragon, Tower).
- **Kills**: `INT` - Number of times this objective was achieved by the team.
- **First**: `BOOLEAN` - Whether the team achieved the first of this objective.
- **ObjectiveValue**: `TEXT` - Additional metadata for objectives (e.g., dragon type).

**Primary Key**: (`MatchID`, `TeamID`, `ObjectiveType`)

---

## Team Bans

Stores champion bans for each team.

- **MatchID**: `UUID` - References the `Matches` table.
- **TeamID**: `INT` - References the `MatchTeams` table.
- **PickTurn**: `INT` - The pick turn when the ban was made.
- **ChampionID**: `UUID` - References the `Champions` table.

**Primary Key**: (`MatchID`, `TeamID`, `PickTurn`)

---

## Match Participants

Stores participant data for each match.

- **MatchID**: `UUID` - References the `Matches` table.
- **SummonerID**: `UUID` - References the `SummonerProfiles` table.
- **TeamID**: `INT` - References the `MatchTeams` table.
- **ChampionID**: `UUID` - Champion played during the match.
- **Role**: `TEXT` - Specific role (e.g., CARRY, JUNGLE).
- **TeamPosition**: `TEXT` - Lane or position played (e.g., TOP, MID).
- **IndividualPosition**: `TEXT` - Player’s individual position.
- **Win**: `BOOLEAN` - Whether the player’s team won the match.
- **SummonerSpell1ID**: `INT` - First summoner spell used.
- **SummonerSpell2ID**: `INT` - Second summoner spell used.
- **ProfileIcon**: `INT` - Player’s profile icon.

**Primary Key**: (`MatchID`, `SummonerID`)

---

## Player Performance

Stores detailed player performance in a match.

- **MatchID**: `UUID` - References the `Matches` table.
- **SummonerID**: `UUID` - References the `SummonerProfiles` table.
- **Kills**: `INT` - Number of kills.
- **Deaths**: `INT` - Number of deaths.
- **Assists**: `INT` - Number of assists.
- **TotalDamageDealt**: `INT` - Total damage dealt.
- **TotalDamageTaken**: `INT` - Total damage taken.
- **VisionScore**: `INT` - Vision contribution score.
- **GoldEarned**: `INT` - Total gold earned by the player.
- **TurretsDestroyed**: `INT` - Number of turrets destroyed.
- **WardsPlaced**: `INT` - Number of wards placed.
- **WardsKilled**: `INT` - Number of wards killed.
- **MinionsKilled**: `INT` - Number of minions killed.
- **NeutralMinionsKilled**: `INT` - Number of neutral creeps killed.
- **DamageToChampionsMagic**: `INT` - Magic damage dealt to champions.
- **DamageToChampionsPhysical**: `INT` - Physical damage dealt to champions.
- **DamageToChampionsTrue**: `INT` - True damage dealt to champions.

**Primary Key**: (`MatchID`, `SummonerID`)

---

## Player Items

Stores items equipped by players during a match.

- **MatchID**: `UUID` - References the `Matches` table.
- **SummonerID**: `UUID` - References the `SummonerProfiles` table.
- **Slot**: `INT` - Item slot number (0 to 6).
- **ItemID**: `UUID` - References the `Items` table.

**Primary Key**: (`MatchID`, `SummonerID`, `Slot`)

---

## Champions

Stores champion data.

- **ChampionID**: `UUID` [Primary Key] - Unique identifier for champions.
- **Version**: `TEXT` - Version of the champion.
- **Name**: `TEXT` - Champion's name.
- **Title**: `TEXT` - Champion's title.

---

## Items

Stores item data.

- **ItemID**: `UUID` [Primary Key] - Unique identifier for items.
- **Version**: `TEXT` - Version of the item.
- **Name**: `TEXT` - Item name.

---

## Maps

Stores map information.

- **MapID**: `UUID` [Primary Key] - Unique identifier for maps.
- **Name**: `TEXT` - Name of the map.

---

## Game Versions

Tracks game version details.

- **VersionID**: `UUID` [Primary Key] - Unique identifier for game version.
- **Version**: `TEXT` - Game version (e.g., 12.19.1).
- **ReleaseDate**: `DATE` - Release date of the version.

---
