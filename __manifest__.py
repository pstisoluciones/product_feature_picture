# -*- coding: utf-8 -*-
#######################################################################################
#                                                                                     #
#Copyright (C) Monoyer Fabian (info@olabs.be)                                         #
#                                                                                     #
#Odoo Proprietary License v1.0                                                        #
#                                                                                     #
#This software and associated files (the "Software") may only be used (executed,      #
#modified, executed after modifications) if you have purchased a valid license        #
#from the authors, typically via Odoo Apps, or if you have received a written         #
#agreement from the authors of the Software (see the COPYRIGHT file).                 #
#                                                                                     #
#You may develop Odoo modules that use the Software as a library (typically           #
#by depending on it, importing it and using its resources), but without copying       #
#any source code or material from the Software. You may distribute those              #
#modules under the license of your choice, provided that this license is              #
#compatible with the terms of the Odoo Proprietary License (For example:              #
#LGPL, MIT, or proprietary licenses similar to this one).                             #
#                                                                                     #
#It is forbidden to publish, distribute, sublicense, or sell copies of the Software   #
#or modified copies of the Software.                                                  #
#                                                                                     #
#The above copyright notice and this permission notice must be included in all        #
#copies or substantial portions of the Software.                                      #
#                                                                                     #
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR           #
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,             #
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.                                #
#IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,          #
#DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,     #
#ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER          #
#DEALINGS IN THE SOFTWARE.                                                            #
#######################################################################################
{
    'name': "Product Feature",
    'author': "O'Labs",
    'website': "http://www.olabs.be",
    'summary':'This module lets you add multi pictures and logo with description.',
    'description': """

    This module lets you add multi pictures and logo with description.
    The feature logos and descriptions that are related to certain highlighted production specifications, such as compliance with EnergyStar, USB3.0, Bluetooth or
    the presence of specific technology.
    Pictures and Logos can be provided in JPG or PNG image formats.
    Textual descriptions of the feature logo are language specific.

     """,
    'price':'19',
    'currency':'EUR',
    'category': 'Sale',
    'version': '1.1',
    'depends': [
        'product',
    ],
    'data': [
        "views/views.xml",
        "security/ir.model.access.csv",
       ],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'licence':"OEEL-1",

}

