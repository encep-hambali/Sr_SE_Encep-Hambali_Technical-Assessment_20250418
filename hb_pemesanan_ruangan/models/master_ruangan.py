from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MasterRoom(models.Model):
    _name = 'master.ruangan'
    _description = 'Master Ruangan'

    name = fields.Char(string='Nama Ruangan', required=True)
    room_type = fields.Selection([
        ('meeting_small', 'Meeting Room Kecil'),
        ('meeting_large', 'Meeting Room Besar'),
        ('aula', 'Aula')
    ], string='Tipe Ruangan', required=True)
    location = fields.Selection([
        ('1A', '1A'),
        ('1B', '1B'),
        ('1C', '1C'),
        ('2A', '2A'),
        ('2B', '2B'),
        ('2C', '2C')
    ], string='Lokasi Ruangan', required=True)
    room_photo = fields.Binary(string='Foto Ruangan', required=True)
    capacity = fields.Integer(string='Kapasitas Ruangan', required=True)
    description = fields.Text(string='Keterangan')

    _sql_constraints = [
        ('unique_room_name', 'UNIQUE(name)', 'Nama Ruangan harus unik!'),
    ]
