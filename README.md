# ChineseMarkov

Base on Markov model and [jieba](https://github.com/fxsjy/jieba) chinese text segmentation

Inspired by [hrs/markov-sentence-generator](https://github.com/hrs/markov-sentence-generator)


## Usage

```python
import markov

m = markov.Markov('data/sample.txt', length=2)
print m.gen_sentence()

```


