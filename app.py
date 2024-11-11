# App #

# Import Packages
from gradio.themes.base import Base
from query import query_data
import gradio as gr

# App Interface

# Title
with gr.Blocks(theme=Base(), title="QnA App") as demo:
    # Header
    gr.Markdown("# Question Answering App Using Atlas Vector Search + RAG Architecture")
    # Textbox and Button
    textbox = gr.Textbox(label="Enter Your Question:")
    with gr.Row():
        button = gr.Button("Submit", variant="primary")
    with gr.Column():
        output1 = gr.Textbox(
            lines=1,
            max_lines=10,
            label="Output Using Atlas Vector Search: (Returns Page Content)",
        )
        output2 = gr.Textbox(
            lines=1,
            max_lines=10,
            label="Output Using Chaining: Atlas Vector Search -> LangChain RetrieverQA -> OpenAI LLM: (Returns Answer)",
        )

    # Button Click Event Handler Function Call
    button.click(query_data, textbox, outputs=[output1, output2])

# Launch The App
demo.launch(share=True)  # For Public Link Make share=True
