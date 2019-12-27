# Copyright 2018 leoetlino <leo@leolam.fr>
# Licensed under GPLv2+

import io
import os
from . import rstb
import syaz0

def read_rstb(path_to_rstb: str, be: bool) -> rstb.ResourceSizeTable:
    with open(path_to_rstb, 'rb') as file:
        buf = syaz0.decompress(file.read())
        return rstb.ResourceSizeTable(buf, be)

def write_rstb(table: rstb.ResourceSizeTable, path_to_rstb: str, be: bool) -> None:
    buf = io.BytesIO()
    table.write(buf, be)
    buf.seek(0)
    with open(path_to_rstb, 'wb+') as file:
        _, extension = os.path.splitext(path_to_rstb)
        if extension.startswith('.s'):
            file.write(syaz0.compress(buf.getbuffer()))
        else:
            file.write(buf.getbuffer()) # type: ignore
