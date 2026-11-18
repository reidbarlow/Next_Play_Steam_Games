import pandas as pd
import streamlit as st
from google import genai
from google.genai import types

MODEL = "gemini-2.5-flash"

st.set_page_config(page_title="Next Play: Steam Games", page_icon="🎮")


@st.cache_data
def load_games():
    return pd.read_csv("steam_games.csv")


# --- Your three functions ---
def online_players(games, n):
    best = games.sort_values("peak_ccu", ascending=False)
    return best[["name", "peak_ccu"]].head(n)


def average_play_time(games, n):
    longest = games.sort_values("avg_playtime_hours", ascending=False)
    return longest[["name", "avg_playtime_hours"]].head(n)


def top_positive_games(games, n, min_reviews=90):
    filtered = games[games["num_reviews_total"] >= min_reviews]
    best = filtered.sort_values("pct_pos_total", ascending=False)
    return best[["name", "pct_pos_total"]].head(n)


def show_medals(df, unit):
    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    for i, (name, value) in enumerate(zip(df.iloc[:, 0], df.iloc[:, 1])):
        st.write(f"{medals[i]} **{name}**: {value:,} {unit}")


def get_pick(text):
    client = genai.Client(
        api_key=st.secrets["GOOGLE_API_KEY"],
        http_options=types.HttpOptions(timeout=30000),
    )
    response = client.models.generate_content(model=MODEL, contents=text)
    return response.text


games = load_games()

st.title("🎮 Next Play: Steam Games")
st.write("Helps streamers decide what to play next: big crowds, long staying power, and happy players.")

n = st.slider("How many games per category?", 3, 10, 3)

crowds = online_players(games, n)
stay = average_play_time(games, n)
happy = top_positive_games(games, n)

st.subheader("🎮 Crowds: most players online at once")
show_medals(crowds, "players")

st.subheader("⏳ Staying power: longest average play time")
show_medals(stay, "hours")

st.subheader("⭐ Satisfaction: highest positive reviews")
show_medals(happy, "% positive")

st.divider()
st.subheader("🤖 Gemini's pick")
if st.button("What should I stream next?"):
    message = (
        "I am a streamer picking a Steam game to play next.\n"
        "Most players online:\n" + crowds.to_string(index=False) + "\n"
        "Longest play time:\n" + stay.to_string(index=False) + "\n"
        "Highest reviews:\n" + happy.to_string(index=False) + "\n"
        "Pick ONE game considering all factors and explain why in 2 sentences."
    )
    with st.spinner("Thinking..."):
        try:
            st.success(get_pick(message))
        except Exception as e:
            st.error(f"Couldn't get a recommendation: {e}")
