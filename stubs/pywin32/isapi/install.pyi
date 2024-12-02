from _typeshed import Incomplete

this_dir: Incomplete

class FilterParameters:
    Name: Incomplete
    Description: Incomplete
    Path: Incomplete
    Server: Incomplete
    AddExtensionFile: bool
    AddExtensionFile_Enabled: bool
    AddExtensionFile_GroupID: Incomplete
    AddExtensionFile_CanDelete: bool
    AddExtensionFile_Description: Incomplete
    def __init__(self, **kw) -> None: ...

class VirtualDirParameters:
    Name: Incomplete
    Description: Incomplete
    AppProtection: Incomplete
    Headers: Incomplete
    Path: Incomplete
    Type: Incomplete
    AccessExecute: Incomplete
    AccessRead: Incomplete
    AccessWrite: Incomplete
    AccessScript: Incomplete
    ContentIndexed: Incomplete
    EnableDirBrowsing: Incomplete
    EnableDefaultDoc: Incomplete
    DefaultDoc: Incomplete
    ScriptMaps: list[ScriptMapParams]
    ScriptMapUpdate: str
    Server: Incomplete
    def __init__(self, **kw) -> None: ...
    def is_root(self): ...
    def split_path(self): ...

class ScriptMapParams:
    Extension: Incomplete
    Module: Incomplete
    Flags: int
    Verbs: str
    AddExtensionFile: bool
    AddExtensionFile_Enabled: bool
    AddExtensionFile_GroupID: Incomplete
    AddExtensionFile_CanDelete: bool
    AddExtensionFile_Description: Incomplete
    def __init__(self, **kw) -> None: ...

class ISAPIParameters:
    ServerName: Incomplete
    Filters: list[FilterParameters]
    VirtualDirs: list[VirtualDirParameters]
    def __init__(self, **kw) -> None: ...

verbose: int

def log(level, what) -> None: ...

class InstallationError(Exception): ...
class ItemNotFound(InstallationError): ...
class ConfigurationError(InstallationError): ...

def FindPath(options, server, name): ...
def LocateWebServerPath(description): ...
def GetWebServer(description: Incomplete | None = None): ...
def LoadWebServer(path): ...
def FindWebServer(options, server_desc): ...
def split_path(path): ...
def CreateDirectory(params, options): ...
def AssignScriptMaps(script_maps, target, update: str = "replace") -> None: ...
def get_unique_items(sequence, reference): ...
def CreateISAPIFilter(filterParams, options): ...
def DeleteISAPIFilter(filterParams, options) -> None: ...
def AddExtensionFiles(params, options) -> None: ...
def DeleteExtensionFileRecords(params, options) -> None: ...
def CheckLoaderModule(dll_name) -> None: ...
def Install(params, options) -> None: ...
def RemoveDirectory(params, options) -> None: ...
def RemoveScriptMaps(vd_params, options) -> None: ...
def Uninstall(params, options) -> None: ...
def GetLoaderModuleName(mod_name, check_module: Incomplete | None = None): ...
def InstallModule(conf_module_name, params, options, log=...) -> None: ...
def UninstallModule(conf_module_name, params, options, log=...) -> None: ...

standard_arguments: Incomplete

def build_usage(handler_map): ...
def MergeStandardOptions(options, params) -> None: ...
def HandleCommandLine(
    params,
    argv: Incomplete | None = None,
    conf_module_name: Incomplete | None = None,
    default_arg: str = "install",
    opt_parser: Incomplete | None = None,
    custom_arg_handlers={},
) -> None: ...