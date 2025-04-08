<think>
我需要为用户提供TEN Agent项目的快速上手指南。根据README.md和其他相关文件的内容，这是一个关于构建AI语音/视频交互代理的框架。我应该提供一个简洁明了的指南，帮助用户理解项目并开始使用它。

首先，我应该回答用户的问题，解释TEN Agent是什么，然后提供项目设置和运行的步骤，包括环境要求、配置文件设置、构建和运行过程。

因为用户的问题是以中文提出的，根据指导我也应该用中文回答。
</think>

# TEN Agent 快速上手指南

## 项目简介

TEN Agent 是一个功能强大的框架，用于构建实时交互式AI代理，支持语音对话、视觉识别和多模态交互。它可以与多种LLM模型（如OpenAI、Gemini）集成，并提供丰富的扩展功能。

## 快速开始

### 基本要求

|类别|要求|
|---|---|
|**密钥**|• Agora App ID 和 App Certificate（每月提供免费分钟数）<br>• OpenAI API 密钥（或兼容的LLM）<br>• Deepgram ASR（注册可获得免费积分）<br>• Elevenlabs TTS（注册可获得免费积分）|
|**安装**|• Docker / Docker Compose<br>• Node.js(LTS) v18|
|**最低系统**|• CPU >= 2核<br>• RAM >= 4GB|

### 设置步骤

1. **克隆仓库**
   ```bash
   git clone https://github.com/TEN-framework/ten-agent.git
   cd ten-agent
   ```

2. **创建并配置.env文件**
   ```bash
   cp ./.env.example ./.env
   ```
   在.env文件中设置Agora App ID和App Certificate：
   ```
   AGORA_APP_ID=你的ID
   AGORA_APP_CERTIFICATE=你的证书
   ```

3. **启动开发容器**
   ```bash
   docker compose up -d
   ```

4. **进入容器**
   ```bash
   docker exec -it ten_agent_dev bash
   ```

5. **构建代理**
   ```bash
   # 在容器内执行以下命令，将 /app 添加为安全目录
   git config --global --add safe.directory /app
   # 执行任务
   task use
   ```

6. **启动Web服务器**
   ```bash
   task run
   ```

7. **配置Playground**
   
   打开浏览器访问[localhost:3000](http://localhost:3000)，配置你的代理：
   - 选择图类型（如语音代理、实时代理）
   - 选择相应模块
   - 选择扩展并配置API密钥设置

## 特色功能

TEN Agent提供多种强大功能，包括：

- **Trulience集成**：使用多样化免费头像选项构建AI头像
- **Deepseek R1兼容**：实现实时对话体验
- **ESP32支持**：在硬件设备上运行实时通信
- **Dify/Coze集成**：支持RAG（检索增强生成）能力
- **Gemini多模态API**：支持实时视觉和屏幕共享检测
- **故事讲述+图像生成**：创造沉浸式体验
- **丰富的扩展工具**：如天气检查、网络搜索等

## Apple Silicon注意事项

如果使用Apple Silicon Mac，请在Docker设置中取消选中"Use Rosetta for x86/amd64 emulation"选项。这可能会导致在ARM上构建速度较慢，但部署到x64服务器时性能将正常。

## 部署

一旦定制完成代理（通过Playground或直接编辑`property.json`），你可以通过创建Docker发布镜像来部署服务。详情请参阅[部署指南](https://doc.theten.ai/docs/ten_agent/deployment_ten_agent/deploy_agent_service)。

## 获取帮助

如需更多帮助：
- [Discord社区](https://discord.gg/VnPftUzAMJ)
- [GitHub讨论](https://github.com/TEN-framework/ten-agent/discussions)
- [文档](https://doc.theten.ai/docs/ten_agent/overview)

希望这个指南能帮助你快速上手TEN Agent项目！如有更多问题，请随时提问。
