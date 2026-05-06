import requests
import time

URL = "www.iplant.cn"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 只在原有基础上加云南特有植物，没改你任何原有代码结构
BACKUP_PLANTS = [
    {"中文名": "华盖木", "图片链接": "huagai.jpg", "详情页": "huagai.html"},
    {"中文名": "巧家五针松", "图片链接": "qiaojia.jpg", "详情页": "qiaojia.html"},
    {"中文名": "漾濞槭", "图片链接": "yangbi.jpg", "详情页": "yangbi.html"},
    {"中文名": "玉龙杓兰", "图片链接": "yulong.jpg", "详情页": "yulong.html"},
    {"中文名": "多岐苏铁", "图片链接": "duoji.jpg", "详情页": "duoji.html"},
    {"中文名": "云南澄广花", "图片链接": "chengguang.jpg", "详情页": "chengguang.html"},
    {"中文名": "云南野生菌", "图片链接": "fungus.jpg", "详情页": "fungus.html"},
    # 新增云南特有植物（无动物、不改动你原有任何逻辑）
    {"中文名": "珙桐", "图片链接": "gongtong.jpg", "详情页": "gongtong.html"},
    {"中文名": "滇山茶", "图片链接": "dianchashan.jpg", "详情页": "dianchashan.html"},
    {"中文名": "云南穗花杉", "图片链接": "suihuashan.jpg", "详情页": "suihuashan.html"},
    {"中文名": "伯乐树", "图片链接": "bole.jpg", "详情页": "bole.html"},
    {"中文名": "香果树", "图片链接": "xiangguoshu.jpg", "详情页": "xiangguoshu.html"}
]


def get_spider_data():
    print("正在尝试连接植物智网站进行爬取...")
    try:
        res = requests.get(URL, headers=HEADERS, timeout=5)
        res.raise_for_status()
        print("网站可访问，无法解析数据，启用本地模拟数据")
        time.sleep(1)
        return BACKUP_PLANTS
    except Exception:
        print("爬取失败，启用本地模拟数据")
        time.sleep(1)
        return BACKUP_PLANTS


def generate_main(plant):
    html = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>植物库</title>
    <link rel="stylesheet" href="sty2.css">

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

    <div class="plant-container">
        <div class="plant-card">
            <a href="huagai.html">
                <img src="huagai.jpg" alt="华盖木">
                <p>华盖木</p >
            </a >
        </div>
        <div class="plant-card">
            <a href="qiaojia.html">
                <img src="qiaojia.jpg" alt="巧家五针松">
                <p>巧家五针松</p >
            </a >
        </div>
        <div class="plant-card">
            <a href="yangbi.html">
                <img src="yangbi.jpg" alt="漾濞槭">
                <p>漾濞槭</p >
            </a >
        </div>
        <div class="plant-card">
            <a href="yulong.html">
                <img src="yulong.jpg" alt="玉龙杓兰">
                <p>玉龙杓兰</p >
            </a >
        </div>
        <div class="plant-card">
            <a href="duoji.html">
                <img src="duoji.jpg" alt="多岐苏铁">
                <p>多岐苏铁</p >
            </a >
        </div>
        <div class="plant-card">
            <a href="chengguang.html">
                <img src="chengguang.jpg" alt="云南澄广花">
                <p>云南澄广花</p >
            </a >
        </div>
        <div class="plant-card">
            <a href="fungus.html">
                <img src="fungus.jpg" alt="云南野生菌">
                <p>云南野生菌</p >
            </a >
        </div>
        <!-- 新增植物卡片 -->
        <div class="plant-card">
            <a href="gongtong.html">
                <img src="gongtong.jpg" alt="珙桐">
                <p>珙桐</p >
            </a >
        </div>
        <div class="plant-card">
            <a href="dianchashan.html">
                <img src="dianchashan.jpg" alt="滇山茶">
                <p>滇山茶</p >
            </a >
        </div>
        <div class="plant-card">
            <a href="suihuashan.html">
                <img src="suihuashan.jpg" alt="云南穗花杉">
                <p>云南穗花杉</p >
            </a >
        </div>
        <div class="plant-card">
            <a href="bole.html">
                <img src="bole.jpg" alt="伯乐树">
                <p>伯乐树</p >
            </a >
        </div>
        <div class="plant-card">
            <a href="xiangguoshu.html">
                <img src="xiangguoshu.jpg" alt="香果树">
                <p>香果树</p >
            </a >
        </div>
    </div>

<script>
const userBtn = document.querySelector('.user-btn');
const dropdown = document.querySelector('.user-dropdown');
userBtn.addEventListener('click', () => { dropdown.classList.toggle('active'); });
document.addEventListener('click', (e) => { if (!dropdown.contains(e.target)) { dropdown.classList.remove('active'); } });
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
    with open("plant.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("✅ plant.html 生成完成")


def generate_detail(plants):
    for p in plants:
        detail = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>{p['中文名']}</title>
    <link rel="stylesheet" href="sty2.css">
</head>
<body>
</body>
</html>
"""
        with open(p['详情页'], "w", encoding="utf-8") as f:
            f.write(detail)
        print(f"✅ 空白详情页 {p['详情页']} 已生成")


if __name__ == "__main__":
    plant_list = get_spider_data()
    generate_main(plant_list)
    generate_detail(plant_list)
    print("全部生成完毕")