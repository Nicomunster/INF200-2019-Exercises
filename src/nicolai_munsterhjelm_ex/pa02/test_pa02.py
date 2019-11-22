# -*- coding: utf-8 -*-

__author__ = 'Alf Georg Ovland', 'Nicolai Munsterhjelm'
__email__ = 'alov@nmbu.no', 'nicmunst@nmbu.no'

import random
import chutes_simulation as cs
import pytest


class TestBoard:
    """Tests for Board class"""
    def test_goal_reached(self):
        """Tests if the goal returns 'True' when position > goal and 'False'
        if not"""
        b = cs.Board(goal=50)
        assert b.goal_reached(50)
        assert not b.goal_reached(2)

    def test_position_adjustment(self):
        """Tests if position_adjustment returns the correct adjustment for
        different positions"""
        b = cs.Board()
        assert b.position_adjustment(2) == 0
        assert b.position_adjustment(49) == 79-49
        assert b.position_adjustment(33) == 3-33


class TestPlayer:
    """Tests for Player class"""
    def test_move(self):
        """Tests if turns is increased by one, and position is changed after
        move."""
        b = cs.Board()
        p = cs.Player(b)
        turns_before = p.turns
        position_before = p.position
        p.move()
        assert p.turns == turns_before + 1
        assert p.position != position_before
        p.position = 22
        random.seed(1)
        p.move()
        random.seed(1)
        p.move()
        assert p.position == 7


class TestResilientPlayer:
    """Tests for ResilientPlayer class"""
    def test_move(self):
        """Tests that resilient player moves as it should."""
        b = cs.Board()
        resilient_player = cs.ResilientPlayer(b, extra_steps=5)
        resilient_player.position = 22
        random.seed(1)
        resilient_player.move()
        random.seed(1)
        resilient_player.move()
        assert resilient_player.position == 12


class TestLazyPlayer:
    """Tests for LazyPlayer class"""
    def test_move(self):
        b = cs.Board()
        lazy_player = cs.LazyPlayer(b, dropped_steps=1)
        lazy_player.position = 34
        random.seed(1)
        lazy_player.move()
        random.seed(1)
        lazy_player.move()
        assert lazy_player.position == 53


class TestSimulation:
    """Tests for Simulation class"""
    def test_single_game(self):
        b = cs.Board()
        s = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer])
