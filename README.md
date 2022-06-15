# Emoji

Extending [carpedm20/emoji](https://github.com/carpedm20/emoji) with **Bahasa Indonesia** support. Indonesian Emoji data obtained from
Google Translate API via [ssut/py-googletrans](https://github.com/ssut/py-googletrans).

**Example**

```python
>>> import emoji
>>> print(emoji.emojize('Python :jempolan:'))
Python 👍
>>> print(emoji.demojize('Python 👍'))
Python :jempolan:
```

## Installation

```bash
$ pip install -U git+https://github.com/Hyuto/emoji.git@master
```

## Development

```
$ git clone https://github.com/Hyuto/emoji.git
$ cd emoji
$ pip install -e .\[dev\]
$ pytest
```
