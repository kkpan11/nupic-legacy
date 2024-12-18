# Copyright 2013 Numenta Inc.
#
# Copyright may exist in Contributors' modifications
# and/or contributions to the work.
#
# Use of this source code is governed by the MIT
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

'''
A category filter can be applied to any categorical field

The basic operation is assumed to be: OR

In the final version users may input Boolean algebra to define this
behaviour

If your field is 'animals'

and your values are

1 - dogs
2 - cat
3 - mouse
4 - giraffe
5 - hippo

A category filter for dog,giraffe

would return records 1 and 4

Note that we're using a substring search so that dogs ~= dog

We can't know all the categories before hand so we present to the user a
freeform input box.
'''

class CategoryFilter(object):

  def __init__(self, filterDict):
    """
    TODO describe filterDict schema
    """
    self.filterDict = filterDict

  def match(self, record):
    '''
    Returns True if the record matches any of the provided filters
    '''

    for field, meta in self.filterDict.iteritems():
      index = meta['index']
      categories = meta['categories']
      for category in categories:
        # Record might be blank, handle this
        if not record:
          continue
        if record[index].find(category) != -1:
          '''
          This field contains the string we're searching for
          so we'll keep the records
          '''
          return True

    # None of the categories were found in this record
    return False
