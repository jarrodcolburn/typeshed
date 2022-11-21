from .compoundtype import *
from .dimension import *
from .enumtypes import *
from .types import *
from .variables import *
from .vltypes import *

class Dataset:
    """
    Dataset

    A netCDF Dataset is a collection of dimensions, groups, variables and attributes. Together they describe the meaning of data and relations among data fields stored in a netCDF file.

    Attributes:
    ----------
        filename : Name of netCDF file to hold dataset. Can also be a python 3 pathlib instance or the URL of an OpenDAP dataset. When memory is set this is just used to set the filepath().

        mode: access mode. r means read-only; no data can be modified. w means write; a new file is created, an existing file with the same name is deleted. x means write, but fail if an existing file with the same name already exists. a and r+ mean append; an existing file is opened for reading and writing, if file does not exist already, one is created. Appending s to modes r, w, r+ or a will enable unbuffered shared access to NETCDF3_CLASSIC, NETCDF3_64BIT_OFFSET or NETCDF3_64BIT_DATA formatted files. Unbuffered access may be useful even if you don't need shared access, since it may be faster for programs that don't access data sequentially. This option is ignored for NETCDF4 and NETCDF4_CLASSIC formatted files.

        clobber: if True (default), opening a file with mode='w' will clobber an existing file with the same name. if False, an exception will be raised if a file with the same name already exists. mode=x is identical to mode=w with clobber=False.

        format: underlying file format (one of 'NETCDF4', 'NETCDF4_CLASSIC', 'NETCDF3_CLASSIC', 'NETCDF3_64BIT_OFFSET' or 'NETCDF3_64BIT_DATA'. Only relevant if mode = 'w' (if mode = 'r','a' or 'r+' the file format is automatically detected). Default 'NETCDF4', which means the data is stored in an HDF5 file, using netCDF 4 API features. Setting format='NETCDF4_CLASSIC' will create an HDF5 file, using only netCDF 3 compatible API features. netCDF 3 clients must be recompiled and linked against the netCDF 4 library to read files in NETCDF4_CLASSIC format. 'NETCDF3_CLASSIC' is the classic netCDF 3 file format that does not handle 2+ Gb files. 'NETCDF3_64BIT_OFFSET' is the 64-bit offset version of the netCDF 3 file format, which fully supports 2+ GB files, but is only compatible with clients linked against netCDF version 3.6.0 or later. 'NETCDF3_64BIT_DATA' is the 64-bit data version of the netCDF 3 file format, which supports 64-bit dimension sizes plus unsigned and 64 bit integer data types, but is only compatible with clients linked against netCDF version 4.4.0 or later.

        diskless: If True, create diskless (in-core) file. This is a feature added to the C library after the netcdf-4.2 release. If you need to access the memory buffer directly, use the in-memory feature instead (see memory kwarg).

        persist: if diskless=True, persist file to disk when closed (default False).

        keepweakref: if True, child Dimension and Variable instances will keep weak references to the parent Dataset or Group object. Default is False, which means strong references will be kept. Having Dimension and Variable instances keep a strong reference to the parent Dataset instance, which in turn keeps a reference to child Dimension and Variable instances, creates circular references. Circular references complicate garbage collection, which may mean increased memory usage for programs that create may Dataset instances with lots of Variables. It also will result in the Dataset object never being deleted, which means it may keep open files alive as well. Setting keepweakref=True allows Dataset instances to be garbage collected as soon as they go out of scope, potentially reducing memory usage and open file handles. However, in many cases this is not desirable, since the associated Variable instances may still be needed, but are rendered unusable when the parent Dataset instance is garbage collected.

        memory: if not None, create or open an in-memory Dataset. If mode = r, the memory kwarg must contain a memory buffer object (an object that supports the python buffer interface). The Dataset will then be created with contents taken from this block of memory. If mode = w, the memory kwarg should contain the anticipated size of the Dataset in bytes (used only for NETCDF3 files). A memory buffer containing a copy of the Dataset is returned by the Dataset.close method. Requires netcdf-c version 4.4.1 for mode=r netcdf-c 4.6.2 for mode=w. To persist the file to disk, the raw bytes from the returned buffer can be written into a binary file. The Dataset can also be re-opened using this memory buffer.

        encoding: encoding used to encode filename string into bytes. Default is None (sys.getdefaultfileencoding() is used).

        parallel: open for parallel access using MPI (requires mpi4py and parallel-enabled netcdf-c and hdf5 libraries). Default is False. If True, comm and info kwargs may also be specified.

        comm: MPI_Comm object for parallel access. Default None, which means MPI_COMM_WORLD will be used. Ignored if parallel=False.

        info: MPI_Info object for parallel access. Default None, which means MPI_INFO_NULL will be used. Ignored if parallel=False.
    """

    def __init__(
        self,
        filename: str,
        mode: MODE = "r",
        clobber=True,
        diskless=False,
        persist=False,
        keepweakref=False,
        memory=None,
        encoding=None,
        parallel=False,
        comm=None,
        info=None,
        format: DATA_MODEL = "NETCDF4",
    ) -> None: ...
    @property
    def dimensions(self) -> Dimension:
        """The dimensions dictionary maps the names of dimensions defined for the Group or Dataset to instances of the Dimension class."""
        ...
    @property
    def variables(self) -> dict[str, Variable]:
        """The variables dictionary maps the names of variables defined for this Dataset or Group to instances of the Variable class."""
        ...
    @property
    def groups(self) -> dict[str, Group]:
        """The groups dictionary maps the names of groups created for this Dataset or Group to instances of the Group class (the Dataset class is simply a special case of the Group class which describes the root group in the netCDF4 file)."""
        ...
    @property
    def cmptypes(self) -> dict[str, CompoundType]:
        """The cmptypes dictionary maps the names of compound types defined for the Group or Dataset to instances of the CompoundType class."""
        ...
    @property
    def vltypes(self) -> dict[str, VLType]:
        """The vltypes dictionary maps the names of variable-length types defined for the Group or Dataset to instances of the VLType class."""
        ...
    @property
    def enumtypes(self) -> dict[str,EnumType]:
        """The enumtypes dictionary maps the names of Enum types defined for the Group or Dataset to instances of the EnumType class."""
        ...
    @property
    def data_model(self) -> DATA_MODEL:
        """data_model describes the netCDF data model version, one of NETCDF3_CLASSIC, NETCDF4, NETCDF4_CLASSIC, NETCDF3_64BIT_OFFSET or NETCDF3_64BIT_DATA."""
        ...
    @property
    def file_format(self) -> DATA_MODEL:
        """same as data_model, retained for backwards compatibility."""
        ...
    @property
    def disk_format(self) -> DISK_FORMAT:
        """disk_format describes the underlying file format, one of NETCDF3, HDF5, HDF4, PNETCDF, DAP2, DAP4 or UNDEFINED. Only available if using netcdf C library version >= 4.3.1, otherwise will always return UNDEFINED."""
        ...
    @property
    def parent(self) -> Group | None:
        """parent is a reference to the parent Group instance. None for the root group or Dataset instance."""
        ...
    @property
    def path(self) -> str:
        """path shows the location of the Group in the Dataset in a unix directory format (the names of groups in the hierarchy separated by backslashes). A Dataset instance is the root group, so the path is simply '/'."""
        ...
    @property
    def keepweakref(self) -> bool:
        """If True, child Dimension and Variables objects only keep weak references to the parent Dataset or Group."""
        ...
    def file(self, encoding=None) -> str:
        """
        Get the file system path (or the opendap URL) which was used to open/create the Dataset. Requires netcdf >= 4.1.2. The path is decoded into a string using sys.getfilesystemencoding() by default, this can be changed using the encoding kwarg.
        """
        ...