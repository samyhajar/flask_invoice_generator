from flask import Flask, request, render_template, send_file
import io
import os
from datetime import datetime
from weasyprint import HTML

app = Flask(__name__)

@app.route('/')
def hello_world():
    today = datetime.today().strftime("%B %-d, %Y")
    invoice_number = 123
    from_addr = {
        'company_name': 'Upleveled GmbH',
        'addr1': 'Lindengasse 7',
        'addr2': 'Wien, 1070',
        'UUID': '2729729'
    }
    to_addr = {
        'company_name': 'Samy Gmbh',
        'person_name': 'Samy Hajar',
        'person_email': 'samy.hajar@gmail.com'
    }
    items = [
        {
            'title': 'website design',
            'charge': 300.00
        },{
            'title': 'Hosting (3 months)',
            'charge': 75.00
        },{
            'title': 'Domain name (1 year)',
            'charge': 10.00
        }
    ]
    duedate = "August 1, 2018"
    total = sum([i['charge'] for i in items])
    rendered = render_template('invoice.html',
                            date = today,
                            from_addr = from_addr,
                            to_addr = to_addr,
                            items = items,
                            total = total,
                            invoice_number = invoice_number,
                            duedate = duedate)
    html = HTML(string=rendered)
    rendered_pdf = html.write_pdf('./static/invoice.pdf')
    return send_file(
            './static/invoice.pdf'
        )
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)