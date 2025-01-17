#!/usr/bin/env python
"""
Contains the Observer class definition

Please note that this module is private. The Observer class is
available in the main ``ananke`` namespace - use that instead.
"""
import numpy as np
from Galaxia_ananke.constants import DEFAULTS_FOR_PARFILE

from .constants import *

__all__ = ['Observer']


class Observer:  # TODO SkyCoord for center point: SkyCoord(u=-rSun[0], v=-rSun[1], w=-rSun[2], unit='kpc', representation_type='cartesian', frame='galactic')
    """
        Store the observer parameters.
    """
    _pos0 = 'rSun0'
    _pos1 = 'rSun1'
    _pos2 = 'rSun2'
    _pos = [_pos0,_pos1,_pos2]
    _default_position = np.array([DEFAULTS_FOR_PARFILE[_p] for _p in _pos])
    _vel = []  # TODO
    _pha = _pos+_vel

    def __init__(self, ananke, pos, **kwargs) -> None:
        """
        Parameters
        ----------
        ananke : Ananke object
            The Ananke object that utilizes this Observer object
        pos : array-like shape (3,)
            Position of the observer
        **kwargs
            Additional parameters
        """
        self.__ananke = ananke
        self.__position = self.__prepare_position(pos)
        self.__velocity = []
        self.__parameters = kwargs
    
    def __prepare_position(self, pos):
        pos = np.array(pos)
        pos[np.isnan(pos)] = self._default_position[np.isnan(pos)]
        return pos

    @property
    def ananke(self):
        return self.__ananke

    @property
    def position(self):
        return self.__position
    
    @property
    def velocity(self):
        return self.__velocity
    
    @property
    def phase_space(self):
        return np.hstack([self.position, self.velocity])
    
    @property
    def to_galaxia_kwargs(self):
        return dict(zip(self._pha, self.phase_space))
        
    @property
    def parameters(self):
        return self.__parameters
    