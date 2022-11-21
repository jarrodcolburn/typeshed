from .group import Group
from .types import *
from numpy import dtype
class EnumType:
    """A EnumType instance is used to describe an Enum data type, and can be passed to the the Dataset.createVariable method of a Dataset or Group instance. See EnumType.__init__ for more details.  """
    def __init__(group: Group, datatype: dtype, datatype_name: str, enum_dict: ENUM_DICT):
        """
        Attributes:

        group: Group instance to associate with the VLEN datatype.

        datatype: An numpy integer dtype object describing the base type for the Enum.

        datatype_name: a Python string containing a description of the Enum data type.

        enum_dict: a Python dictionary containing the Enum field/value pairs.
        """
        ...