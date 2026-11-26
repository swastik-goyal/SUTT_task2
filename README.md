# Web Basics and My Django Polls Project

## 1. What happens when I type a URL and press Enter?

1. My browser reads the URL. For `localhost:8000/polls/`, the host is `localhost` and the path is `/polls/`.
2. DNS turns the name into an IP address, like a phone book. `localhost` means my own computer.
3. My browser connects to that IP and port. HTTP uses port 80, HTTPS uses 443, and Django's dev server uses 8000.
4. My browser sends an HTTP request: "GET `/polls/`".
5. The server works out the answer. In my project, Django runs Python and reads the database.
6. The server sends back a response with a status code and HTML.
7. My browser loads the CSS and images the HTML asks for, then draws the page.

## 2. Client and server

The **client** (my browser) asks for things. The **server** (`manage.py runserver`) waits and answers. The client always sends a request first, and the server sends a response. They both follow HTTP.

## 3. HTTP, request and response

HTTP is the shared language between browsers and servers.

- A **request** has a method (GET/POST), a URL, headers (my cookies, my browser), and sometimes a body (form data).
- A **response** has a status code, headers, and a body (HTML, an image, JSON).

## 4. GET vs POST

- **GET** asks for data. The data goes in the URL, and it doesn't change anything on the server. I use it to open a page or search.
- **POST** sends data to change something. The data goes in the hidden body. I use it for login, register, create poll, and vote.

In my project, opening `/polls/1/` is a GET. Clicking "Vote" is a POST to `/polls/1/vote/`.

## 5. Status codes

- **200**: success.
- **302**: redirect. After I vote, my app sends me to the results page. `@login_required` also uses it to send me to login.
- **404**: the page doesn't exist, like `/polls/999/`.
- **500**: the server's code crashed.

## 6. HTML, CSS, JavaScript

- **HTML** is the structure: text, forms, links.
- **CSS** is the style: colors, fonts, layout (my `style.css`).
- **JavaScript** is the behavior: making the page react. My project doesn't use it yet.

## 7. How a site remembers me

HTTP forgets me after every request. So when I log in, Django creates a **session** on the server. It sends my browser a **cookie** holding only a random `sessionid`. My browser sends that cookie with every request, so Django knows who I am. That's why `{% if user.is_authenticated %}` works on every page. The password is never stored in the cookie.

## 8. A request through Django

1. The request passes through the middleware (sessions, CSRF, auth).
2. `mysite/urls.py` sees `polls/` and passes the rest to `polls/urls.py`.
3. `polls/urls.py` picks the view, for example `IndexView`.
4. The view asks the model (`Question`) for data.
5. The model reads the database (`db.sqlite3`).
6. The template (`index.html`) turns the data into HTML.
7. The response goes back to my browser.

In short: URL → view → model → database → template → response.

## 9. Why `{% csrf_token %}`?

Browsers automatically send my login cookie to a site. Without protection, an evil page could secretly submit a form to my vote URL, and the server would think I did it. The tag adds a hidden random secret to my form. Django checks it on every POST, and a fake form can't know it, so it gets a 403 error. That's why all my POST forms have it.
