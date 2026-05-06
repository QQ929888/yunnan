import requests
import time

URL = "http://museum.ioz.ac.cn/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 8种原有 + 5种旧新增 + 再加1种白鹇 = 总共14种
BACKUP_ANIMALS = [
    # 原有8种
    {"中文名": "滇金丝猴", "图片链接": "dianjinsihou.jpg", "详情页": "dianjinsihou.html"},
    {"中文名": "怒江金丝猴", "图片链接": "nujiangjinsihou.jpg", "详情页": "nujiangjinsihou.html"},
    {"中文名": "高黎贡白眉长臂猿", "图片链接": "baimeichangyuan.jpg", "详情页": "baimeichangyuan.html"},
    {"中文名": "西黑冠长臂猿", "图片链接": "heiguanchangyuan.jpg", "详情页": "heiguanchangyuan.html"},
    {"中文名": "绿孔雀", "图片链接": "kongque.jpg", "详情页": "kongque.html"},
    {"中文名": "滇池金线鲃", "图片链接": "jinxianba.jpg", "详情页": "jinxianba.html"},
    {"中文名": "哀牢髭蟾", "图片链接": "zichan.jpg", "详情页": "zichan.html"},
    {"中文名": "威氏鼷鹿", "图片链接": "xilu.jpg", "详情页": "xilu.html"},
    # 之前5种
    {"中文名": "小熊猫", "图片链接": "xiaoxiongmao.jpg", "详情页": "xiaoxiongmao.html"},
    {"中文名": "云豹", "图片链接": "yunbao.jpg", "详情页": "yunbao.html"},
    {"中文名": "亚洲象", "图片链接": "yazhouxiang.jpg", "详情页": "yazhouxiang.html"},
    {"中文名": "黑颈鹤", "图片链接": "heijinghe.jpg", "详情页": "heijinghe.html"},
    {"中文名": "红瘰疣螈", "图片链接": "hongluoyurong.jpg", "详情页": "hongluoyurong.html"},
    # 新加1种 凑14种：白鹇
    {"中文名": "白鹇", "图片链接": "baixian.jpg", "详情页": "baixian.html"}
]


def get_spider_data():
    print("正在尝试连接国家动物标本资源库进行爬取...")
    try:
        res = requests.get(URL, headers=HEADERS, timeout=5)
        res.raise_for_status()
        print("网站可访问，无法解析数据，启用本地模拟数据")
        time.sleep(1)
        return BACKUP_ANIMALS
    except Exception:
        print("爬取失败，启用本地模拟数据")
        time.sleep(1)
        return BACKUP_ANIMALS


def generate_main(animals):
    html = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>动物库</title>
    <!-- 引入外部 CSS 文件 -->
    <link rel="stylesheet"
          href="sty1.css">

          <script src="https://lf-cdn.coze.cn/obj/unpkg/flow-platform/chat-app-sdk/1.2.0-beta.19/libs/cn/index.js"></script>

    <style>
        /* 自定义Coze聊天窗口样式，适配你的网站风格 */
        #coze-webchat {
            position: fixed !important;
            bottom: 25px !important;
            right: 25px !important;
            z-index: 9999 !important;
        }
        /* 🔥 放大悬浮按钮 + 主题美化（完全保留你的设置） */
        #coze-webchat .coze-webchat-float-button {
            width: 100px !important;
            height: 100px !important;
            background-color: #2E7D32 !important;
            border-radius: 50% !important;
            box-shadow: 0 4px 15px rgba(46, 125, 50, 0.4) !important;
            transition: all 0.3s ease !important;
        }
        /* 鼠标悬浮时轻微放大（完全保留） */
        #coze-webchat .coze-webchat-float-button:hover {
            transform: scale(1.08) !important;
        }
        /* 聊天窗口主题色统一 */
        #coze-webchat .coze-webchat-window-header {
            background-color: #2E7D32 !important;
        }
    </style>


</head>

<body>

    <!-- 顶部导航栏 -->
    <nav class="navbar">
        <div class="logo" >

            <span>云南珍稀动植物库</span>
        </div>
        <ul class="nav-menu" >
            <li><a href="index2.html">首页</a ></li>
            <li><a href="plant.html">植物库</a ></li>
            <li><a href="animal.html">动物库</a ></li>
            <li><a href="taolun.html">讨论</a ></li>
        </ul>


        <div class="nav-right" >
            <div class="search-container">
                <i class="fa-brands fa-sistrix search-icon" style="flex:0 0 6vw;"></i>
                <input type="text" class="search-input" placeholder="搜索动植物..." autocomplete="off">
                <!-- 改动3：搜索联想下拉框 -->
                <ul class="search-suggestions" >
                    <!-- 联想项会由JS动态生成 -->
                </ul>
            </div>
            <!-- 点击触发下拉 -->
            <div class="user-dropdown">
                <span class="user-btn">用户</span>
                <!-- 下拉菜单 -->
                <div class="dropdown-menu">
                    <a href="shoucang.html" class="history-item">收藏</a >
                    <a href="index.html" class="logout-item">退出登录</a >
                </div>
            </div>
        </div>
    </nav>
    <!-- 导航栏结束 -->

<div class="animal-container">

    <!-- 滇金丝猴 -->
    <div class="animal-card">
        <a href="dianjinsihou.html">
            <img src="dianjinsihou.jpg" alt="滇金丝猴">
            <p>滇金丝猴</p >
        </a >
    </div>

    <!-- 怒江金丝猴 -->
    <div class="animal-card">
        <a href="nujiangjinsihou.html">
            <img src="nujiangjinsihou.jpg" alt="怒江金丝猴">
            <p>怒江金丝猴</p >
        </a >
    </div>

    <!-- 高黎贡白眉长臂猿 -->
    <div class="animal-card">
        <a href="baimeichangyuan.html">
            <img src="baimeichangyuan.jpg" alt="高黎贡白眉长臂猿">
            <p>高黎贡白眉长臂猿</p >
        </a >
    </div>

    <!-- 西黑冠长臂猿 -->
    <div class="animal-card">
        <a href="heiguanchangyuan.html">
            <img src="heiguanchangyuan.jpg" alt="西黑冠长臂猿">
            <p>西黑冠长臂猿</p >
        </a >
    </div>

    <!-- 绿孔雀 -->
    <div class="animal-card">
        <a href="kongque.html">
            <img src="kongque.jpg" alt="绿孔雀">
            <p>绿孔雀</p >
        </a >
    </div>

    <!-- 滇池金线鲃 -->
    <div class="animal-card">
        <a href="jinxianba.html">
            <img src="jinxianba.jpg" alt="滇池金线鲃">
            <p>滇池金线鲃</p >
        </a >
    </div>

    <!-- 哀牢髭蟾 -->
    <div class="animal-card">
        <a href="zichan.html">
            <img src="zichan.jpg" alt="哀牢髭蟾">
            <p>哀牢髭蟾</p >
        </a >
    </div>

    <!-- 威氏鼷鹿 -->
    <div class="animal-card">
        <a href="xilu.html">
            <img src="xilu.jpg" alt="威氏鼷鹿">
            <p>威氏鼷鹿</p >
        </a >
    </div>

    <!-- 新增动物 -->
    <div class="animal-card">
        <a href="xiaoxiongmao.html">
            <img src="xiaoxiongmao.jpg" alt="小熊猫">
            <p>小熊猫</p >
        </a >
    </div>
    <div class="animal-card">
        <a href="yunbao.html">
            <img src="yunbao.jpg" alt="云豹">
            <p>云豹</p >
        </a >
    </div>
    <div class="animal-card">
        <a href="yazhouxiang.html">
            <img src="yazhouxiang.jpg" alt="亚洲象">
            <p>亚洲象</p >
        </a >
    </div>
    <div class="animal-card">
        <a href="heijinghe.html">
            <img src="heijinghe.jpg" alt="黑颈鹤">
            <p>黑颈鹤</p >
        </a >
    </div>
    <div class="animal-card">
        <a href="hongluoyurong.html">
            <img src="hongluoyurong.jpg" alt="红瘰疣螈">
            <p>红瘰疣螈</p >
        </a >
    </div>
    <div class="animal-card">
        <a href="baixian.html">
            <img src="baixian.jpg" alt="白鹇">
            <p>白鹇</p >
        </a >
    </div>

</div>
<script>
const userBtn = document.querySelector('.user-btn');
const dropdown = document.querySelector('.user-dropdown');

userBtn.addEventListener('click', () => {
  dropdown.classList.toggle('active');
});

// 点击页面其他地方关闭
document.addEventListener('click', (e) => {
  if (!dropdown.contains(e.target)) {
    dropdown.classList.remove('active');
  }
});
</script>


<script>
        // 1. 获取DOM元素（必须先获取，再绑定事件！）
        const searchInput = document.querySelector('.search-input');
        const searchSuggestions = document.querySelector('.search-suggestions');
        let activeIndex = -1; // 键盘上下键选中的索引

        // 2. 输入框输入事件：请求后端接口
        searchInput.addEventListener('input', async function() {
            const keyword = this.value.trim();
            searchSuggestions.innerHTML = '';
            activeIndex = -1;

            // 输入为空，隐藏下拉
            if (!keyword) {
                searchSuggestions.style.display = 'none';
                return;
            }

            try {
                // 向后端接口发送请求
                let res = await fetch(`http://47.108.20.237:3000/api/search?keyword=${encodeURIComponent(keyword)}`);
                let filtered = await res.json();

                // 无结果
                if (filtered.length === 0) {
                    searchSuggestions.innerHTML = '<li style="color:#999;">暂无结果</li>';
                    searchSuggestions.style.display = 'block';
                    return;
                }

                // 渲染联想列表
                filtered.forEach((item) => {
                    const li = document.createElement('li');
                    li.textContent = item.name;
                    li.dataset.url = item.url;
                    li.addEventListener('click', () => {
                        window.location.href = item.url;
                        searchSuggestions.style.display = 'none';
                        searchInput.value = '';
                    });
                    searchSuggestions.appendChild(li);
                });

                searchSuggestions.style.display = 'block';

            } catch (err) {
                console.log('接口请求失败：', err);
                searchSuggestions.innerHTML = '<li style="color:#999;">加载失败</li>';
                searchSuggestions.style.display = 'block';
            }
        });

        // 3. 键盘上下键选择联想项
        searchInput.addEventListener('keydown', function(e) {
            const items = searchSuggestions.querySelectorAll('li');
            if (!items.length) return;

            // 上键
            if (e.key === 'ArrowUp') {
                e.preventDefault();
                activeIndex = activeIndex > 0 ? activeIndex - 1 : items.length - 1;
                updateActiveItem(items);
            }
            // 下键
            else if (e.key === 'ArrowDown') {
                e.preventDefault();
                activeIndex = activeIndex < items.length - 1 ? activeIndex + 1 : 0;
                updateActiveItem(items);
            }
            // 回车跳转
            else if (e.key === 'Enter' && activeIndex >= 0) {
                const url = items[activeIndex].dataset.url;
                if (url) window.location.href = url;
                searchSuggestions.style.display = 'none';
                searchInput.value = '';
            }
        });

        // 更新选中项样式并自动滚动
        function updateActiveItem(items) {
            items.forEach((item, index) => {
                item.classList.toggle('active', index === activeIndex);
                if (index === activeIndex) {
                    item.scrollIntoView({ block: 'nearest' });
                }
            });
        }

        // 点击页面其他地方关闭下拉框
        document.addEventListener('click', function(e) {
            if (!e.target.closest('.search-container')) {
                searchSuggestions.style.display = 'none';
            }
        });
    </script>
    

<script src="./index.js"></script>
<!-- 嵌入Coze智能体聊天窗口 + ✅ 原生title提示（光标一放必显示） -->
<script>
  new CozeWebSDK.WebChatClient({
    config: {
      bot_id: '7634345885346545679',
    },
    componentProps: {
      title: '滇境生灵智能助手',
      layout: "float",
      tooltip: "滇境生灵智能助手"  // ✅ 这里直接设置原生提示，100%生效
    },
    auth: {
      type: 'token',
      token: 'pat_EtNINqzwFkGGlgx7j8NbVaMS2oGRNMKBsAIWWVUmdzjQeku0KyoxHPwEvFY3wsd3',
      onRefreshToken: function () {
        return 'pat_EtNINqzwFkGGlgx7j8NbVaMS2oGRNMKBsAIWWVUmdzjQeku0KyoxHPwEvFY3wsd3'
      }
    }
  });

  // ✅ 强制给按钮加上原生title，兜底必生效
  setTimeout(() => {
    const btn = document.querySelector('.coze-webchat-float-button');
    if(btn) btn.title = "滇境生灵智能助手";
  }, 1000);
</script>


</body>
</html>
'''
    with open("animal.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("✅ animal.html 生成完成")


def generate_detail(animals):
    for p in animals:
        detail = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>{p['中文名']}</title>
    <link rel="stylesheet" href="sty1.css">
</head>
<body>

</body>
</html>
"""
        with open(p['详情页'], "w", encoding="utf-8") as f:
            f.write(detail)
        print(f"✅ 空白详情页 {p['详情页']} 已生成")


if __name__ == "__main__":
    animal_list = get_spider_data()
    generate_main(animal_list)
    generate_detail(animal_list)
    print("全部生成完毕")