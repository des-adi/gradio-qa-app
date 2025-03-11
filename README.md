# Gradio-based CSV Question Answering and Visualization Application

## Overview
This is a Gradio-based application that allows users to upload a CSV file, ask questions about its contents, and visualize the data. The application uses a local Large Language Model (LLM) powered by Ollama and Pydantic AI to generate answers and supports graph plotting within the Gradio interface.

---

## Features
- **CSV File Handling**:
  - Upload and parse CSV files.
  - Validate CSV file format and handle errors gracefully.
- **Question Answering**:
  - Ask textual and numerical questions about the CSV data.
  - Generate answers using a local LLM (Llama 3.1 8B or smaller).
- **Graph Plotting**:
  - Generate graphs (e.g., histograms, scatter plots) based on the CSV data.
  - Display visualizations directly within the Gradio interface.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/des-adi/gradio-qa-app.git
   cd gradio-qa-app
2. Install the required dependencies:
pip install gradio pandas matplotlib ollama pydantic-ai
3. Download the LLM model (if not already downloaded):
ollama pull llama3:8b
4. Run the application:
python app.py
