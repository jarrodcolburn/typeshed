class CompoundType:
    """
    A CompoundType instance is used to describe a compound data type, and can be passed to the the Dataset.createVariable method of a Dataset or Group instance. Compound data types map to numpy structured arrays. See CompoundType.__init__ for more details.

    The instance variables dtype and name should not be modified by the user.
    """

    def __init__(group, datatype, datatype_name) -> None: ...