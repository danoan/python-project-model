from danoan import utils


def test_title():
    width = 64
    expected_str = f"{'*'*width}\n"
    expected_str += "Toml dataclass".center(width) + "\n"
    expected_str += f"{'*'*width}"

    assert expected_str == utils.title("Toml dataclass")
