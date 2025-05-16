from flask import Flask, render_template, request, send_file, redirect
import yt_dlp
import os
import uuid
import threading

app = Flask(__name__)
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def delete_file_later(filepath, delay=60):
    def remove():
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
                print(f"Deleted file: {filepath}")
        except Exception as e:
            print(f"Error deleting file: {e}")
    threading.Timer(delay, remove).start()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        return redirect(f"/info?url={url}")
    return render_template("index.html")

@app.route("/info")
def info():
    url = request.args.get("url")
    if not url:
        return redirect("/")

    ydl_opts = {'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        formats = [
            {
                "format_id": f["format_id"],
                "resolution": f.get("resolution") or f.get("height", "Unknown"),
                "filesize": f.get("filesize") or 0
            }
            for f in info['formats'] if f.get('filesize') and f.get('vcodec') != 'none'
        ]

    return render_template("info.html", title=info["title"], thumbnail=info["thumbnail"], formats=formats, url=url)

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")
    format_id = request.form.get("format_id")

    if not url or not format_id:
        return "Missing data", 400

    filename = f"{uuid.uuid4()}.mp4"
    filepath = os.path.join(DOWNLOAD_DIR, filename)

    ydl_opts = {
        'format': format_id,
        'outtmpl': filepath,
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        delete_file_later(filepath, delay=60)
        return send_file(filepath, as_attachment=True, download_name="video.mp4")

    except Exception as e:
        return f"Download failed: {str(e)}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

    
# developed with ❤ by Surajit 