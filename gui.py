from easygui import msgbox, enterbox
from typing import Any

TITLE: str = "战舰世界汉化安装器"
OK_BUTTON: str = "好"


def print(*values: object) -> None:
    """
    使用EasyGUI提供的消息窗体代替builtin print。
    :param values: 同builtin print的第一个参数
    :return: 无
    """
    msgbox(" ".join(map(str, values)), TITLE, OK_BUTTON)


def input(__prompt: Any) -> str:
    """
    使用EasyGUI提供的输入窗体代替builtin input。
    :param 同builtin input用法
    :return: 用户输入，不为None
    """
    result: str | None = enterbox(str(__prompt), TITLE)

    return "" if result is None else result
