# Text Prompt Generator with Gradio Interface

## Overview

This Python script uses Gradio to create a simple web-based interface for generating text prompts based on user input. The interface allows users to input four types of text:

- `prompt`: The main text that serves as the base prompt.
- `prepend`: Text that will be prepended to the main prompt.
- `append`: Text that will be appended to the main prompt.
- `args`: Additional arguments that will be added at the end.

Each of these input fields can contain multiple lines. All lines will be combined in all possible ways to generate a list of final prompts. Empty lines or lines with only whitespace are ignored.

## Installation

### Dependencies

- Gradio
- Tk

You can install the required packages using pip:

```bash
pip install gradio
pip install tk

## Usage

1. Run the script:

\`\`\`bash
python generate_and_save_prompts.py
\`\`\`

2. Open the Gradio interface that appears in your web browser.
   
3. Fill in the input fields (`prompt`, `prepend`, `append`, `args`) as needed.

4. Click the "Submit" button to generate the prompts.

5. A file explorer window will appear, allowing you to choose where to save the generated prompts as a `.txt` file.
