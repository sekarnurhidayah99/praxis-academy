dictionary = ['fox', 'boss', 'orange', 'toes', 'fairy', 'cup']
def puralize(words):
   result = []
   for word in words:
       word = words[i]
       if word.endswith('s') or word.endswith('x'):
           plural = (word + 'es')
           if word.endswith('y'):
               plural = (word[:-1] + 'ies')
       else:
           plural = +  's'
       result.append(plural)
       return result
       def test_pluralize():
           result = puralize(dictionary)
           assert result == ['foxes', 'bosses', 'oranges', 'toeses', 'fairies', 'cups']

def add_bar(items=[]):
    items.append('bar')
    return items

l = add_bar()  # l is ['bar']
l.append('foo')
add_bar() # returns ['bar', 'foo', 'bar']