# -*- coding: utf-8 -*-

import jieba
import codecs
import random
import collections
from punctuations import STOPS, NON_STOPS


class Markov(object):
    def __init__(self, filename='', length=1):
        self._start_word = []
        self._temp_map = collections.defaultdict(collections.Counter)
        self._word_map = {}
        self._markov_length = length
        self.filename = filename
        self.word_list = self._get_word_list()

    def _get_word_list(self):
        with codecs.open(self.filename, 'r', encoding='utf-8') as f:
            words_list = [w for w in jieba.cut(f.read(), cut_all=False)]
            print 'jieba cut words done! Get {} words'.format(len(words_list))
            return words_list

    def _prepare_word_list(self):
        self._start_word.append(self.word_list[0])
        for i in range(1, len(self.word_list) - 1):
            if i < self._markov_length:
                words_history = self.word_list[:i + 1]
            else:
                words_history = self.word_list[i - self._markov_length + 1: i + 1]
            next_word = self.word_list[i + 1]
            if words_history[-1] in STOPS and next_word not in NON_STOPS:
                self._start_word.append(next_word)
            # temp map store next word counts
            while len(words_history) > 0:
                key = tuple(words_history)
                self._temp_map[key][next_word] += 1.0
                words_history = words_history[1:]
        # probable for next words
        for word, probable_word in self._temp_map.iteritems():
            total = sum(probable_word.values())
            self._word_map[word] = {
                k: v / total for k, v in probable_word.iteritems()
            }

    def _get_next_word(self, prev_list):
        probably_sum = 0.0
        next_word = u''
        index = random.random()
        while tuple(prev_list) not in self._word_map:
            prev_list.pop(0)
        for k, v in self._word_map[tuple(prev_list)].iteritems():
            probably_sum += v
            if probably_sum >= index and not next_word:
                next_word = k
                break
        return next_word

    def gen_sentence(self):
        self._prepare_word_list()
        current_word = random.choice(self._start_word)
        sentence = current_word
        prev_list = [current_word]
        while current_word not in STOPS:
            current_word = self._get_next_word(prev_list)
            prev_list.append(current_word)
            if len(prev_list) > self._markov_length:
                prev_list.pop(0)
            sentence = u''.join((sentence, current_word))
        return sentence
