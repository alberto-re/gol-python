import pytest  # noqa, flake8 issue

from gol.game_state import GameState


def test_init_from_array():
    state = [
        [1, 0, 0],
        [0, 1, 1],
        [1, 0, 1]]
    gs = GameState(array=state)
    assert state == gs._cells


def test_init_shape_density():
    gs = GameState(20, 20, 0.4)
    assert 20 == gs.n_cols
    assert 20 == gs.n_rows


def test_neighbors_score():
    state = [
        [1, 0, 0],
        [0, 1, 1],
        [1, 0, 1]]
    gs = GameState(array=state)
    assert gs._neighbors_score(0, 0) == 4
    assert gs._neighbors_score(0, 1) == 5
    assert gs._neighbors_score(0, 2) == 5
    assert gs._neighbors_score(1, 0) == 5
    assert gs._neighbors_score(1, 1) == 4
    assert gs._neighbors_score(1, 2) == 4
    assert gs._neighbors_score(2, 0) == 4
    assert gs._neighbors_score(2, 1) == 5
    assert gs._neighbors_score(2, 2) == 4
