from flask import Flask, render_template, request, send_file
from datetime import datetime
from io import BytesIO
import os

app = Flask(__name__)
entries = []
additional_comments = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    global additional_comments

    if request.method == 'POST':
        ticket = request.form['ticket']
        priority = request.form['priority']
        comment = request.form['comment']
        hours = request.form['hours']
        additional_comments = request.form['additional_comments']

        if ticket.lower() == "none":
            ticket_text = "No ticketed work"
        else:
            ticket_text = f"[INFRA2-{ticket}](https://eagleeyenetworks.atlassian.net/browse/INFRA2-{ticket})"

        entries.append((len(entries)+1, ticket_text, priority, comment, hours))

    return render_template('index.html', entries=entries, additional_comments=additional_comments)

@app.route('/markdown')
def markdown_output():
    date_str = datetime.now().strftime("%Y-%m-%d")
    output = "| # | Ticket | Priority | Comment | Hours |\n"
    output += "|---|--------|----------|---------|--------|\n"
    for entry in entries:
        output += f"| {entry[0]} | {entry[1]} | {entry[2]} | {entry[3]} | {entry[4]} |\n"
    final = f"My update for {date_str}\n\n{output}\n"

    if additional_comments.strip():
        final += "Additional Comments:\n"
        for line in additional_comments.strip().splitlines():
            final += f"- {line}\n"

    return f"<pre>{final}</pre>"

@app.route('/download')
def download_markdown():
    date_str = datetime.now().strftime("%Y-%m-%d")
    content = f"My update for {date_str}\n\n"
    content += "| # | Ticket | Priority | Comment | Hours |\n"
    content += "|---|--------|----------|---------|--------|\n"
    for entry in entries:
        content += f"| {entry[0]} | {entry[1]} | {entry[2]} | {entry[3]} | {entry[4]} |\n"

    if additional_comments.strip():
        content += "\nAdditional Comments:\n"
        for line in additional_comments.strip().splitlines():
            content += f"- {line}\n"

    buffer = BytesIO()
    buffer.write(content.encode('utf-8'))
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name="daily_update.md", mimetype='text/markdown')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

@app.route('/clear', methods=['POST'])
def clear_entries():
    global entries, additional_comments
    entries = []
    additional_comments = ""
    return render_template('index.html', entries=entries, additional_comments=additional_comments)
