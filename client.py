from abc import ABC, abstractmethod
from .server import NetworkCaster
from typing import List


class Card(ABC):
    """Defines a spell property"""
    ID = 0 # unique to each and every card
    
    @property
    def type_(self):
        return self._type
    
    @abstractmethod
    def valid_play(self, deck) -> bool | Exception:
        """Check the deck to make sure that the placement is correct"""
        return NotImplementedError()
    
# -- SPELL TYPES

class SpellTypeCard(Card):
    """Defines a concrete card"""
    def valid_play(self, deck: List[Card]) -> bool:
        # Needs to be the first card in the deck
        return len(deck) == 0 
    
    @abstractmethod
    def apply_modifiers(self, spell) -> None | Exception:
        """Modifiers Specific to the Projectile Card"""
        return NotImplementedError()

class EssenceProjectileCard(SpellTypeCard):
    """Essense projectile"""
    def apply_modifiers(self, spell):
        """Modifiers Specific to the Projectile Card"""
    
class EssenceBeamCard(SpellTypeCard):
    """Essense projectile"""

# -- Modifiers

class Modifier(Card):        
    """Defines a concrete card"""
    
class Multiplier(Modifier):        
    """Defines a concrete card"""
    
class Elemental(Modifier):        
    """Defines a concrete card"""

# -- Triggers
    
class Trigger(Card):        
    """Defines a concrete card"""

class ExplodeOnPlayer(Trigger):
    """Defines a concrete card"""
    
class ExplodeOnImpact(Trigger):
    """Defines a concrete card"""

# -- Event
    
class Event(Card):        
    """Defines a concrete card"""
    
class Explode(Event):        
    """Defines a concrete card"""
        
class Deck:
    def __init__(self) -> None:
        self._deck: List[Card] = []
        
    def append(self, card: Card):
        
        if card.valid_play(self._deck):
            self._deck.append(card)    

    def deck_info(self):
        return [card.ID for card in self._deck]
    
    def reset(self):
        self._deck = []
        
    
class BuffInfo(ABC):

    def buff_deck(self, deck: List[Card]):
        for card in deck:
            self.apply_buff(card)
        
    @abstractmethod
    def apply_buff(self, card):
        """Apply buff to card"""
        raise NotImplementedError()
        
class Player:
    def __init__(self) -> None:
        
        self._wand_buffs = []
        self._player_buffs = []
        
        self._spell_buffer = Deck()
    
    async def spell_action(self):
        """Cast Spell"""
        buffs = self._wand_buffs + self._player_buffs
        await NetworkCaster().network_cast(self._spell_buffer.deck_info(), buffs)
        self._spell_buffer.reset()


# ALL CARD CLASSES DEFINED IN MAP WITH UNIQUE IDs
CARD_MAP = {
    "unique_id_1": EssenceProjectileCard,
    "unique_id_2": EssenceBeamCard
}
