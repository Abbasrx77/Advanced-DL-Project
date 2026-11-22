"""Gradio application (empty shell used to test the installation).

Run with: ``python -m src.app.app``
"""

from __future__ import annotations

import gradio as gr

from src.data.classes import CLASSES

NOT_IMPLEMENTED = "Pas encore implémenté"


def _not_implemented(*_args: object) -> str:
    return NOT_IMPLEMENTED


def build_app() -> gr.Blocks:
    """Build the Gradio interface with its three tabs."""
    with gr.Blocks(title="EuroSAT Assistant") as demo:
        gr.Markdown("# EuroSAT Assistant")
        with gr.Tab("Classification"):
            image = gr.Image(type="pil", label="Image")
            classify_btn = gr.Button("Classer")
            classify_out = gr.Markdown(NOT_IMPLEMENTED)
            classify_btn.click(_not_implemented, inputs=image, outputs=classify_out)
        with gr.Tab("Génération"):
            label = gr.Dropdown(choices=list(CLASSES), label="Classe")
            generate_btn = gr.Button("Générer")
            generate_out = gr.Markdown(NOT_IMPLEMENTED)
            generate_btn.click(_not_implemented, inputs=label, outputs=generate_out)
        with gr.Tab("Questions"):
            question = gr.Textbox(label="Question")
            ask_btn = gr.Button("Demander")
            ask_out = gr.Markdown(NOT_IMPLEMENTED)
            ask_btn.click(_not_implemented, inputs=question, outputs=ask_out)
    return demo


def main() -> None:
    """Launch the app locally."""
    build_app().launch()


if __name__ == "__main__":
    main()
