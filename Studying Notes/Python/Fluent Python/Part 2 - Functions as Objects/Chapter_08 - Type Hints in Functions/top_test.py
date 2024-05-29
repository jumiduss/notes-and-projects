from collections.abc import Iterable, Iterator
from typing import TypeVar, Protocol, Any, TYPE_CHECKING
import pytest

class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...

LT = TypeVar('LT', bound=SupportsLessThan)

def top(series: Iterable[LT], length: int) -> list[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]

def test_top_tuples() -> None:
    fruit = 'mango pear apple kiwi banana'.split()
    series: Iterator[tuple[int, str]] = ((len(s), s) for s in fruit)
    length = 3
    expected = [(6, 'banana'), (5, 'mango'), (5, 'apple')]
    result = top(series, length)
    if TYPE_CHECKING: # This is mypy's static type checking, and isn't run at runtime
        reveal_type(series)
        reveal_type(expected)
        reveal_type(result)
    assert result == expected

def test_top_objects_error() -> None:
    series = [object() for _ in range(4)]
    if TYPE_CHECKING:
        reveal_type(series)
    with pytest.raises(TypeError) as excinfo:
        top(series, 3)
    assert "'<' not supported" in str(excinfo.value)