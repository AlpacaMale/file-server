from flask import (
    Flask,
    request,
    Response,
    send_from_directory,
    render_template,
    redirect,
    flash,
)
import os
import time

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
SECRET_KEY = "your-secret"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["SECRET_KEY"] = SECRET_KEY
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET"])
def index():
    path = os.path.abspath(app.config["UPLOAD_FOLDER"])
    file_list = os.listdir(app.config["UPLOAD_FOLDER"])
    files = []
    for name in file_list:
        file_info = os.stat(f"{app.config["UPLOAD_FOLDER"]}/{name}")
        file = {
            "name": name,
            "size": human_readable(file_info.st_size),
            "ctime": time.ctime(file_info.st_ctime),
            "mtime": time.ctime(file_info.st_mtime),
        }
        files.append(file)
    return render_template("index.html", path=path, files=files)


@app.route("/files/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        flash("There is no file")
        return redirect("/")

    file = request.files["file"]

    if file.filename == "":
        flash("There is no file")
        return redirect("/")

    file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))

    flash("File uploaded successfully!")
    return redirect("/")


@app.route("/files/download/<filename>", methods=["GET"])
def download_file(filename):
    return send_from_directory(
        app.config["UPLOAD_FOLDER"], filename, as_attachment=True
    )


@app.route("/files/delete/<filename>", methods=["POST"])
def delete_file(filename):
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        flash(f"File '{filename}' deleted successfully!")
    else:
        flash("File not found")
    return redirect("/")


def human_readable(size):
    if size > 1073741824:
        size /= 1073741824
        return f"{size:.2f} GB"
    if size > 1048576:
        size /= 1048576
        return f"{size:.2f} MB"
    if size > 1024:
        size /= 1024
        return f"{size:.2f} KB"


if __name__ == "__main__":
    app.run(debug=True)
