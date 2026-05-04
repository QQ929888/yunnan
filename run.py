from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
import bcrypt
import random
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)

# ====================== 【你的云服务器 MySQL 配置】 ======================
DB_CONFIG = {
    "host": "47.108.20.237",
    "port": 3306,
    "user": "root",
    "password": "123456@xqxayjr",
    "database": "web_auth",
    "charset": "utf8mb4"
}

# ====================== 邮箱配置 ======================
MAIL_USER = "2197223898@qq.com"
MAIL_PASS = "isrtizgdyhvdebdg"
code_storage = {}


# ====================== 数据库连接函数 ======================
def get_db_conn():
    return pymysql.connect(**DB_CONFIG)


# ====================== 1. 注册接口（写入云服务器MySQL） ======================
@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    password = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt()).decode()

    conn = get_db_conn()
    cursor = conn.cursor()
    try:
        sql = """
        INSERT INTO users (username, email, password) 
        VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (username, email, password))
        conn.commit()
        print(f"✅ 注册成功：{username} | {email}")
        return jsonify({"code": 200, "msg": "注册成功"})
    except Exception as e:
        conn.rollback()
        print("❌ 注册失败：", e)
        return jsonify({"code": 400, "msg": "用户名或邮箱已存在"})
    finally:
        cursor.close()
        conn.close()


# ====================== 2. 登录接口 ======================
@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    res = cursor.fetchone()
    cursor.close()
    conn.close()

    if not res:
        return jsonify({"code": 400, "msg": "用户不存在"})
    if bcrypt.checkpw(password.encode(), res[0].encode()):
        return jsonify({"code": 200, "msg": "登录成功"})
    return jsonify({"code": 400, "msg": "密码错误"})


# ====================== 3. 发送验证码（修复中文编码） ======================
@app.route("/api/send-code", methods=["POST"])
def send_code():
    print("\n===== 发送验证码 =====")
    try:
        data = request.get_json()
        email = data["email"]
        print("前端邮箱：", email)

        conn = get_db_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        print("数据库查询结果：", user)
        if not user:
            return jsonify({"code": 400, "msg": "该邮箱未注册"})

        # 生成验证码
        code = str(random.randint(100000, 999999))
        code_storage[email] = code
        print("✅ 验证码：", code)

        # ========== 核心修复：强制utf-8编码，解决中文报错 ==========
        msg = MIMEText(f"找回密码验证码：{code}", "plain", "utf-8")
        msg["Subject"] = "找回密码"
        msg["From"] = MAIL_USER
        msg["To"] = email

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(MAIL_USER, MAIL_PASS)
        server.send_message(msg)
        server.quit()

        return jsonify({"code": 200, "msg": "验证码发送成功"})
    except Exception as e:
        print("❌ 发送失败：", e)
        return jsonify({"code": 500, "msg": "发送失败"})


# ====================== 4. 重置密码 ======================
@app.route("/api/reset-pwd", methods=["POST"])
def reset_pwd():
    data = request.get_json()
    email = data["email"]
    code = data["code"]
    new_pwd = data["newPwd"]

    if code_storage.get(email) != code:
        return jsonify({"code": 400, "msg": "验证码错误"})

    new_hash = bcrypt.hashpw(new_pwd.encode(), bcrypt.gensalt()).decode()
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password = %s WHERE email = %s", (new_hash, email))
    conn.commit()
    cursor.close()
    conn.close()

    del code_storage[email]
    return jsonify({"code": 200, "msg": "密码重置成功"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)