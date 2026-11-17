# Next Play Steam Games

My app helps streamers decide what game to play and have the best experience by evaluating games with other players playing, what game keeps players playing the longest, and the games with the best reviews.

> A course project for **MIST 4600: Computer Programming in Business** at the University of Georgia's Terry College of Business (Fall 2026).

## Problem
Next Play Steam Games helps streamers decide what to play next. It pulls data on active player counts, average playtime, and user reviews, then ranks games so streamers can pick titles with engaged communities and strong audience appeal.

## What it does
My app answers three questions:
1. **Crowds:** Which games have many players online at once?
2. **Staying Power:** Which game keeps players playing longest?
3. **Satisfaction:** What games have the largest positive percentage of user reviews?

## Data
The [Steam Games Dataset](https://www.kaggle.com/datasets/artermiloff/steam-games-dataset) on Kaggle, collected in March 2025. The dataset is shared under the MIT License by its creator, artermiloff. This repo uses `steam_games.csv`, a smaller file made for the course: the 1,000 games with the most reviews.

## Built with
- Python and pandas, in Google Colab
- Coming soon: LLM API (Gemini)

## How to run it
Download the steam games file in your Google Drive. Add your gemini key named "GOOGLE_API_KEY". 

## Example output
🤖 GEMINI'S PICK
I recommend streaming **Counter-Strike 2** because its massive peak concurrent player count of over 1.2 million guarantees an instantly engaged, highly searchable audience. Additionally, its proven staying power—backed by an average playtime of 553 hours and universal recognition—makes it a reliable, high-retention staple for long-term community building.

## AI Use Disclosure
I used Claude to help me come up with a creative way to display the top 3 games for each one of my sub-questions. I wrote the code entirely myself, except for the creative title above each of the podium's. I understand every line I wrote.

## Author
Reid Barlow
