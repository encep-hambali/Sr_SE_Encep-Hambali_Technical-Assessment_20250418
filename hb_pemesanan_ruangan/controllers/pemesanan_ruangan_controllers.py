from odoo import http
from odoo.http import request

class RoomBookingController(http.Controller):

    @http.route('/api/booking/status', type='json', auth='public', methods=['GET'], csrf=False)
    def get_booking_status(self):
        # Ambil booking_number dari semua parameter yang diterima
        booking_number = request.httprequest.args.get('booking_number')

        # Periksa apakah booking_number tidak ada
        if not booking_number:
            return http.Response("Booking number is required", status=400)

        booking = request.env['pemesanan.ruangan'].search([('name','=',booking_number)])
        print('booking : ', booking)
        if not booking:
            return request.make_response("Booking Not Found", 404)
        return {
            'booking_number': booking.name,
            'status': booking.state,
            'room': booking.room_id.name,
            'date': booking.booking_date,
        }