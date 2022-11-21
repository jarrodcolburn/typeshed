from .group import *


class Dimension:
    """
    A netCDF Dimension is used to describe the coordinates of a Variable. See Dimension.__init__ for more details.

    The current maximum size of a Dimension instance can be obtained by calling the python len function on the Dimension instance. The Dimension.isunlimited method of a Dimension instance can be used to determine if the dimension is unlimited
    """

    def __init__(self, group: Group, name: str, size=None) -> None:
        """Dimension instances should be created using the Dataset.createDimension method of a Group or Dataset instance, not using Dimension.__init__ directly."""
        ...

    @property
    def name(self) -> str:
        """Name of the dimension."""
        ...

    @property
    def size(self) -> int:
        """Size of the dimension. None or 0 means unlimited. (Default None)."""
        ...

    def group(self) -> Group:
        """Group instance to associate with dimension."""
        ...

    def isunlimited(self) -> bool:
        """
        returns True if the Dimension instance is unlimited, False otherwise.
        """
        ...
