import re 

def gruesome(str):
    
    result = []
    
    result = result + re.findall(r"[a-zA-Z]*b[a-zA-Z]*t[a-zA-z]*",str)
    result = result + re.findall(r"[a-zA-Z]*t[a-zA-Z]*g[a-zA-z]*",str)
    
    return list(set(result))

test1 = "A gruesome wombat practiced rackateering!"

answer1 = [ "wombat", "rackateering" ]

print (gruesome(test1) == answer1)

test2 = """Sir Walter Elliot, of Kellynch Hall, in Somersetshire, was
a man who, for his own amusement, never took up any book but the
Baronetage; there he found occupation for an idle hour, and
consolation in a distressed one; there his faculties were roused into
admiration and respect, by contemplating the limited remnant of the
earliest patents; there any unwelcome sensations, arising from
domestic affairs changed naturally into pity and contempt as he turned
over the almost endless creations of the last century; and there, if
every other leaf were powerless, he could read his own history with an
interest which never failed. This was the page at which the favourite
volume always opened:""" # Jane Austen 

print (gruesome(test2) == ['but', 'Baronetage', 'contemplating'])

test3 = """Every inch of wall space is covered by a bookcase. Each
bookcase has six shelves, going almost to the ceiling. Some
bookshelves are stacked to the brim with hardcover books: science,
mathematics, history, and everything else. Other shelves have two
layers of paperback science fiction, with the back layer of books
propped up on old tissue boxes or two-by-fours, so that you can see
the back layer of books above the books in front. And it still isn't
enough. Books are overflowing onto the tables and the sofas and making
little heaps under the windows.""" # E. Yudkowsky

print (gruesome(test3) == ['everything'])

test4 = """The reign of terror caused by wombats sseems to be abating.""" 

print (gruesome(test4) == ['wombats', 'abating'])
