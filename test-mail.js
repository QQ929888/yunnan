const nodemailer = require('nodemailer');

// 这里是你的邮箱和授权码，已经填好
const transporter = nodemailer.createTransport({
    host: "smtp.qq.com",
    port: 465,
    secure: true,
    auth: {
        user: "2197223898@qq.com",
        pass: "hvobszghbjxodiie"
    }
});

// 直接发一封测试邮件给你自己
async function sendTestMail() {
    try {
        let result = await transporter.sendMail({
            from: `"测试发送" <2197223898@qq.com>`,
            to: "2197223898@qq.com",
            subject: "测试",
            text: "能收到这封邮件，说明你的邮箱和授权码完全没问题！"
        })
        console.log("✅ 成功！！！邮箱配置是对的！")
    } catch (error) {
        // 这里会打印出 为什么发不了 的真实原因
        console.log("❌ 发送失败！真实错误如下：")
        console.log(error)
    }
}

sendTestMail()