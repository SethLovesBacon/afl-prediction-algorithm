# afl-prediction-algorithm

A machine learning algorithm with the purpose to make predictions on AFL games using features like recent form, where the game is being played, injury list, etc.

## Goal

Predict the outcome of AFL matches (winner, margin, and/or total score) by learning from historical match and betting data.

## Repository layout

```
src/
  alg/    # prediction algorithm / model code
  data/   # match data used for training and evaluation
```

## Data

`src/data/afl_matches_clean.csv` contains historical AFL match records, including:

- Match info: date, kick-off time, home/away teams, venue, whether it was a finals ("play off") game
- Scores: home/away goals, behinds, and total score
- Betting markets: head-to-head odds, line (handicap) odds, and total score (over/under) odds, each with open/min/max/close values

## Status

Early stage — data collection is underway; the prediction model itself has not been implemented yet.
