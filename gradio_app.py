from pathlib import Path
import html as h
import gradio as gr

game = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
iframe = f'<iframe srcdoc="{h.escape(game, quote=True)}" style="width:100%;height:92vh;border:0" allow="autoplay"></iframe>'

with gr.Blocks(title="ميمي") as demo:
    gr.HTML(iframe)

demo.launch(share=True)