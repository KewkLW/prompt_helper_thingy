import gradio as gr
from tkinter import filedialog
from tkinter import Tk
#iAmKewk

def generate_and_save_prompts(prompt, prepend, append, args):
    # Initialize list to hold final prompts
    final_prompts = []
    
    # Split prompt, prepend, append, args by lines and filter out lines with only whitespace
    prompt_lines = [line for line in prompt.split("\n") if line.strip() != ""]
    prepend_lines = [line for line in prepend.split("\n") if line.strip() != ""]
    append_lines = [line for line in append.split("\n") if line.strip() != ""]
    args_lines = [line for line in args.split("\n") if line.strip() != ""]
    
    for pre in prepend_lines:
        for main in prompt_lines:
            for app in append_lines:
                for arg in args_lines:
                    final_prompts.append(f"{pre}{main}{app}{arg}")

    # Initialize Tkinter root window but don't show it
    root = Tk()
    root.withdraw()
    
    # Open file explorer and get the save path
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    
    if file_path:
        # Save the final prompts to a text file
        with open(file_path, "w") as f:
            for line in final_prompts:
                f.write(f"{line}\n")
                
        return f"Prompts saved to {file_path}"
    else:
        return "File save cancelled."

# Define Gradio interface
iface = gr.Interface(
    fn=generate_and_save_prompts, 
    inputs=["text", "text", "text", "text"], 
    outputs="text",
    live=False
)

# Launch the Gradio interface
iface.launch()
