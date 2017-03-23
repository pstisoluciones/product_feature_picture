# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) Monoyer Fabian (info@olabs.be)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models,fields,api
from openerp import tools

class product_product(models.Model):
   _inherit = 'product.product'

   picture_ids=fields.One2many('product.feature.picture','product_id', string='Picture')
   logo_ids=fields.Many2many('product.feature.logo',string='Feature')

class product_template(models.Model):
   _inherit = 'product.template'

   picture_ids=fields.One2many('product.feature.picture','template_id',string='Picture')
   logo_ids=fields.Many2many('product.feature.logo',string='Feature')

class product_feature_picture(models.Model):
   _name = 'product.feature.picture'
   _rec_name ='name'

   name=fields.Char(compute="get_name",string="name",store=True)
   thumb=fields.Binary(compute="get_thumb",string='Thumb')
   picture=fields.Binary(string='Picture')
   sequence=fields.Integer(string="Sequence")
   product_id=fields.Many2one('product.product',string='Product')
   template_id=fields.Many2one('product.template',string='Product template')

   @api.one
   @api.depends("picture")
   def get_thumb(self):
         self.thumb=tools.image_get_resized_images(self.picture, avoid_resize_medium=True)["image_small"]

   @api.one
   @api.depends("product_id","template_id")
   def get_name(self):
         if self.product_id: self.name=self.product_id.name
         if self.template_id: self.name=self.template_id.name



class product_feature_logo(models.Model):
   _inherit = 'product.feature.picture'
   _name = 'product.feature.logo'
   _rec_name ='legend'
   legend=fields.Text(string='Legend', required=True,translate="True")






