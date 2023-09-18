# Timing Side Channel Example

Presentation: https://docs.google.com/presentation/d/1MYieWwAqEIp5A8SyNpbzJwdj5Gil6KRMrV6-hGS0s00/edit?usp=sharing

### Testing Environment

- OS: Ubuntu Server 22.04
- Python: 3.10
    - pwntools (~~I'm lazy~~)
- g++: 11.4.0
- Valgrind: 3.18.1 from `apt`

### `.cpp` Files

Compile with `-O0`

### `sca.py`

Run with `python3 ./sca.py correct` or `python3 ./sca.py wrong`
