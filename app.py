import os
import uuid
import math
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
@app.route("/<page_number>")
#  Set default value to 0
def all_items(page_number=0):
    # Find all items in item database
    complete_item_list = list(mongo.db.items.find())
    profiles = list(mongo.db.profile.find())
    profile_list = []
    # Create a list of users with profiles for comparison in items page
    for profile in profiles:
        profile_list.append(profile["username"])

    # Pagination
    items_per_page = 5
    # Find first index of list to show on items page
    index_1 = int(page_number) * items_per_page
    # Slice items list depending on page number
    items = complete_item_list[index_1:(index_1)+items_per_page]
    # Total list count required to display paginations numbers
    total = (mongo.db.items.find()).count()
    links_number = math.ceil(total/items_per_page)
    link_list = list(range(links_number))

    return render_template(
        "items.html", profiles=profiles, profile_list=profile_list,
        items=items, links=link_list, page_number=int(page_number),
        total_links=links_number)


# For initial search with no page number
@app.route("/search", methods=["GET", "POST"])
# For page navigation when page number and query specified
@app.route("/search/<query>/<page_number>", methods=["GET", "POST"])
def search(page_number=0, query=""):
    # Check to verify if new search or previous search
    if request.method == "POST":
        # New request
        query = request.form.get("query")
    else:
        # Previous request with links being used to change page
        query == query
    # Obtain list of items matching search criteria
    complete_item_list = list(mongo.db.items.find(
        {"$text": {"$search": query}}))

    # Pagination
    items_per_page = 5
    # Find first index of list to show on items page
    index_1 = int(page_number) * items_per_page
    # Slice items list depending on page number
    items = complete_item_list[index_1:(index_1)+items_per_page]
    # Total list count required to display paginations numbers
    item_list_count = len(complete_item_list)
    links_number = math.ceil(item_list_count/items_per_page)
    link_list = list(range(links_number))
    # Query sent to be used as reference when changing pages
    return render_template(
        "search_items.html", items=items, links=link_list,
        page_number=int(page_number), total_links=links_number,
        total=item_list_count, query=query)


# Registration modal
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Find a match in exsiting user database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # Find a match in exsiting email database
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        # If a match is found and existing_user returns a username
        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("all_items"))
        # If exisiting email returns something
        elif existing_email:
            flash("Email already exists!")
            return redirect(url_for("all_items"))
        # If no match is found
        else:
            # Store username/password into users database
            register = {"username": request.form.get("username").lower(),
                        "password": generate_password_hash(
                        request.form.get("password")),
                        "contact_number": request.form.get("contact_number"),
                        "email": request.form.get("email")}
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
                flash("Incorrect Username/Password")
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
    items = list(mongo.db.items.find({"username": username}))
    return render_template(
        'profile.html', username=user, profile=profile, items=items)


# Add Profile info to profile page
@app.route("/add_profile", methods=["GET", "POST"])
def add_profile():
    if request.method == "POST":
        # Add image file to mongodb
        profile_image = request.files["profile_image"]
        # Create unique file name using UUID. Resource obtained from:
        # https://www.geeksforgeeks.org/generating-random-ids-using-uuid-python/
        unique_filename = str(uuid.uuid1())
        mongo.save_file(unique_filename, profile_image)
        # Retreive all information from form
        new_item = {"profile_image": unique_filename,
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
        # If image field has been changed
        if profile_image:
            # Remove fs.files and fs.chunks first associated with image
            # Find file from mongodb with same profile_id
            profile = mongo.db.profile.find_one({"_id": ObjectId(profile_id)})
            # Find fs.files doc with matching filename
            fs_files = mongo.db.fs.files.find_one(
                {"filename": profile["profile_image"]})
            # Remove data from fs.files database using filename as reference
            mongo.db.fs.files.remove({"filename": profile["profile_image"]})
            # Remove data from fs.chunks database using files_id as reference
            mongo.db.fs.chunks.remove({"files_id": fs_files["_id"]})

            # Create unique file name using UUID
            unique_filename = str(uuid.uuid1())
            mongo.save_file(unique_filename, profile_image)
            # Retrieve all information from form
            # username not modifed
            new_item = {"profile_image": unique_filename,
                        "full_name": request.form.get("profile_fullname"),
                        "profile_description": request.form.get(
                            "profile_description")}

            # update new data into profile database in mongo.db
            mongo.db.profile.update_one(
                {"_id": ObjectId(profile_id)}, {"$set": new_item})

            flash("Profile has been Updated")
            return redirect(url_for("profile", username=session["user"]))
        # If Image field is empty
        else:
            # Retreive all information from form
            # username and Image not modifed
            new_item = {"full_name": request.form.get("profile_fullname"),
                        "profile_description": request.form.get(
                            "profile_description")}

            # Update new data into profile database in mongo.db
            mongo.db.profile.update_one(
                {"_id": ObjectId(profile_id)}, {"$set": new_item})
            flash("Profile has been Updated")
            return redirect(url_for("profile", username=session["user"]))

    profile = mongo.db.profile.find_one({"_id": ObjectId(profile_id)})
    return render_template("edit_profile.html", profile=profile)


# Function to delete profile from database
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
        # Create unique file name using UUID
        unique_filename = str(uuid.uuid1())
        mongo.save_file(unique_filename, item_image)
        new_item = {"item_category": request.form.get("item_category"),
                    "item_image": unique_filename,
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
        # If image has been changed
        if item_image:
            # Remove fs.files and chunks first from database
            # Obtain file from mongodb with same item_id
            item = mongo.db.items.find_one({"_id": ObjectId(item_id)})
            # Find fs.files doc with matching filename
            fs_files = mongo.db.fs.files.find_one(
                {"filename": item["item_image"]})
            # Remove data from fs.files database using filename as reference
            mongo.db.fs.files.remove({"filename": item["item_image"]})
            # Remove data from fs.chunks database using files_id
            mongo.db.fs.chunks.remove({"files_id": fs_files["_id"]})
            # Update complete item record of item with item_id
            # Create unique filename to prevent duplication
            unique_filename = str(uuid.uuid1())
            mongo.save_file(unique_filename, item_image)
            new_item = {"item_category": request.form.get("item_category"),
                        "item_image": unique_filename,
                        "item_name": request.form.get("item_name"),
                        "item_description": request.form.get(
                            "item_description"),
                        "item_price": request.form.get("item_price"),
                        "contact_number": request.form.get("contact_number"),
                        "email": request.form.get("email")}
            # Update data in items database in mongo.db
            mongo.db.items.update_one(
                {"_id": ObjectId(item_id)}, {"$set": new_item})
            flash("Item has been Modified")
            return redirect(url_for("all_items"))
        # If image has not been updated
        else:
            new_item = {"item_category": request.form.get("item_category"),
                        "item_name": request.form.get("item_name"),
                        "item_description": request.form.get(
                            "item_description"),
                        "item_price": request.form.get("item_price"),
                        "contact_number": request.form.get("contact_number"),
                        "email": request.form.get("email")}
            # Update data in items database in mongo.db except for image file
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


# Add category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        # Add category to database
        mongo.db.categories.insert_one(
            {"category_name": request.form.get("category_name")})
        flash("Category has been inserted")
        return redirect(url_for("control_center"))
    return render_template("add_category.html")


# Edit category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        # Update datebase with updated category name
        updated_category = {"category_name": request.form.get("category_name")}
        mongo.db.categories.update_one(
            {"_id": ObjectId(category_id)}, {"$set": updated_category})
        flash("Category updated")
        return redirect(url_for("control_center"))
    # obtain category with category_id
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# Delete category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    # Remove category from database having matching id
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category has been removed")
    return redirect(url_for("control_center"))


# Control center
@app.route("/control_center")
@app.route("/control_center/<page_number>")
def control_center(page_number=0):
    profiles = list(mongo.db.profile.find())
    items = list(mongo.db.items.find())
    categories = list(mongo.db.categories.find())

    # Pagination
    items_per_page = 5
    # Find first index of list to show on items page
    index_1 = int(page_number) * items_per_page
    # Slice items list depending on page number
    items_list = items[index_1:(index_1)+items_per_page]
    # Total list count required to display paginations numbers
    total = (mongo.db.items.find()).count()
    links_number = math.ceil(total/items_per_page)
    link_list = list(range(links_number))

    return render_template(
        "control_center.html", profiles=profiles,
        items=items_list, categories=categories, links=link_list,
        page_number=int(page_number), total_links=links_number)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
