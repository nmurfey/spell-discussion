from abc import ABC, abstractmethod
from client import Card, CARD_MAP
from typing import List

IS_SERVER = True

class Caster:
    """This is a factory that allows for arbitrary casting of spells"""
    def cast(self, spell_type, spell, position, direction):
        """"""
        
        caster = self.get_caster(spell_type)
        return caster(spell, position, direction)
    
    def get_caster(self, spell):
        if spell.type_ == "Projectile":
            return self._projectile_caster
        # etc
    
    def _projectile_caster(self, spell, position, direction):
        print(f"Cast a projectile!! {spell}")
        
    def _beam_caster(self, spell, position, direction):
        print(f"Cast a {spell} {position} {direction}")
        
    def _shield_caster(self, spell, position, direction):
        print(f"Cast a {spell} {position} {direction}")
        
    def _trap_caster(self, spell, position, direction):
        print(f"Cast a {spell} {position} {direction}")
        
    def _spring_caster(self, spell, position, direction):
        print(f"Cast a {spell} {position} {direction}")
        
    def _rain_caster(self, spell, position, direction):
        print(f"Cast a {spell} {position} {direction}")
        
    def _stream_caster(self, spell, position, direction):
        print(f"Cast a {spell} {position} {direction}")
        
    def _playerbuff_caster(self, spell, position, direction):
        print(f"Cast a {spell} {position} {direction}")
    

class NetworkCaster:
    def network_cast(self, deck_info, buff_info):

        if not IS_SERVER: #---------------------------------------------------- SERVER
            return
    
        deck: List[Card] = [CARD_MAP[id_] for id_ in deck_info]
        
        # SPELL BUILDER 
        
        spell_type = deck[0].type_
        
        if spell_type == "projectile":
            builder = ProjectileSpellBuilder()
        
        constructor = SpellContructor()
        spell: Spell = constructor.build(builder, deck, buff_info)
        
        # etc.
        
        # CAST FACTORY
        
        caster = Caster()
        caster.cast(spell_type, spell, self.position, self.direction)
        
            
class SpellContructor:
    """Takes the information from a builder and constructs the spell"""
    def __init__(self):
        self._deck: List[Card] = []
            
    def build(self, builder, deck, buffs):
        """Build spell"""

class SpellBuilder(ABC):
    """This class builds the spell"""
    @abstractmethod
    def reset(self):
        """Clear spell and create new"""
        
    @abstractmethod
    def build_visuals(self):
        """Create the spells visual component"""

    @abstractmethod
    def build_physics(self):
        """Create the spells physics component"""
        
    @abstractmethod
    def build_trigger(self):
        """Create the spells physics component"""
        
    @abstractmethod
    def build_events(self):
        """Create the spells physics component"""
    
    @abstractmethod
    def get_result(self):
        """Return resultant spell"""

class Spell(ABC):
    def __init__(self):
        self.events = []
        self.triggers = []
        self.collisions = []
        self.eols = []
        
    def Awake(self):
        """"""
        
    def Start(self):
        """"""
    
    def Update(self):
        """"""
        for event in self.events:
            event.tick()
            
    
    def OnTrigger(self):
        """"""
        for trigger in self.triggers:
            trigger.trigger()
            
    def OnCollision(self):
        """"""
        for collision in self.collisions:
            collision.collide()
            
    def EOL(self):
        """"""
        for eol in self.eols:
            eol.collide()

class ProjectileSpellBuilder:
    """Builds the projectile spell"""


class Projectile(Spell):
    """This is the concrete spell"""
    
    def build_physics(self):
        """Set Gravity Off"""
    
class Lob(Spell):
    """This is the concrete spell"""
    
    def build_physics(self):
        """Set Gravity On"""
    
class Shield(Spell):
    """This is the concrete spell"""
    
class Beam(Spell):
    """This is the concrete spell"""
    
class Stream(Spell):
    """This is the concrete spell"""
    
class Trap(Spell):
    """This is the concrete spell"""
    
class Rain(Spell):
    """This is the concrete spell"""
    
class Spring(Spell):
    """This is the concrete spell"""

class PlayerBuffs(Spell):
    """This is the concrete spell"""