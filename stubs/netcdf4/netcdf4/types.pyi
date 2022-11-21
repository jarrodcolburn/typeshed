from typing import Literal, TypeAlias, Dict, Tuple

ENUM_DICT: TypeAlias = dict[str,int]
# ENDIAN: TypeAlias = Literal['big','little','native']
# DIMENSIONS: TypeAlias = Tuple[str, ...]

MODE: TypeAlias = Literal[
    "a",
    "a+s",
    "r",
    "r+",
    "r+s",
    "rs",
    "w",
    "ws",
    "x",
]
DATA_MODEL: TypeAlias = Literal[
    "NETCDF3_64BIT_DATA",
    "NETCDF3_64BIT_OFFSET",
    "NETCDF3_CLASSIC",
    "NETCDF4_CLASSIC",
    "NETCDF4",
]
FILE_FORMAT: TypeAlias = DATA_MODEL  # retained for backwards compatibility
DISK_FORMAT: TypeAlias = Literal[
    "DAP2",
    "DAP4",
    "HDF4",
    "HDF5",
    "NETCDF3",
    "PNETCDF",
    "UNDEFINED",
]
