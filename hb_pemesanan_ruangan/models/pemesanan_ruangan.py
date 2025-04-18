from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Booking(models.Model):
    _name = 'pemesanan.ruangan'
    _description = 'Pemesanan Ruangan'

    name = fields.Char(string='Nomor Pemesanan', required=True, copy=False, readonly=True, index=True,
                       default=lambda self: self.env['ir.sequence'].next_by_code('pemesanan.ruangan'))
    room_id = fields.Many2one('master.ruangan', string='Ruangan', required=True)
    booking_name = fields.Char(string='Nama Pemesanan', required=True)
    booking_date = fields.Date(string='Tanggal Pemesanan', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'On Going'),
        ('done', 'Done'),
    ], default='draft',
    readonly=True)
    notes = fields.Text(string='Catatan Pemesanan')

    _sql_constraints = [
        ('unique_booking_name', 'UNIQUE(booking_name)', 'Nama Pemesanan tidak boleh sama!'),
        ('check_booking_conflict',
         'CHECK (NOT EXISTS (SELECT 1 FROM room_booking WHERE room_id = room_id AND booking_date = booking_date AND id != id))',
         'Ruangan sudah dipesan pada tanggal ini!'),
    ]

    @api.constrains('booking_name')
    def _check_unique_booking_name(self):
        for record in self:
            if self.search_count([('booking_name', '=', record.booking_name)]) > 1:
                raise ValidationError("Nama Pemesanan tidak boleh sama!")

    def action_confirm(self):
        """Metode untuk memproses pemesanan dan mengubah status menjadi ongoing."""
        for record in self:
            if record.state == 'draft':
                record.state = 'ongoing'  # Ubah status menjadi 'On Going'

    def action_done(self):
        """Metode untuk menyelesaikan pemesanan dan mengubah status menjadi done."""
        for record in self:
            if record.state == 'ongoing':
                            record.state = 'done'  # Ubah status menjadi 'Done'