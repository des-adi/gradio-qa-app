import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import ollama
from pydantic_ai import PydanticAI

# Initialize LLM and Pydantic AI
def initialize_llm():
    model = "llama3:8b"
    ollama.pull(model)
    return model

llm = initialize_llm()
pydantic_ai = PydanticAI(llm=llm)

# Load CSV file
def load_csv(file):
    try:
        df = pd.read_csv(file.name)
        return df
    except Exception as e:
        raise gr.Error(f"Error parsing CSV file: {str(e)}")

# Ask questions using LLM
def ask_question(df, question):
    try:
        data_summary = df.describe().to_string()
        prompt = f"The dataset contains the following information:\n{data_summary}\n\nQuestion: {question}\nAnswer:"
        response = ollama.generate(model=llm, prompt=prompt)
        return response["response"]
    except Exception as e:
        raise gr.Error(f"Error generating answer: {str(e)}")

# Generate plots
def generate_plot(df, question):
    try:
        if "price" in df.columns:
            plt.figure()
            df["price"].hist()
            plt.title("Price Distribution")
            return plt.gcf()
        else:
            return None
    except Exception as e:
        raise gr.Error(f"Error generating plot: {str(e)}")

# Process user queries
def process_query(file, question):
    try:
        if file is None:
            raise gr.Error("Please upload a CSV file.")
        
        df = load_csv(file)
        answer = ask_question(df, question)
        plot = generate_plot(df, question)
        return answer, plot
    except Exception as e:
        raise gr.Error(f"An error occurred: {str(e)}")

# Gradio interface
def main():
    with gr.Blocks() as demo:
        gr.Markdown("# CSV Question Answering and Visualization")
        
        with gr.Row():
            file_input = gr.File(label="Upload CSV File", file_types=[".csv"])
        
        with gr.Row():
            question_input = gr.Textbox(label="Ask a Question")
        
        with gr.Row():
            answer_output = gr.Textbox(label="Answer")
            plot_output = gr.Plot(label="Visualization")
        
        submit_button = gr.Button("Submit")
        
        submit_button.click(
            process_query,
            inputs=[file_input, question_input],
            outputs=[answer_output, plot_output]
        )
    
    demo.launch()

if __name__ == "__main__":
    main()