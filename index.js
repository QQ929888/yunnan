console.log('Happy developing ✨')
// 获取元素
const loginBox = document.getElementById('loginBox');
const regBox = document.getElementById('regBox');
const toReg = document.getElementById('toReg');
const toLogin = document.getElementById('toLogin');

// 切换到注册
toReg.onclick = function () {
    loginBox.style.display = 'none';
    regBox.style.display = 'flex';
}

// 切换到登录
toLogin.onclick = function () {
    regBox.style.display = 'none';
    loginBox.style.display = 'flex';
}

// 登录按钮（可后续加逻辑）
document.getElementById('loginBtn').onclick = function () {
    const user = document.getElementById('loginUser').value;
    const pwd = document.getElementById('loginPwd').value;
    if (!user || !pwd) {
        alert('请输入账号和密码');
        return;
    }
    alert('登录成功！');
}

// 注册按钮（可后续加逻辑）
document.getElementById('regBtn').onclick = function () {
    const user = document.getElementById('regUser').value;
    const pwd = document.getElementById('regPwd').value;
    const pwd2 = document.getElementById('regPwd2').value;

    if (!user || !pwd || !pwd2) {
        alert('请填写完整信息');
        return;
    }
    if (pwd !== pwd2) {
        alert('两次密码不一致');
        return;
    }
    alert('注册成功！请登录');
    regBox.style.display = 'none';
    loginBox.style.display = 'flex';
}
