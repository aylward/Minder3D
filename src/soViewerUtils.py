"""
Utility functions for working with spatial objects.

This module contains utility functions for working with spatial objects.

Functions:
    get_children_as_list: Finds all children of a given type in a
        GroupSpatialObject and returns them as a list.
    read_group: Reads a group from a file.
    write_group: Writes a group to a file.
"""

import itk


def get_children_as_list(
    grp: itk.GroupSpatialObject, child_type: str = "Tube"
) -> list:
    """Finds all children of a given type in a Group and returns as a list.

    Args:
        grp (itk.GroupSpatialObject): The GroupSpatialObject to search.
        child_type (str, optional): The type of object to be included.
            Defaults to "Tube".

    Returns:
        list: The list of children of the given type.
    """
    soList = grp.GetChildren(
        grp.GetMaximumDepth(),
        child_type
    )
    return [
        itk.down_cast(soList[i])
        for i in range(len(soList))
    ]


def get_so_index_in_list(
    so_id: int, so_list: list
) -> int:
    """Finds the index of a so in a list of sos.

    Args:
        so_id (int): The id of the so to find.
        so_list (list): The list of sos to search.

    Returns:
        int: The index of the so in the list.
    """
    id_list = [so.GetId() for so in so_list]
    index = id_list.index(so_id)
    return index


def read_group(filename: str, dims: int = 3) -> itk.GroupSpatialObject:
    """Reads a group from a file.

    Args:
        filename (str): The name of the file to read.
        dims (int, optional): The dimensionality of the group. Defaults to 3.

    Returns:
        itk.GroupSpatialObject: The group read from the file.
    """
    GroupFileReaderType = itk.SpatialObjectReader[dims]

    groupFileReader = GroupFileReaderType.New()
    groupFileReader.SetFileName(filename)
    groupFileReader.Update()

    return groupFileReader.GetGroup()


def write_group(group: itk.GroupSpatialObject, filename: str):
    """Writes a group to a file.

    Args:
        group (itk.GroupSpatialObject): The group to write.
        filename (str): The name of the file to write to.

    Returns:
        itk.GroupSpatialObject: The group read from the file.
    """
    dims = group.GetObjectDimension()
    GroupFileWriterType = itk.SpatialObjectWriter[dims]

    groupFileWriter = GroupFileWriterType.New()
    groupFileWriter.SetFileName(filename)
    groupFileWriter.SetInput(group)
    groupFileWriter.Update()
