## Breath of the Wild RSTB parser and editing tool

Utilities to manipulate the [RSTB (Resource Size TaBle)](https://github.com/leoetlino/botw-re-notes/blob/master/resource_system.md#resource-size-table).

It is recommended to be familiar with how the resource system works and
in particular how resources are listed
([Wii U RSTB](https://github.com/leoetlino/botw-re-notes/blob/master/game_files/wiiu_rstb_150.csv),
[Switch RSTB](https://github.com/leoetlino/botw-re-notes/blob/master/game_files/switch_rstb_150.csv))
in the table before modifying resource entries.

For all commands, **you must pass `--be` if you are dealing with a big endian RSTB** (Wii U version).

### Get a resource size

    rstbtool  [--be]  path/to/ResourceSizeTable.product.srsizetable  get  RESOURCE_NAME

### Set a resource size

    rstbtool  [--be]  path/to/ResourceSizeTable.product.srsizetable  set  RESOURCE_NAME  NEW_SIZE

NEW_SIZE can be an integer (hex or decimal), in which case the size will be set directly.

Or it can be a path on your _host filesystem_ (unlike RESOURCE_NAME). In that case rstb
will automatically calculate the size value it should write to the RSTB.

The RESOURCE_NAME must exist in the RSTB for this command.

### Add a resource size

    rstbtool  [--be]  path/to/ResourceSizeTable.product.srsizetable  add  RESOURCE_NAME  NEW_SIZE

Same as `set`, except the RESOURCE_NAME must *not* exist in the RSTB for this command.

### Delete a resource size

    rstbtool  [--be]  path/to/ResourceSizeTable.product.srsizetable  del  RESOURCE_NAME

**Warning**: deleting the entry for a resource will make the game waste precious memory
when loading it, since the resource system will fall back to a different, wasteful method
of calculating how much memory to allocate (see the resource system notes for more details).

**Deleting entries may cause instability**. Only use this command if rstbtool tells you to
do so or if you know what you are doing.

### License

This software is licensed under the terms of the GNU General Public License, version 2 or later.
