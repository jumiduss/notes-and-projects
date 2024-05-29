# Starting base function for mypy example, runs without conflict with mypy
# def show_count(count, word):
#     if count == 1:
#         return f'1 {word}'
#     count_str = str(count) if count else 'no'
#     return f'{count_str} {word}s'

# First Type Annotation Test
# def show_count(count, word) -> str:
#     if count == 1:
#         return f'1 {word}'
#     count_str = str(count) if count else 'no'
#     return f'{count_str} {word}s'

# Second Type Annotation Test
# def show_count(count: int, word: str) -> str:
#     if count == 1:
#         return f'1 {word}'
#     count_str = str(count) if count else 'no'
#     return f'{count_str} {word}s'


# Adding the Plural Argument
def show_count(count: int, singular: str, plural: str = '') -> str:
    if count == 1:
        return f'1 {singular}'
    count_str = str(count) if count else 'no'
    if not plural:
        plural = singular + 's'
    return f'{count_str} {plural}s'