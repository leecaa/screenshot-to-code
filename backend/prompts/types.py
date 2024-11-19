from typing import Literal, TypedDict


class SystemPrompts(TypedDict):
    html_css: str
    html_tailwind: str
    react_tailwind: str
    expo: str
    bootstrap: str
    ionic_tailwind: str
    vue_tailwind: str
    svg: str


Stack = Literal[
    "html_css",
    "html_tailwind",
    "react_tailwind",
    "expo",
    "bootstrap",
    "ionic_tailwind",
    "vue_tailwind",
    "svg",
]
