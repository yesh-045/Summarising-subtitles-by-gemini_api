# Subtitle Summarizer

## Description
Subtitle Summarizer is a Python application that summarizes the content of subtitle files into a concise and meaningful paragraph. It utilizes Google's Generative AI to generate a summary that captures the main ideas and key points of the subtitles.

## Features
- Summarizes subtitle files into a meaningful paragraph.
- Removes timestamps and unwanted formatting before summarization.
- Allows customization of summarization parameters.

## Installation
1. **Clone the repository:**
git clone https://github.com/yesh-045/Summarising-subtitles-by-gemini_api.git

## Usage
1. Ensure you have a valid API key for Google's Generative AI.
2. Place your subtitle file (in `.srt` format) in the project directory.
3. Run the script `main.py` and follow the instructions.

## Configuration
- Set up your Google Generative AI API key by editing the `main.py` file and replacing `"YOUR_API_KEY"` with your actual API key.
- You can adjust the summarization parameters such as temperature, top_p, top_k, and max_output_tokens in the `generation_config` dictionary in the `main.py` file.

## Example
```bash
python main.py
