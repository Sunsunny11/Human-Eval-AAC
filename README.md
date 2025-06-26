# Human-Eval-AAC

## Human Evaluation Tool for AAC 

This Streamlit app lets human annotators rate the relevance and accuracy of automatically generated audio captions.  
The interface paginates **150 audio–caption pairs** into **5 pages (30 items per page)**, plays each `.wav` file, shows its caption, and collects a 1–5 Likert score.  When the annotator finishes, all ratings are written to a CSV file for later statistical analysis (Pearson ρ, Kendall τ, Krippendorff’s α, etc.).

### Features
- 🔊 Inline audio player for every sample  
- 📝 One-click 1–5 scoring radio buttons (no default selection)  
- 📄 Automatic pagination (30 items per page)  
- 💾 Ratings saved as `scores_<user_id>.csv` with a single click  
- ✔️ Designed for multi-annotator studies; each sample can be rated by 3–5 people

### Installation
```bash
# clone the repo
git clone https://github.com/<your-username>/Human-Eval-AAC.git
cd Human-Eval-AAC

### Running
streamlit run main.py
