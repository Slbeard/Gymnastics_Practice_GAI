# Gymnastics Practice Plan Generator

## Project Overview
The Gymnastics Practice Plan Generator is a web-based application built using Streamlit and OpenAI's fine-tuned GPT-3.5 model. It automates the creation of structured gymnastics practice plans based on user input.

## Features
- Generates personalized gymnastics practice plans
- Supports different class durations and skill levels
- Implements a chat-style user interface
- Outputs structured Markdown-formatted practice plans
- Attempts conversion of Markdown tables to DataFrames

## Technologies Used
- **Python**: Main programming language
- **Streamlit**: Web application framework
- **OpenAI API**: Fine-tuned GPT-3.5 model for plan generation
- **Pandas**: Data processing and table handling
- **Requests**: API integration

## Dataset & Model Fine-Tuning
- The model was fine-tuned using a structured JSONL dataset of gymnastics practice plans.
- Multiple iterations were performed to enhance output quality.
- The fine-tuned model ID used: `ft:gpt-3.5-turbo-0125:personal::B6kk1I2j`

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd gymnastics-practice-generator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up API keys:
   - Create a `.env` file and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage
- Open the web app in your browser.
- Enter details about your class (duration, level, events to focus on).
- The AI will generate a structured practice plan in real-time.

## Challenges & Future Improvements
### Challenges:
- Fine-tuning required multiple iterations for better plan accuracy.
- Formatting Markdown tables into DataFrames was complex.

### Future Improvements:
- Enhance UI for better customization options.
- Improve table formatting and export features.
- Expand dataset for more diverse practice plans.

## References
- OpenAI Fine-Tuning Guide
- GenAI Book (Bahree, 2023)
