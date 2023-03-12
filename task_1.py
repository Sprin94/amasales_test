from typing import Tuple
from collections import deque


def check_relation(net: Tuple[Tuple[str, str]],
                   first: str, second: str) -> bool:
    relations = {}
    for i in net:
        relations.setdefault(i[0], set()).add(i[1])
        relations.setdefault(i[1], set()).add(i[0])

    q = deque()
    q.append(first)
    viewed = set()
    while q:
        current_friend = q.popleft()
        if current_friend == second:
            return True
        viewed.add(current_friend)
        for i in relations[current_friend]:
            if i not in viewed:
                q.append(i)
    return False


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
