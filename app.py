from flask import Flask, render_template, request, send_file
from datetime import datetime
from io import BytesIO

app = Flask(__name__)
entries = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ticket = request.form['ticket']
        comment = request.form['comment']
        hours = request.form['hours']

        if ticket.lower() == "none":
            ticket_text = "No ticketed work"
        else:
            ticket_text = f"[INFRA2-{ticket}](https://eagleeyenetworks.atlassian.net/browse/INFRA2-{ticket})"

        entries.append((len(entries)+1, ticket_text, comment, hours))

    return render_template('index.html', entries=entries)

@app.route('/markdown')
def markdown_output():
    date_str = datetime.now().strftime("%Y-%m-%d")
    output = "| # | Ticket | Comment | Hours |\n"
    output += "|---|--------|---------|--------|\n"
    for entry in entries:
        output += f"| {entry[0]} | {entry[1]} | {entry[2]} | {entry[3]} |\n"
    final = f"My update for {date_str}\n\n{output}"
    return f"<pre>{final}</pre>"

@app.route('/download')
def download_markdown():
    date_str = datetime.now().strftime("%Y-%m-%d")
    content = f"My update for {date_str}\n\n"
    content += "| # | Ticket | Comment | Hours |\n"
    content += "|---|--------|---------|--------|\n"
    for entry in entries:
        content += f"| {entry[0]} | {entry[1]} | {entry[2]} | {entry[3]} |\n"

    buffer = BytesIO()
    buffer.write(content.encode('utf-8'))
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name="daily_update.md", mimetype='text/markdown')

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

