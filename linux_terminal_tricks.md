# Linux Terminal tricks

## How to create file with a numberic prefix within a range and fixed suffix using touch and sed
```bash
seq 10 28 | sed -En "s/(.*)/\1-answer.txt/p" | xargs -t touch
```
