def sum_of_squares(a):
    tot = 0
    for i in a:
        tot += (i**2)
    return(tot)

def test_one():
    assert sum_of_squares([1,2,3]) == 14

def test_two():
    print(sum_of_squares([0,-2,6]))
