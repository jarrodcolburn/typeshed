from .vltypes import *
from .compoundtype import *
from numpy import dtype
from typing import Literal
from .types import *
from .group import *


class Variable:
    """A netCDF Variable is used to read and write netCDF data. They are analogous to numpy array objects."""

    def __init__(
        self,
        group: Group | Dataset,
        name: str,
        datatype,
        dimensions: Tuple[str, ...] = (),
        compression: Literal[
            "blosc_lz",
            "blosc_lz4",
            "blosc_lz4hc",
            "blosc_zlib",
            "bzip2",
            "szip",
            "zlib",
            "zstd",
            None,
        ] = None,
        zlib: bool = False,
        complevel: int = 4,
        shuffle: bool = True,
        szip_coding: Literal[
            "ec",
            "nn",
        ] = "nn",
        szip_pixels_per_block: Literal[
            4,
            8,
            16,
            32,
        ] = 8,
        blosc_shuffle: int = 1,
        fletcher32: bool = False,
        contiguous: bool = False,
        chunksizes: int | None = None,
        endian: Literal[
            "big",
            "little",
            "native",
        ] = "native",
        least_significant_digit: int = None,
        fill_value=None,
        chunk_cache=None,
    ) -> None:
        ...

    def dimensions(self) -> tuple:
        """
        A tuple containing the names of the dimensions associated with this variable.
        """
        ...

    def dtype(self) -> dtype:
        """
        A numpy dtype object describing the variable's data type.
        """
        ...

    def ndim(self) -> int:
        """
        The number of variable dimensions.
        """
        ...

    def shape(self) -> tuple:
        """
        A tuple with the current shape (length of all dimensions).
        """
        ...

    def scale(self) -> bool:
        """
        If True, scale_factor and add_offset are applied, and signed integer data is automatically converted to unsigned integer data if the _Unsigned attribute is set. Default is True, can be reset using Variable.set_auto_scale and Variable.set_auto_maskandscale methods.
        """
        ...

    def mask(self) -> bool:
        """
        If True, data is automatically converted to/from masked arrays when missing values or fill values are present. Default is True, can be reset using Variable.set_auto_mask and Variable.set_auto_maskandscale methods. Only relevant for Variables with primitive or enum types (ignored for compound and vlen Variables).
        """
        ...

    def chartostring(self) -> bool:
        """
        If True, data is automatically converted to/from character arrays to string arrays when the _Encoding variable attribute is set. Default is True, can be reset using Variable.set_auto_chartostring method.
        """
        ...

    def least_significant_digit(self) -> int:
        """
        Describes the power of ten of the smallest decimal place in the data the contains a reliable value. Data is truncated to this decimal place when it is assigned to the Variable instance. If None, the data is not truncated.
        """
        ...

    def significant_digits(self) -> int:
        """
        New in version 1.6.0. Describes the number of significant digits in the data the contains a reliable value. Data is truncated to retain this number of significant digits when it is assigned to the Variable instance. If None, the data is not truncated. Only available with netcdf-c >= 4.9.0, and only works with NETCDF4 or NETCDF4_CLASSIC formatted files. The number of significant digits used in the quantization of variable data can be obtained using the Variable.significant_digits method. Default None - no quantization done.
        """
        ...

    def quantize_mode(self) -> str:
        """
        New in version 1.6.0. Controls the quantization algorithm (default 'BitGroom', 'BitRound' and 'GranularBitRound' also available). The 'GranularBitRound' algorithm may result in better compression for typical geophysical datasets. Ignored if significant_digits not specified. If 'BitRound' is used, then significant_digits is interpreted as binary (not decimal) digits.
        """
        ...

    def __orthogonal_indexing__(self) -> Literal[True]:
        """
        Always True. Indicates to client code that the object supports 'orthogonal indexing', which means that slices that are 1d arrays or lists slice along each dimension independently. This behavior is similar to Fortran or Matlab, but different than numpy.
        """
        ...

    def datatype(self) -> VLType | CompoundType | dtype:
        """
        numpy data type (for primitive data types) or VLType/CompoundType instance (for compound or vlen data types).
        """
        ...

    def name(self) -> str:
        """
        String name.
        """
        ...

    def size(self) -> int:
        """
        The number of stored elements.
        """
        ...
