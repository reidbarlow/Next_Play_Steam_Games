# Next Play Steam Games

A small Python app helps a player which game to play and have the best expierence.

> A course project for MIST 4600: Computer Programming in Business at the University of Georgia's Terry College of Business (Fall 2026).

## Problem
A player wants to pick a game to play but is overwhelemed with options. They want a game that they will have a good time playing and want to go back to. 

**My app pulls data on active player counts, average playtime, and user reviews, then ranks games so streamers can pick titles with engaged communities and strong audience appeal.**

## What it does
My app answers three sub-questions:
1. **Crowds:** Which games have many players online at once? My app returns most players each game has.
2. **Staying Power:** Which game keeps players playing longest? My app returns the apps with the longest average playing times.
3. **Satisfaction:** What games have the largest positive percentage of user reviews? My app returns what apps have the most positive reviews.

**Together:** Gemini recommends a game to play based on the top 3 games for crowds, staying power, and satisfaction.

## Data
The [Steam Games Dataset](https://www.kaggle.com/datasets/artermiloff/steam-games-dataset) on Kaggle, collected in March 2025. The dataset is shared under the MIT License by its creator, artermiloff. This repo uses `steam_games.csv`, a smaller file made for the course: the 1,000 games with the most reviews.

## Built with
- Python and pandas, in Google Colab
- Google Gemini API through the google-genai library: labeling how each game is played
  
## How to run it
1. Click **Open in Colab** above, or open steam_games.ipynb from this repository in Google Colab.
  
2. Put steam_Games.csv (in this repository) in your Google Drive, in the same folder as the notebook.
   
3. Get a free Gemini API key at aistudio.google.com (use a personal Gmail account). In Colab, click the key icon on the left (Secrets), add a secret named GOOGLE_API_KEY with your key as its value, and turn on **Notebook access.**
   
4. Choose **Runtime → Run all**. Allow access to Google Drive when Colab asks. The last cell takes about 30 seconds.

Note: Never type your Gemini key into the notebook.

## Example output
**Sub-question 1:**

🎮 CROWDS: most players online at once

🥇 Counter-Strike 2 - 1212356 players

🥈 Monster Hunter Wilds - 703236 players

🥉 PUBG: BATTLEGROUNDS - 616738 players

**Sub-question 2:**

⏳ STAYING POWER: longest average play time

🥇 FINAL FANTASY XIV Online - 837.6 hours

🥈 Dota 2 - 717.2 hours

🥉 Counter-Strike 2 - 553.2 hours

**Sub-question 3:**

⭐ SATISFACTION: highest positive reviews

🥇 HoloCure - Save the Fans! - 99 % positive

🥈 Cats Hidden in Paris - 98 % positive

🥉 VPet-Simulator - 98 % positive

**Recommendation for the player from Gemini:**

🤖 GEMINI'S PICK
I recommend streaming **Counter-Strike 2** because its massive peak concurrent player count of over 1.2 million guarantees an instantly engaged, highly searchable audience. Additionally, its proven staying power—backed by an average playtime of 553 hours and universal recognition—makes it a reliable, high-retention staple for long-term community building.

## AI Use Disclosure:
I used Claude to help me come up with a creative way to display the top 3 games for each one of my sub-questions. I wrote the code entirely myself, except for the creative title above each of the podium's. I understand every line I wrote.

**I used AI tools:** Yes

**Tools:** Claude

**What I asked:** come up with a creative way to display the top 3 games for each one of my sub-questions.

**What I added, changed, or fixed in the AI's output:** I altered the way it presented the top 3 games for each sub-question.

**What I designed and wrote entirely myself:** the project idea, the sub-question functions, the use of gemini as my tool, and the recommendation.

**I understand every line of code I am submitting:** Yes

## Author
Reid Barlow · MIST 4600, Fall 2026
