# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Ungenerate
                                 A QGIS plugin
 make ArcInfo File
                             -------------------
        begin                : 2016-10-28
        copyright            : (C) 2016 by Peter Dudley
        email                : phdphd@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Ungenerate class from file Ungenerate.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Ungenerate import Ungenerate
    return Ungenerate(iface)
