"""
Check that parameters' documentation have a uniform format.
  - `<param_name>`: [The |A |An ]*.
"""
import sys

COMMENTS_CAN_START_WITH = ' The ', ' If ', ' An ', ' A '

filename = sys.argv[1]

for line in open(filename).readlines():
    if line.replace(' ', '').startswith('-`') and ':' in line:
        try:
            variable, comment = line.split(':', maxsplit=1)

            assert variable.endswith(' ') is False
            assert any(comment.startswith(x) for x in COMMENTS_CAN_START_WITH)
            assert comment[-1] == '.' or comment[-2] == '.'
        except Exception as _:
            print(f"Error in file '{filename}': '{line}'")
            exit(1)
