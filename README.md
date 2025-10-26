# 📚 Django REST Framework Project

This project is a **Django REST Framework (DRF)**–based API system consisting of multiple apps, each demonstrating a different DRF approach — from function-based views to class-based views and viewsets. This extends what I learnt from Django for APIs Fourth Edition.

---

## 🚀 Project Overview

The project showcases:

* Use of **Function-Based Views**, **Class-Based Views**, and **ViewSets**
* Integration with **dj-rest-auth** and **django-allauth** for authentication and registration
* API documentation using **drf-spectacular**
* Custom **permissions** for secure and controlled access
* Support for **Swagger UI** and **ReDoc** for interactive API documentation

---

## 🧩 Applications Overview

### 1️⃣ **Library App (`books/`)**

* **Purpose:** Manage books in a library system.
* **View Type:** Function-Based Views
* **Serializer Type:** `serializers.Serializer`
* **Core Features:**

  * Create, read, update, and delete books
  * Each book includes basic details such as title, subtitle, author, and ISBN
* **Notable Design:**

  * Utilizes a custom decorator to attach serializers to function-based views for proper rendering in the DRF browsable interface.

**Example Model Structure:**

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
```

**Example Functional View:**

```python
@api_view(['GET', 'POST'])
@serializer(BookSerializer)
def book_list(request):
    ...
```

---

### 2️⃣ **To-Do App (`todo/`)**

* **Purpose:** Manage a to-do list where each task belongs to a user.
* **View Type:** Class-Based Views
* **Serializer Type:** `ModelSerializer`
* **Core Views Used:**

  * `ListCreateAPIView`
  * `RetrieveUpdateDestroyAPIView`
* **Custom Permissions:**

  * `IsAuthorOrIsNotPrivate` — allows access if:

    * The requesting user **is the author**, or
    * The to-do item **is not private** (`private=False`)

**Model Fields:**

```python
class Todo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    private = models.BooleanField(default=False)
```

**Filtering Logic in Views:**

```python
def get_queryset(self):
        # Base queryset
        queryset = Todo.objects.all()

        # Hide lists that are marked as private
        queryset = queryset.filter(private=False)

        # Also show user’s own private todos
        user = self.request.user
        if user.is_authenticated:
            queryset = queryset | Todo.objects.filter(author=user)

        return queryset
```

This ensures users only see:

* Their own to-dos, and
* To-dos made public by other users.

---

### 3️⃣ **Post App (`posts/`)**

* **Purpose:** Blog-like application for creating and managing posts.
* **View Type:** ViewSets (`ModelViewSet`)
* **Serializer Type:** `ModelSerializer`
* **Core ViewSets:**

  * `PostViewSet`
  * `UserViewSet`

**Model Fields:**

```python
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**Features:**

* Full CRUD (Create, Read, Update, Delete) functionality
* Linked to the authenticated user
* ViewSets are registered with routers for automatic URL generation

---

### 4️⃣ **Accounts App (`accounts/`)**

* **Purpose:** Manages user authentication and profile details.
* **Model:** `CustomUser` (extends Django’s base user model)
* **Authentication System:**

  * **dj-rest-auth** for API-based login, logout, and registration
  * **django-allauth** for email verification and user management

**Some Endpoints Provided:**

```
/api/dj-rest-auth/login/
/api/dj-rest-auth/logout/
/api/dj-rest-auth/registration/
/api/dj-rest-auth/password/reset/
/api/dj-rest-auth/password/change/
```

---

## 🔐 Authentication & Permissions

* **Authentication:** `dj-rest-auth` + `django-allauth`
* **Email Verification:** Enabled (`ACCOUNT_EMAIL_VERIFICATION = 'mandatory'`)
* **Custom Permission Classes:**

  * `IsAuthorOrIsNotPrivate` (used in the To-Do app)
  * `IsAuthorOrReadOnly` (Used in the Post app)

---

## 🧭 API Documentation

The project uses **drf-spectacular** to generate and serve API documentation in different formats.

| Type                      | URL Placeholder           |
| ------------------------- | ------------------------- |
| **Swagger UI**            | `api/schema/swagger-ui/` |
| **ReDoc UI**              | `api/schema/redoc/`   |
| **OpenAPI Schema (YAML)** | `api/schema/`  |

Example (if using `spectacular`):

```python
path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
```

---

## ⚙️ Tech Stack

* **Backend:** Django 5 + Django REST Framework
* **Authentication:** dj-rest-auth, django-allauth
* **Documentation:** drf-spectacular
* **Database:** SQLite (development)
* **Language:** Python 3.11+

---

## 📦 Installation & Setup

```bash
# 1️⃣ Clone the repository
git clone https://github.com/favour-olumese/drf_projects
cd drf_projects

# 2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate   # On Linux/Mac

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Apply migrations
python manage.py migrate

# 5️⃣ Create a superuser
python manage.py createsuperuser

# 6️⃣ Run development server
python manage.py runserver
```

---

## 🧪 Testing the API

You can test API endpoints using:

* **Browsable API:** via `/api-auth/login/`
* **Swagger UI:** `api/schema/swagger-ui/`
* **ReDoc UI:** `api/schema/redoc/`
* **Curl/Postman:** for manual testing

---

## 🧑‍💻 Example API Endpoints

| Endpoint                          | Method                   | Description                       |
| --------------------------------- | ------------------------ | --------------------------------- |
| `/api/books/`                     | `GET` / `POST`           | List or add books                 |
| `/api/todo/`                      | `GET` / `POST`           | List or create to-dos             |
| `/api/todo/<id>/`                 | `GET` / `PUT` / `DELETE` | Retrieve, update, or delete to-do |
| `/api/posts/`                     | `GET` / `POST`           | List or create blog posts         |
| `/api/post/users/`                     | `GET`                    | List users (for posts app). This can only be accessed by superuser.       |
| `/api/dj-rest-auth/registration/` | `POST`                   | Register new user                 |

---

## 📁 Project Structure

```
drf_projects/
│
├── accounts/           # Custom user model and authentication logic
├── books/              # Library app (function-based views)
├── drf_projects/       # Main project settings and URLs
├── todo/               # To-do app (class-based views)
├── posts/              # Blog app (viewsets)
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

---

## 📘 Possible Improvements

* Add filtering
* Implement JWT authentication (optional)
* Add image upload support for posts
* Add CI/CD pipeline

---

## 🧾 License

This project is open-source under the **MIT License**.
You’re free to modify, distribute, or use it as a reference for your own Django REST projects.