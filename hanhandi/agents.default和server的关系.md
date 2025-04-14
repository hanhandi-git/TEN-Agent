



# TEN Agent default 配置中提供的服务

根据 `agents/examples/default/property.json` 文件，default 配置提供了三个主要的预定义图（服务），每个图代表一种不同类型的 AI 代理服务。以下是这些服务的详细分析：

## 1. voice_assistant（语音助手）

这是一个基本的语音交互助手，具有以下功能：

- **语音通信**：通过 Agora RTC 进行实时语音通信
- **语音识别**：使用 Deepgram ASR 将语音转换为文本
- **对话生成**：使用 OpenAI ChatGPT (Deepseek 模型) 生成回复
- **语音合成**：使用 Fish Audio TTS 将文本转换为语音
- **中断检测**：通过 interrupt_detector 检测用户中断
- **消息收集**：通过 message_collector 收集和管理消息
- **工具集成**：集成了天气查询工具 (weatherapi_tool_python)

这个服务适合基本的语音对话场景，用户可以通过语音提问，AI 会通过语音回答，并且可以查询天气信息。

## 2. voice_assistant_integrated_stt（集成语音识别的语音助手）

这是 voice_assistant 的变体，主要区别在于使用了 Agora 集成的语音识别（而不是单独的 Deepgram 服务）：

- **集成语音识别**：使用 Agora 内置的 Microsoft 语音识别服务
- **OpenAI 集成**：使用环境变量配置的 OpenAI 模型
- **图像生成工具**：集成了 OpenAI 图像生成工具

这个服务适合需要更紧密集成语音识别的场景，并且支持生成图像的功能，可以在对话中创建和分享图像。

## 3. story_teller_realtime（实时故事讲述器）

这是一个专门用于讲故事的服务，具有以下特点：

- **实时语音交互**：使用 Agora RTC 进行实时语音通信
- **实时语音到语音**：使用 OpenAI 的实时 V2V (Voice-to-Voice) 模型
- **图像生成**：集成了 OpenAI 图像生成工具
- **故事讲述**：专门配置为生成儿童图画书内容
- **交互式故事发展**：会提问引导故事发展方向
- **图文结合**：每个故事片段都会生成相应的图像

这个服务特别适合儿童教育和娱乐场景，可以实时生成故事并配以相应的图像，创造沉浸式的故事体验。

## 共同特点

所有这些服务都具有以下共同特点：

1. **实时通信**：使用 Agora RTC 进行实时语音通信
2. **多模态交互**：结合了语音、文本和（在某些情况下）图像
3. **消息管理**：使用 message_collector 收集和管理消息
4. **可配置性**：通过环境变量和配置参数高度可定制
5. **工具集成**：可以集成各种外部工具和服务

## 技术组件

这些服务使用了多种技术组件：

- **语音通信**：Agora RTC
- **语音识别**：Deepgram ASR 或 Agora 集成的 Microsoft 语音识别
- **对话模型**：OpenAI ChatGPT 或 GPT-4o Realtime
- **语音合成**：Fish Audio TTS
- **图像生成**：OpenAI 图像生成工具
- **工具集成**：天气 API 等

这些预定义的服务展示了 TEN 框架的灵活性和强大功能，可以根据不同需求组合各种组件，创建多样化的 AI 代理应用。






# TEN 框架中 server 组件的功能与 default 的关系

`server` 目录中定义了一个 HTTP 服务器，它作为 TEN 框架的管理层，负责创建、管理和控制 TEN Agent 实例。这个服务器与 `default` 配置的关系如下：

## server 服务的主要功能

1. **Agent 生命周期管理**：
   - 启动 (`/start`)：根据请求创建和启动新的 Agent 实例
   - 停止 (`/stop`)：终止运行中的 Agent
   - 保活 (`/ping`)：防止 Agent 因超时而被终止

2. **配置管理**：
   - 动态修改 `property.json` 配置
   - 根据请求参数选择特定的图 (graph)
   - 覆盖默认配置参数

3. **资源管理**：
   - 限制最大 Worker 数量
   - 管理 Worker 超时
   - 清理未正常终止的进程

4. **API 服务**：
   - 提供 RESTful API 接口
   - 生成 Agora 令牌
   - 列出可用的图和扩展

## server 与 default 的关系

`default` 目录中的配置（`manifest.json` 和 `property.json`）定义了一个默认的 Agent 应用，而 `server` 则是用来管理和启动这些 Agent 的服务：

1. **配置使用关系**：
   - 当通过 server 的 `/start` API 启动 Agent 时，可以指定使用 `default` 中定义的图
   - server 会读取 `property.json` 中的预定义图，并根据请求中的 `graph_name` 参数选择特定的图

2. **动态配置**：
   - server 允许在启动时动态修改 `default` 中定义的配置
   - 例如，可以覆盖 LLM 模型、API 密钥等参数，而无需修改原始配置文件

3. **多实例管理**：
   - server 可以同时管理多个基于 `default` 配置的 Agent 实例
   - 每个实例可以有不同的通道名称和配置参数

## 实际应用场景

在实际应用中，server 的作用是：

1. **Web 应用集成**：
   - Web 应用可以通过 server 的 API 动态创建和管理 Agent
   - 例如，当用户加入聊天时，Web 应用可以调用 `/start` API 启动一个 Agent

2. **多用户支持**：
   - 每个用户可以有自己的 Agent 实例，使用相同的基础配置但有不同的参数
   - server 负责管理这些实例的生命周期

3. **资源优化**：
   - 当用户离开时，可以停止相应的 Agent 以释放资源
   - 通过 ping 机制确保只有活跃的 Agent 继续运行

## 示例流程

1. 用户通过 Web 界面加入聊天
2. Web 应用调用 server 的 `/start` API，指定：
   - `channel_name`：用户的通道名
   - `graph_name`：使用 `default` 中定义的某个图（如 "voice_assistant"）
   - `properties`：可能覆盖某些配置参数
3. server 创建一个新的 Worker 进程，运行指定的 Agent
4. Web 应用定期调用 `/ping` 保持 Agent 活跃
5. 用户离开时，Web 应用调用 `/stop` 终止 Agent

总结来说，server 是一个管理层，它使得 `default` 和其他 Agent 配置可以被动态实例化、配置和管理，为 TEN 框架提供了更灵活的部署和使用方式。

