import re
import google.generativeai as genai

genai.configure(api_key="Your-API-Key")

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config)

convo = model.start_chat(history=[])

def remove_timestamps(subtitles):
    """
    Removes timestamps from subtitle text.

    Args:
        subtitles: A string representing the subtitles content.

    Returns:
        clean_subtitles: A string with timestamps removed.
    """
    # Define the regular expression pattern to match timestamps
    timestamp_pattern = r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}'
    
    
    clean_subtitles = re.sub(timestamp_pattern, '', subtitles)
    
    return clean_subtitles

def summarize_text(prompt: str) :
    """
    Summarizes the given prompt using Generative AI.

    Args:
        prompt: A string representing the prompt for summarization.

    Returns:
        summary: A string representing the summarized text.
    """
    summary = ""
    try:
        response = convo.send_message(prompt)
        if response:
            summary = convo.last.text
    except Exception as e:
        print("Error:", e)
    return summary

def summarize_file(file_path):
    """
    Summarizes the content of a file.

    Args:
        file_path: A string representing the path to the file that needs to be summarized.

    Returns:
        None
    """
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            if file_path.endswith('.srt'):  
                file_content = remove_timestamps(file_content)
            file_content="Given the provided text, summarize it into a concise and meaningful paragraph, ensuring that the length of the summary is approximately half of the total number of lines in the input text. The summary should capture the main ideas and key points of the text while maintaining coherence and clarity."+file_content
            summary = summarize_text(file_content)
            if summary:
                print("Summarized text:")
                print(summary)
    except FileNotFoundError:
        print("Error: File not found")

file_path = "file.srt"  
summarize_file(file_path)
