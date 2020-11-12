import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# Used to connect to mongodb
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# Used for session cookie
app.secret_key = os.environ.get("SECRET_KEY")
# creating mongodb using ["MONGO_URI"]
mongo = PyMongo(app)


# Main Page
@app.route("/")
def all_items():
    # Find all items in item database
    items = list(mongo.db.items.find())
    profiles = list(mongo.db.profile.find())
    profile_list = []
    # Create a list of users with profiles for comparison in items page
    for profile in profiles:
        profile_list.append(profile["username"])

    return render_template(
        "items.html", items=items, profile_list=profile_list)


# Registration modal
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Find a match in exsiting user database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # If a match is found and existing_user returns a username
        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("all_items"))
        # If no match is found
        else:
            # Store username/password into users database
            register = {"username": request.form.get("username").lower(),
                        "password": generate_password_hash(
                        request.form.get("password"))}
            mongo.db.users.insert_one(register)
            # Add username into session cookie
            session["user"] = request.form.get("username").lower()
            flash("You have been registered!")
            return redirect(url_for("all_items"))


# Login modal
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Locate any users with same username in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username2").lower()})
        if existing_user:
            # check if passwords are identical
            if check_password_hash(
                    existing_user["password"], request.form.get("password2")):
                # If match is obtained, save username to session cookie
                session["user"] = request.form.get("username2").lower()
                flash("Welcome, {}".format(request.form.get("username2")))
                return redirect(url_for("profile", username=session["user"]))
            # Password do not match
            else:
                flash("Incorrect Password/Password")
                return redirect(url_for("all_items"))
        else:
            # No username exists in user database
            flash("Incorrect Username/Password")
            return redirect(url_for("all_items"))


# Logout function
@app.route("/logout")
def logout():
    # Remove session cookie
    session.pop("user")
    flash("You have been logged out")
    return redirect(url_for("all_items"))


# Profile page
@app.route("/profile/<username>")
def profile(username):
    # Find user and profile database for username
    user = mongo.db.users.find_one({"username": username})
    profile = mongo.db.profile.find_one({"username": username})

    return render_template('profile.html', username=user, profile=profile)


# Add Profile info to profile page
@app.route("/add_profile", methods=["GET", "POST"])
def add_profile():
    if request.method == "POST":
        # Add image file to mongodb
        profile_image = request.files["profile_image"]
        mongo.save_file(profile_image.filename, profile_image)
        # Retreive all information from form
        new_item = {"profile_image": profile_image.filename,
                    "full_name": request.form.get("profile_fullname"),
                    "profile_description": request.form.get(
                        "profile_description"),
                    "username": session["user"]}

        # Insert new data into profile database in mongo.db
        mongo.db.profile.insert_one(new_item)
        flash("Profile has been created")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("add_profile.html")


# Function to edit Profile in database
@app.route("/edit_profile/<profile_id>", methods=["GET", "POST"])
def edit_profile(profile_id):
    if request.method == "POST":
        # Add image file to mongodb
        profile_image = request.files["profile_image"]
        mongo.save_file(profile_image.filename, profile_image)
        # Retreive all information from form
        # username not modifed
        new_item = {"profile_image": profile_image.filename,
                    "full_name": request.form.get("profile_fullname"),
                    "profile_description": request.form.get(
                        "profile_description")}

        # Insert new data into profile database in mongo.db
        mongo.db.profile.update_one(
            {"_id": ObjectId(profile_id)}, {"$set": new_item})
        flash("Profile has been Updated")
        return redirect(url_for("all_items"))

    profile = mongo.db.profile.find_one({"_id": ObjectId(profile_id)})

    return render_template("edit_profile.html", profile=profile)


# Funcion to delete profile from database
@app.route("/delete_profile/<profile_id>")
def delete_profile(profile_id):
    # Find file from mongodb with same profile_id
    profile = mongo.db.profile.find_one({"_id": ObjectId(profile_id)})
    # Find fs.files doc with matching filename
    fs_files = mongo.db.fs.files.find_one(
        {"filename": profile["profile_image"]})
    # Remove data from fs.files database using filename as reference
    mongo.db.fs.files.remove({"filename": profile["profile_image"]})
    # Remove data from fs.chunks database using files_id as reference
    mongo.db.fs.chunks.remove({"files_id": fs_files["_id"]})
    # Remove profile with specific profile_id
    mongo.db.profile.remove({"_id": ObjectId(profile_id)})
    flash("Profile has been deleted")

    # Redirect to profile page for user
    return redirect(url_for("profile", username=session["user"]))


# Function to retrieve form data from add_item page
# Save and retrieve file coding tutorial obtained from:
    #  https://www.youtube.com/watch?v=DsgAuceHha4
@app.route("/add_item", methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        # Add image file to mongodb
        item_image = request.files["item_image"]
        mongo.save_file(item_image.filename, item_image)
        new_item = {"item_category": request.form.get("item_category"),
                    "item_image": item_image.filename,
                    "item_name": request.form.get("item_name"),
                    "item_description": request.form.get("item_description"),
                    "item_price": request.form.get("item_price"),
                    "username": session["user"],
                    "contact_number": request.form.get("contact_number"),
                    "email": request.form.get("email")}
        # Insert data into items database in mongo.db
        mongo.db.items.insert_one(new_item)
        flash("Item has been inserted")
        return redirect(url_for("all_items"))
    categories = list(mongo.db.categories.find())
    return render_template("add_item.html", categories=categories)


# Function to edit items
@app.route("/edit_item/<item_id>", methods=["GET", "POST"])
def edit_item(item_id):
    if request.method == "POST":
        # Add image file to mongodb
        # username not modifed
        item_image = request.files["item_image"]
        mongo.save_file(item_image.filename, item_image)
        new_item = {"item_category": request.form.get("item_category"),
                    "item_image": item_image.filename,
                    "item_name": request.form.get("item_name"),
                    "item_description": request.form.get("item_description"),
                    "item_price": request.form.get("item_price"),
                    "contact_number": request.form.get("contact_number"),
                    "email": request.form.get("email")}
        # Update data in items database in mongo.db
        mongo.db.items.update_one(
            {"_id": ObjectId(item_id)}, {"$set": new_item})
        flash("Item has been Modified")
        return redirect(url_for("all_items"))

    item = mongo.db.items.find_one({"_id": ObjectId(item_id)})
    categories = mongo.db.categories.find()

    return render_template("edit_item.html", item=item, categories=categories)


# Function to delete items
@app.route("/delete_item/<item_id>")
def delete_item(item_id):
    # Obtain file from mongodb with same item_id
    item = mongo.db.items.find_one({"_id": ObjectId(item_id)})
    # Find fs.files doc with matching filename
    fs_files = mongo.db.fs.files.find_one({"filename": item["item_image"]})
    # Remove data from fs.files database using filename as reference
    mongo.db.fs.files.remove({"filename": item["item_image"]})
    # Remove data from fs.chunks database using files_id
    mongo.db.fs.chunks.remove({"files_id": fs_files["_id"]})
    # Remove complete item record of item with item_id
    mongo.db.items.remove({"_id": ObjectId(item_id)})
    flash("Item has been removed")
    return redirect(url_for("all_items"))


# Function to retrieve image
@app.route("/file/<filename>")
def file(filename):
    return mongo.send_file(filename)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
