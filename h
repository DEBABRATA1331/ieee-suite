[1mdiff --git a/templates/dashboard.html b/templates/dashboard.html[m
[1mindex b27b35f..3d347fd 100644[m
[1m--- a/templates/dashboard.html[m
[1m+++ b/templates/dashboard.html[m
[36m@@ -112,7 +112,7 @@[m
         <p class="subtext">Today is {{ current_date }}. Have a productive day!</p>[m
 [m
         <div class="grid">[m
[31m-            {% if session.role == 'chair' %}[m
[32m+[m[32m            {% if role == 'chair' %}[m
             <div class="card">[m
                 <h3>Notice Generator</h3>[m
                 <p>Create formal notices with logos and signatures.</p>[m
[1mdiff --git a/templates/login.html b/templates/login.html[m
[1mindex 35595a5..e400788 100644[m
[1m--- a/templates/login.html[m
[1m+++ b/templates/login.html[m
[36m@@ -76,6 +76,10 @@[m
 <body>[m
     <form class="login-card" method="POST">[m
         <h2>IEEE ExCom Login</h2>[m
[32m+[m[32m        {% if error %}[m
[32m+[m[32m        <p style="color: red; text-align: center;">{{ error }}</p>[m
[32m+[m[32m        {% endif %}[m
[32m+[m
         <input type="text" name="username" placeholder="Username" required autofocus>[m
         <input type="password" name="password" placeholder="Password" required>[m
         <button type="submit">Login</button>[m
[1mdiff --git a/users.json b/users.json[m
[1mindex f0a77ff..8875f01 100644[m
[1m--- a/users.json[m
[1m+++ b/users.json[m
[36m@@ -3,23 +3,23 @@[m [mfrom werkzeug.security import generate_password_hash[m
 [m
 users = {[m
     "chair": {[m
[31m-        "password": generate_password_hash("ieee123"),[m
[32m+[m[32m        "password": str(generate_password_hash("ieee123")),[m
         "role": "chair"[m
     },[m
     "secretary": {[m
[31m-        "password": generate_password_hash("sb2024"),[m
[32m+[m[32m        "password": str(generate_password_hash("sb2024")),[m
         "role": "secretary"[m
     },[m
     "vicechair": {[m
[31m-        "password": generate_password_hash("vssutvc"),[m
[32m+[m[32m        "password": str(generate_password_hash("vssutvc")),[m
         "role": "vicechair"[m
     },[m
     "treasurer": {[m
[31m-        "password": generate_password_hash("bankieee"),[m
[32m+[m[32m        "password": str(generate_password_hash("bankieee")),[m
         "role": "treasurer"[m
     },[m
     "webmaster": {[m
[31m-        "password": generate_password_hash("ieeedev"),[m
[32m+[m[32m        "password": str(generate_password_hash("ieeedev")),[m
         "role": "webmaster"[m
     }[m
 }[m
[36m@@ -27,4 +27,4 @@[m [musers = {[m
 with open("users.json", "w") as f:[m
     json.dump(users, f, indent=4)[m
 [m
[31m-print("users.json created with hashed passwords and roles.")[m
[32m+[m[32mprint("users.json created with hashed passwords and roles.")[m
\ No newline at end of file[m
