# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Test
                                 A QGIS plugin
 Test
                             -------------------
        begin                : 2015-03-10
        copyright            : (C) 2015 by Nikolche Kolevski
        email                : nikolche.kolevski@gmail.com
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
    """Load Test class from file Test.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Test import Test
    return Test(iface)
