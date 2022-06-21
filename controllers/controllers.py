# -*- coding: utf-8 -*-
import json
from datetime import datetime

from odoo import fields, http
from odoo.http import request


class Rfid(http.Controller):

    @http.route('/rfid', type='json', auth='none', methods=['POST'], csrf=False)
    def log_read(self, **post):
        data = json.loads(request.httprequest.data)

        # Some conditions to ensure the data is coming from the Zebra device.
        if data['reader_name'] and data['mac_address']:

            reader = request.env['rfid.reader'].sudo().search([("name","=",data['reader_name']),("mac_address","=",data['mac_address'])], limit=1)
            
            if reader.id == False:
                reader = request.env['rfid.reader'].sudo().create({
                    "name": data['reader_name'],
                    "mac_address": data['mac_address'],
                    })
            
            for read in data['tag_reads']:            
                # TODO Validate the timestamp format, the documentation describes UTC or Unix format but the examples have an extra colon for the millisecond float.
                timeStamp = datetime.strptime(read['timeStamp'], "%d/%m/%Y %H:%M:%S.%f")

                if read['isHeartBeat'] == 'true':
                    request.env['rfid.reads.heartbeat'].sudo().create({
                        "reader": reader.id,
                        "timeStamp": timeStamp,
                        })
                else:
                    request.env['rfid.reads.tag'].sudo().create({
                        "reader": reader.id,
                        "epc":read['epc'],
                        "pc":read['pc'],
                        "antennaPort":read['antennaPort'],
                        "peakRssi":read['peakRssi'],
                        "seenCount":read['seenCount'],
                        "timeStamp": timeStamp,
                        "phase":read['phase'],
                        "channelIndex":read['channelIndex'],
                        })
