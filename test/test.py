import sys
sys.path.insert(0, '../')
import vist

sis = vist.Story_in_Sequence('/playpen/data/vist')
story_id = sis.Stories.keys()[0]
print sis.Stories[story_id]
