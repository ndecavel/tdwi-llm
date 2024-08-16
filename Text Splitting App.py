import gradio as gr
import fitz  # PyMuPDF
import os
from PIL import Image
import io
from llama_index.core.node_parser import TokenTextSplitter, SentenceSplitter
import tiktoken
import base64



def count_tokens(text):
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))

def extract_text_from_pdf(pdf_file_path):
    pdf_document = fitz.open(pdf_file_path)
    text = '\n\n'.join([page.get_text("text") for page in pdf_document])
    return text

def extract_pages_as_images(pdf_file_path, num_pages=2):
    pdf_document = fitz.open(pdf_file_path)
    images = []
    total_pages = min(num_pages, len(pdf_document))
    for i in range(total_pages):
        page = pdf_document.load_page(i)
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes()))
        images.append(img)
    return images, total_pages

def document_parse_example(doc_text, splitter, chunk_size, chunk_overlap):
    if splitter == 'TokenTextSplitter':
        text_parser = TokenTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    elif splitter == 'SentenceSplitter':
        text_parser = SentenceSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    else:
        return []
    
    chunks = text_parser.split_text(doc_text)
    return chunks

def get_splitter_description(splitter):
    if splitter == 'TokenTextSplitter':
        return ("<b>TokenTextSplitter:</b> Splits text into chunks based on tokens. "
                "<br><b>Chunk Size:</b> Number of tokens per chunk."
                "<br><b>Chunk Overlap:</b> Number of overlapping tokens between chunks.")
    elif splitter == 'SentenceSplitter':
        return ("<b>SentenceTextSplitter:</b> Splits text with a preference for complete sentences."
                "<br><b>Chunk Size:</b> Number of tokens per chunk."
                "<br><b>Chunk Overlap:</b> Number of overlapping tokens between chunks.")
    else:
        return "Please select a Text Splitter to begin."

def gradio_interface(file_name, splitter, chunk_size, chunk_overlap):
    pdf_file_path = os.path.join(directory, file_name)
    doc_text = extract_text_from_pdf(pdf_file_path)
    chunks = document_parse_example(doc_text, splitter, chunk_size, chunk_overlap)
    description = get_splitter_description(splitter)

    # Extract and convert pages to images
    images, total_pages = extract_pages_as_images(pdf_file_path, num_pages=2)
    
    # Convert images to base64 strings for HTML display
    image_outputs = [None, None]
    if total_pages > 0:
        buffered = io.BytesIO()
        images[0].save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        image_outputs[0] = f"<img src='data:image/png;base64,{img_str}' style='width:100%;'>"
    if total_pages > 1:
        buffered = io.BytesIO()
        images[1].save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        image_outputs[1] = f"<img src='data:image/png;base64,{img_str}' style='width:100%;'>"

    # Format chunk details into an HTML table
    chunk_details = """
    <table style="width: 100%; border-collapse: collapse; color: white; background-color: #444;">
        <thead>
            <tr>
                <th style="border: 1px solid #888; padding: 5px;">Chunk Number</th>
                <th style="border: 1px solid #888; padding: 5px;">Chunk Text</th>
                <th style="border: 1px solid #888; padding: 5px;">Token Count</th>
                <th style="border: 1px solid #888; padding: 5px;">Length (Characters)</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for i, chunk in enumerate(chunks):
        token_count = count_tokens(chunk)
        chunk_length = len(chunk)
        chunk_details += f"""
        <tr>
            <td style="border: 1px solid #888; padding: 5px;">{i + 1}</td>
            <td style="border: 1px solid #888; padding: 5px; word-wrap: break-word;">{chunk}</td>
            <td style="border: 1px solid #888; padding: 5px;">{token_count}</td>
            <td style="border: 1px solid #888; padding: 5px;">{chunk_length}</td>
        </tr>
        """
    
    chunk_details += "</tbody></table>"
    
    if splitter:
        output = (f'<div style="color: white; background-color: #333; padding: 10px;">'
                  f'<div><b>Number of Chunks Created:</b> {len(chunks)}</div>'
                  f'<div><b>Chunk Details:</b><br>{chunk_details}</div>'
                  '</div>')
    else:
        output = ""
    
    return description, output, image_outputs[0], image_outputs[1]

# Create the Gradio app
def create_app():
    with gr.Blocks() as app:
        gr.Markdown("# Text Splitting Visualization")
        gr.Markdown("""
            ## Instructions:
            1. **Select a PDF file**: Choose a PDF file from the dropdown menu. The first two pages of the selected file will be displayed.
            2. **Visualize Pages**: View the first two pages of the PDF side by side. If the PDF has only one page, only that page will be shown.
            3. **Choose Text Splitter**: Select a text splitter from the dropdown menu and adjust the parameters (Chunk Size and Chunk Overlap). A description of each splitter will be displayed.
            4. **View Chunk Details**: The text chunks created by the selected splitter, along with their details, will be shown below.
        """)
        
        with gr.Row():
            with gr.Column(scale=1):
                file_input = gr.Dropdown(choices=file_names, label="Select PDF File")
        
        with gr.Row():
            with gr.Column(scale=1):
                image_output1 = gr.HTML(label="Page 1")
            with gr.Column(scale=1):
                image_output2 = gr.HTML(label="Page 2")
        
        with gr.Row():
            with gr.Column(scale=2):
                splitter_input = gr.Dropdown(choices=["TokenTextSplitter", "SentenceSplitter"], label="Text Splitter")
                chunk_size_input = gr.Slider(minimum=10, maximum=500, step=10, value=100, label="Chunk Size", visible=False)
                chunk_overlap_input = gr.Slider(minimum=0, maximum=50, step=1, value=0, label="Chunk Overlap", visible=False)
            with gr.Column(scale=1):
                description_output = gr.HTML(label="Splitter Description")
        
        chunk_details_output = gr.HTML(label="Chunk Details")

        def update_params_visibility(splitter):
            show_sliders = splitter in ["TokenTextSplitter", "SentenceSplitter"]
            return [
                gr.update(visible=show_sliders),
                gr.update(visible=show_sliders)
            ]

        splitter_input.change(
            fn=update_params_visibility,
            inputs=[splitter_input],
            outputs=[chunk_size_input, chunk_overlap_input]
        )

        def update_visuals_on_file_change(file_name, splitter, chunk_size, chunk_overlap):
            description, output, image1, image2 = gradio_interface(file_name, splitter, chunk_size, chunk_overlap)
            return image1, image2, description, output

        # Create separate change functions for file and splitter
        file_input.change(fn=update_visuals_on_file_change, inputs=[file_input, splitter_input, chunk_size_input, chunk_overlap_input], outputs=[image_output1, image_output2, description_output, chunk_details_output])
        splitter_input.change(fn=update_visuals_on_file_change, inputs=[file_input, splitter_input, chunk_size_input, chunk_overlap_input], outputs=[image_output1, image_output2, description_output, chunk_details_output])
        chunk_size_input.change(fn=update_visuals_on_file_change, inputs=[file_input, splitter_input, chunk_size_input, chunk_overlap_input], outputs=[image_output1, image_output2, description_output, chunk_details_output])
        chunk_overlap_input.change(fn=update_visuals_on_file_change, inputs=[file_input, splitter_input, chunk_size_input, chunk_overlap_input], outputs=[image_output1, image_output2, description_output, chunk_details_output])

    return app

def launch_app(TDS_FOLDER_PATH):
    # Define the directory containing your files
    global directory
    directory = TDS_FOLDER_PATH

    # List all PDF files in the directory
    global file_names
    file_names = sorted([f for f in os.listdir(directory) if f.endswith('.pdf')])
    app = create_app()
    app.launch(debug=False)
