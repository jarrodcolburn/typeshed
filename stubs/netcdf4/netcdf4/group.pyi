from .dataset import * 
from __future__ import annotations
class Group(Dataset):
    def __init__(self, parent: Group, name: str) -> None:
        """ Note: Group instances should be created using the Dataset.createGroup method of a Dataset instance, or another Group instance, not using this class directly.  """
        ...

    def parent(self) -> Group | Dataset | None : 
        """
        Group instance for the parent group. If being created in the root group, use a Dataset instance.
        """
        ...
        
    def name(self) -> str: 
        """
        Name of the group.
        """
        ...
    
    def close(self) -> IOError:
        """
        Overrides Dataset close method which does not apply to Group instances, raises IOError.
        """
