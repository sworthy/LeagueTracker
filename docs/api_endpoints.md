# Riot Games API Endpoints

## Authorization

### Header:

- `X-Riot-Token`: Your API key.

### Rate Limits

- 20 Requests every 1 second
- 100 requests every 2 minutes
- Rate limits enforced per routing value (e.g., na1, euw1, americas)

---

## Routing Values

### Region-Based Routing:

- **Region**: E.g., `americas.api.riotgames.com`

### Platform-Based Routing:

- **Platform**: E.g., `na1.api.riotgames.com`

---

## League-Exp-V4

### Endpoint: Get Ranked Player List

**URL**: `/lol/league-exp/v4/entries/{queue}/{tier}/{division}`

#### Path Parameters:

- `queue`: Type of ranked queue (e.g., `RANKED_SOLO_5x5`).
- `tier`: Ranked tier (e.g., `Iron`, `Bronze`, `Silver`, `Gold`, `Platinum`, `Emerald`, `Diamond`, `Master`, `Grandmaster`, `Challenger`).
- `division`: Ranked division within the tier (e.g., `I`, `II`, `III`, `IV`).

---

## Match-V5

### Endpoint: Get Match History

**URL**: `/lol/match/v5/matches/by-puuid/{puuid}/ids`

#### Path Parameters:

- `puuid`: Unique identifier for the summoner.

#### Query Parameters:

- `startTime`: Epoch timestamp in seconds. Matches must be after this time.
- `endTime`: Epoch timestamp in seconds. Matches must be before this time.
- `queue`: Filter by queue ID.
- `type`: Filter by type of match (e.g., `Ranked`, `Normal`).
- `start`: Start index for pagination (default: 0).
- `count`: Number of match IDs to return (default: 20; max: 100).

---

### Endpoint: Get Match Details

**URL**: `/lol/match/v5/matches/{matchId}`

#### Path Parameters:

- `matchId`: Unique identifier for the match.

---

## Data Dragon

### Endpoint: Static Data Assets

**URL**: Downloadable tarball (.tgz)

#### Notes:

- Centralized game data and assets for champions, items, runes, summoner spells, and profile icons.
- Updated manually after each patch.

---
