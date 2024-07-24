import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="Main Page", layout="wide")

    st.title("About Me Page")

    if st.button("Go to Extra"):
        st.session_state.current_page = "second"
        st.experimental_rerun()

    # Apply custom CSS for styling
    st.markdown("""
        <style>
        .app {
            background-color: #f0f2f6;
            padding: 20px;
        }
                
        .header {
            font-family: 'Press Start 2P', fantasy;
            text-align: center;
            color: #333;
            font-size: 2em;
            margin-bottom: 20px;
        }
        .caption {
            font-family: 'Oswald';
            color: black; 
            text-align: center;
            font-size: 0.9em; 
        }
        .centered-text {
            font-family: 'Playfair Display', fantasy;
            text-align: center;
            font-size: 1.2em;
            color: #555;
            margin-bottom: 20px;
        }
        .hidden {
            display: none;
        }
        .photo-grid {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
        }
        .photo {
            flex: 1;
            max-width: 45%;
            margin: 10px;
            border-radius: 10px;
            overflow: hidden;
        }
        .photo img {
            width: 100%;
            height: auto;
        }
        .button-container {
            text-align: center;
            margin-top: 20px;
        }
        .styled-button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .styled-button:hover {
            background-color: #45a049;
        }
        </style>
        """, unsafe_allow_html=True)

    #Header
    st.markdown("<div class='header'>ABOUT ME :D</div>", unsafe_allow_html=True)

    #Center text
    st.markdown("<div class='centered-text'>Hello! I'm Ethan, and I kind of(EMPHASIS ON KIND) like coding games. A few years ago I used to do it on Scratch, but I quickly moved on to python. I also do the bare minimum of graphic design for these said games, as indicated by these pngs below(It doesn't help that I STILL draw these pngs on SCRATCH). The captions below are meant to give you an idea of my personal game-coding timeline.<div>", unsafe_allow_html=True)

    #Photo Gallery
    photos = ["/Users/thaonguyen/Downloads/Platformer/Ball.png", "/Users/thaonguyen/Downloads/Platformer/DemonLeft.png", "/Users/thaonguyen/Downloads/for slides.png", "/Users/thaonguyen/Downloads/Knight & Link.png"]
    cols = st.columns(4)

    captions = [
        "This lazily designed ball character was actually made like 3 years ago, when I started learning pygame after finishing python basics. At this time, I was horrendous at pixel art(I have and still hate it with a fiery passion) However, I kind of just forgot about it, atleast until the previous summer.",
        "The previous summer, I actually remembered the ball character existed, so I used pygame to try to make a funny little platformer. Thus, I figured the best obstacle to parkour over would be devils, which is how I came to draw this in the previous summer. All it did was move slowly around to try to attack the ball, but I thought it was funny so it became the main premise of the simple platformer.",
        "This was midway through the school year, when I proposed the idea of a Scratch game to my English 2. Although it was kind of a bad idea, I was pretty desperate for a good grade and that was the only way, so I ended up coding an entire game (What you're seeing is just the thumbnail) to save my GPA. Obviously, since it was Scratch, it sucked(ESPECIALLY DRAWING SPRITES), but atleast I learned to avoid rushing games in a few days.",
        "This was drawn at the end of year, and it was some excluded content from my friend's game. To clarify, my friend really wanted to make a Zelda fangame for his end-of-year CSAP project, but he wanted ME to draw NPCS for his game. I agreed, and drew around 40 pixel art NPCS. 30 of them were never used, but I got full credit for the 10 so it was worth it. Here, you're seeing both an early Link model, and some prototype art for a Knight NPC, and how my pixel art has atleast improved by a smidge."
    ]

    image_dimensions = (300, 280)

    for col, photo, caption in zip(cols, photos, captions):
        with col:
            image = Image.open(photo)
            image = image.resize(image_dimensions)
            st.image(image, use_column_width=True)
            st.markdown(f"<p class='caption'>{caption}</p>", unsafe_allow_html=True)

    # Initialize session state
    if 'button_clicked' not in st.session_state:
        st.session_state.button_clicked = False

    # Button and conditional rendering
    if not st.session_state.button_clicked:
        if st.button("Click Me For a Surprise!"):
            st.session_state.button_clicked = True
            st.experimental_rerun()
        st.write("(The voices in your head tell you to click the button.)")
    else:
        st.write("HAHA YOU GOT JUMPSCARED BY ME AND MY PLUSHIES! Not my proudest picture though...;-;")
        st.image("/Users/thaonguyen/Desktop/JUMPSCARE.png", use_column_width=True)
    

if __name__ == "__main__":
    main()
