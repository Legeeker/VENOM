import VENOM 
import game 

def test_venom():
    assert VENOM.bestcoup([0,7,56,63]) == 0 or 7 or 56 or 63 

def test_coord():
    assert game.coord(1) == (0,1)

def test_add(): 
    assert game.add((7,3),(8,9)) == (0, 1) , (15, 12)