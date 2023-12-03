from textwrap import dedent


def title(text: str, border: str = "*", width: int = 64):
    title = f"{border*width}\n"
    title += f"{text.center(width)}\n"
    title += f"{border*width}"

    return dedent(title)
