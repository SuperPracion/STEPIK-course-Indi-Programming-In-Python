my_set = {
    'mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
    'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error',
    'pneumonia', 'concert', 'value', 'value', 'disclose', 'glasses', 'tank',
    'national', 'soup', 'feel', 'few', 'concert', 'wrestle', 'proposal', 'soup',
    'sail', 'brown', 'service', 'proposal', 'winter', 'jacket', 'mention',
    'tradition', 'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal',
    'government', 'control', 'value', 'few', 'generation', 'service', 'national',
    'tradition', 'government', 'mention', 'proposal'
}

for remove_word in ['government', 'national', 'tease']:
    my_set.discard(remove_word)
