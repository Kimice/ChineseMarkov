# ChineseMarkov

Base on Markov model and [jieba](https://github.com/fxsjy/jieba) chinese text segmentation

Inspired by [hrs/markov-sentence-generator](https://github.com/hrs/markov-sentence-generator)


## Install

```bash
pip install chineseMarkov
```


## Usage

```python
import chineseMarkov

gen = chineseMarkov.MarkovGenerator('data/sample.txt', length=2)
gen.get_sentence()

```


