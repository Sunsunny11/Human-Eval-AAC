# Human evaluation tool for automated audio captioning
# By Jianyuan Sun, email: jianyuan.sun@dmu.ac.uk
# run commond to generate the web: 1. conda activate humantation 2. streamlit run main.py
import streamlit as st
import pandas as pd
import os
import math

st.set_page_config(page_title="Audio caption Evaluation", layout="centered")
st.title("Human Evaluation Tool for Automated Audio Captioning")
st.markdown(
    "Please rate how well the caption describes the audio clip on a scale from 1 (Not accurate) to 5 (Highly accurate).")

csv_path = "/Volumes/新加卷/CVSSP_Surrey_University/CLAPScore-main/CSV_files/CNN-BART-Clotho-base.csv"
audio_folder = "/Volumes/新加卷/CVSSP_Surrey_University/Audio_captioning_data/data/data/Clotho/waveforms/test/"

df = pd.read_csv(csv_path, header=None, usecols=[0, 1], nrows=150)
#df.columns = ['audio_filename'] + [f'caption_{i}' for i in range(1, len(df.columns))]
df.columns = ['audio_filename', 'caption'] 

# split page setting
samples_per_page = 30
total_samples = len(df)
total_papes = math.ceil(total_samples / samples_per_page)

if "page" not in st.session_state:
    st.session_state.page = 0
    
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("⬅ Previous") and st.session_state.page > 0:
        st.session_state.page -= 1
with col3:
    if st.button("Next ➡") and st.session_state.page < total_papes - 1:
        st.session_state.page += 1

start_idx = st.session_state.page * samples_per_page
end_idx = min(start_idx + samples_per_page, total_samples)

st.markdown(f"## Page {st.session_state.page + 1} of {total_papes}")


#store scores
score_dict = {}
for i in range(start_idx, end_idx):
    row = df.iloc[i]
    st.markdown(f"### Sample {i + 1}")
    
    audio_filename = row['audio_filename'].strip()
    if not audio_filename.endswith(".wav"):
        audio_filename += ".wav"
    audio_path = os.path.join(audio_folder, audio_filename)
    
    if os.path.exists(audio_path):
        st.audio(audio_path, format="audio/wav")
    else:
        st.warning(f"Audio file not found: {audio_path}")
        continue
    
    st.markdown(f"**Caption:** {row['caption']}")
    score = st.radio(
        "Select a score:",
        options=[1, 2, 3, 4, 5],
        key=f"score_{i}",
        index=None
    )
    score_dict[i] = score
user_id = st.text_input("Enter your name or ID (required to save scores)")

if st.button("Submit Ratings"):
    if user_id.strip() == "":
        st.warning("Please enter your name or ID before submitting.")
    else:
        results = df.copy()
        # 填充 score 列（用字典中已有的打分）
        results["score"] = [score_dict.get(i, "") for i in range(len(df))]
        save_path = f"scores_{user_id.strip()}.csv"
        results.to_csv(save_path, index=False)
        st.success(f"Thank you! Your ratings have been saved as '{save_path}'.")