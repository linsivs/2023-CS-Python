from ocean import Ocean


def test_ocean_init():
    init_state = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ocean = Ocean(init_state = init_state)
    assert ocean.state == init_state


def test_ocean_repr():
    init_state = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ocean = Ocean(init_state = init_state)
    expected_repr = "Ocean([[1, 2, 3], [4, 5, 6], [7, 8, 9]])"
    assert repr(ocean) == expected_repr


def test_ocean_step():
    init_state = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ocean = Ocean(init_state = init_state)
    next_state = ocean.gen_next_quantum()
    expected_next_state = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
    assert next_state.state == expected_next_state
