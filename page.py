import streamlit as st


def pagelink():
  # Set page title
  st.title("find your subtitle here")

  # Add box with title "YouTube Video Link"
  with st.expander("YouTube Video Link"):
    # Add YouTube video link
    st.session_state.youtube_video_link = st.text_input(
        "Enter YouTube Video Link:")
    # Display YouTube video
    if st.session_state.youtube_video_link:
      st.video(st.session_state.youtube_video_link)

  # Add large box
  st.header("Large Box Below")
  # Add text or content inside the large box
  st.write("bla bla")


pagelink()
