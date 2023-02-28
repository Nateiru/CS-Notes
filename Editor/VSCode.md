# VSCode 配置

[toc]

## TIPS

> **[VScode快捷键(最全)](https://adong.blog.csdn.net/article/details/121996966?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-121996966-blog-100094155.t0_edu_mix&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-121996966-blog-100094155.t0_edu_mix&utm_relevant_index=1)**

### 使用技巧

**[锁定组](https://christianheilmann.com/2021/09/08/locking-editor-panes-in-visual-studio-code-helps-unwanted-multi-tab-experiences/)**：The locked group then shows a lock icon and no other files will open as tabs on it, even if it had the focus. 

相当于保持改页面作为最“顶”层，不会被新打开的页面覆盖。

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c19a8f5a-9423-4840-a720-b152ac79573d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230228T034705Z&X-Amz-Expires=86400&X-Amz-Signature=8765e8f0317ad4bd1bb612fb58d4a3c25d385c274d642c0608394dd039412534&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

通常打开终端，将其拖到右边，并锁定组如上图右上角有个🔒，那么就能保持终端不会吧别的页面覆盖。

## 快捷键

### 查找

- **查找文件：**`ctrl + p`
- **全局查找文件：**`ctrl + shift + f`
- **显示相关插件的命令**：`ctrl + shift + p`（遇事不决就按）
- **跳转至符号处：**`ctrl + shift + o`

> 冒号来进行分组：`@:`

![https://img-blog.csdnimg.cn/20191115211038104.png](https://img-blog.csdnimg.cn/20191115211038104.png)

**工作区符号跳转：`Ctrl + t`(下图所示)**

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4f74aac2-b7d3-482e-88a6-8afd71d2f7f1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230228T034745Z&X-Amz-Expires=86400&X-Amz-Signature=f3f16eca9be5db05414632db8da2988b2758403314534624fd346d73babd6e00&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

### 光标移动

- **按word移动光标：**`Ctrl + ←/→`
- **跳转行头/尾巴**：`Home`/`End`→ `ctrl + ;` /`ctrl + '`
- **移动一整行**：`alt+up/down`

### 基础编辑 Basic editing

- **选中文字**：`shift + left / right / up / down`
- **单行注释**：`ctrl+/`
- **删除当前行**：`ctrl+shift+k` → `ctrl+d`
- **删除上一个词**：`Ctrl + backspace`
- **行增加/减少缩进:** `ctrl + [` /`ctrl + ]`
- **显示/隐藏左侧目录栏：** `ctrl + b`
- **控制台终端显示与隐藏**：`ctrl + ~`
- **全局替换：**`ctrl + shift + h`
- **在当前行之前/后插入一行**：`Ctrl+Enter` /  `Ctrl+Shift+Enter`
- **格式化代码**：`Shift + Alt + F`

### 编辑/窗口管理

|     快捷键     |             作用             |
| :------------: | :--------------------------: |
| Ctrl + Shift+N |          打开新窗口          |
|     Ctrl+W     |           关闭窗口           |
|    Ctrl+F4     |       关闭当前编辑窗口       |
|    Ctrl+K F    |     关闭当前打开的文件夹     |
|    Ctrl+ \     | 拆分编辑器（最多拆分为三块） |
|   Ctrl+1/2/3   |   切换焦点在不同的拆分窗口   |
|    ctrl+Tab    |         切换工作窗口         |

## 插件

- **Reload**：重启软件
- **Auto Rename Tag**：修改html标签，自动帮你完成尾部闭合标签的同步修改，和webstorm一样。
- **Material Icon Theme**：让文件夹图标好看😍
- **One Dark Pro**：暗黑主题
- **Git Graph**：在VSCode可视化 Git 版本情况