import streamlit as st
import requests

def fetch_github_events():
    url = "https://api.github.com/events"
    response = requests.get(url)

    if response.status_code == 200:
        events = response.json()
        return events
    else:
        return {"error": f"Failed to fetch data: {response.status_code}"}

def main():
    st.set_page_config(page_title="Extra Page", layout="wide")

    st.title("Extra Page")
    st.write("Here is a random video of me gaming in Decaying Winter on Roblox. I have spent countless hours suffering in that game, and got mad plenty of times. Let's just say I uhh... let out my anger on a hostile NPC.")

    video_url = "https://www.youtube.com/watch?v=Jfq-vJtXy20"
    
    st.title("funny video because why not")
    
    # Embed the YouTube video
    st.video(video_url, format="video/mp4")

    owner = "streamlit"
    repo = "streamlit"

    events = fetch_github_events()

    if "error" not in events:
        # Display a summary of each event
        st.write("This page shows recent events on GitHub. I just formatted the data so it would look nicer.")
        for event in events:
            st.write(f"**Type:** {event.get('type')}")
            st.write(f"**Repo:** {event['repo'].get('name')}")
            st.write(f"**Actor:** {event['actor'].get('login')}")
            st.write(f"**Created At:** {event.get('created_at')}")
            st.write("---")
    else:
        st.write(events["error"])
    
    if st.button("Back to Main Page"):
        st.session_state.current_page = "main"
        st.experimental_rerun()

if __name__ == "__main__":
    main()


