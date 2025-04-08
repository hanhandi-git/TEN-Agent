# 项目目录结构分析

这个项目是一个基于Next.js构建的TEN Agent应用程序，用于实时多模态AI交互。以下是目录结构的详细分析：

## 顶层目录

- `.dockerignore` - 指定Docker构建过程中要忽略的文件和目录
- `.gitignore` - 指定Git版本控制要忽略的文件和目录
- `.prettierrc.json` - Prettier代码格式化工具的配置文件
- `Dockerfile` - 用于构建Docker容器的配置文件
- `LICENSE` - MIT许可证文件
- `README.md` - 项目说明文档
- `components.json` - shadcn/ui组件库的配置文件
- `next-env.d.ts` - Next.js的TypeScript类型声明文件
- `next.config.mjs` - Next.js的配置文件
- `package.json` - 项目依赖和脚本配置
- `postcss.config.js` - PostCSS配置文件，包含Tailwind和移动端适配
- `src/` - 源代码目录

## src目录

### app目录

Next.js的App Router结构：

- `api/` - API路由
  - `agents/start/route.tsx` - 启动AI代理的API端点
- `global.css` - 全局CSS样式
- `layout.tsx` - 应用的根布局组件
- `page.tsx` - 主页面组件

### common目录

通用工具和常量：

- `constant.ts` - 应用常量定义
- `graph.ts` - 图形编辑和处理工具
- `hooks.ts` - 自定义React Hooks
- `index.ts` - 导出所有通用功能
- `mock.ts` - 模拟数据生成工具
- `moduleConfig.ts` - 模块配置和注册

### components目录

React组件：

- `Agent/` - 代理相关组件
  - `AudioVisualizer.tsx` - 音频可视化组件
  - `AvatarTrulience.tsx` - Trulience头像组件(文件列表中未显示但被引用)
- `Button/` - 按钮组件
  - `LoadingButton.tsx` - 带加载状态的按钮组件
- `Layout/` - 布局组件
  - `Header.tsx` - 页面头部组件(文件列表中未显示但被引用)
  - `Action.tsx` - 动作组件(文件列表中未显示但被引用)
- `Chat/` - 聊天相关组件
  - `ChatCard.tsx` - 聊天卡片组件(文件列表中未显示但被引用)
- `Dynamic/` - 动态加载的组件
  - `RTCCard.tsx` - RTC卡片组件(文件列表中未显示但被引用)
- `Icon/` - 图标组件(文件列表中未显示但被引用)
- `ui/` - UI组件(文件列表中未显示但被引用)
  - `sonner.tsx` - 通知组件(文件列表中未显示但被引用)

### manager目录

管理器类：

- `rtc/` - RTC(实时通信)管理器(文件列表中未显示但被引用)

### store目录

Redux状态管理：

- `reducers/` - Redux reducers(文件列表中未显示但被引用)
  - `global.ts` - 全局状态reducer(文件列表中未显示但被引用)
- `index.ts` - Redux store配置(文件列表中未显示但被引用)

### types目录

TypeScript类型定义(文件列表中未显示但被引用)

## 技术栈

- **前端框架**: Next.js 15
- **UI库**: shadcn/ui, Tailwind CSS
- **状态管理**: Redux Toolkit
- **实时通信**: Agora RTC SDK
- **容器化**: Docker
- **包管理**: pnpm
- **语言**: TypeScript

这个项目是一个实时多模态AI代理应用，支持语音、视觉和知识库访问，使用了现代的React和Next.js技术栈，并通过Docker进行容器化部署。
