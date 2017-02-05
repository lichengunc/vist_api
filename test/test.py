import vist

sis = vist.SIS('/playpen/data/vist')
story_id = sis.Stories.keys()[0]
print sis.Stories[story_id]