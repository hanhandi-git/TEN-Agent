#!/bin/bash
set -e

echo "Setting up environment..."
# 解决 Git 安全性问题
git config --global --add safe.directory /app
export GOFLAGS='-buildvcs=false'

echo "Installing Graphviz..."
apt-get update && apt-get install -y graphviz curl

echo "Installing NVM and Node.js 18..."
# 安装 NVM (如果尚未安装)
if [ ! -d "$HOME/.nvm" ]; then
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
  
  # 添加 NVM 到 .bashrc
  echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.bashrc
  echo '[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"' >> ~/.bashrc
  echo '[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"' >> ~/.bashrc
fi

# 加载 NVM
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

# 安装 Node.js 18 (如果尚未安装)
if ! nvm ls 18 > /dev/null 2>&1; then
  nvm install 18
fi

# 使用 Node.js 18
nvm use 18

# 安装 mermaid-cli (如果尚未安装)
if ! command -v mmdc > /dev/null 2>&1; then
  npm install -g @mermaid-js/mermaid-cli
fi

echo "Setting up graph generator agent..."
cd /app
task use AGENT=agents/examples/graph_generator

echo "Building agent..."
task build

echo "Stopping existing instances..."
curl -X POST http://localhost:8080/stop -d '{"channel_name":"diagram_8159"}' || true

echo "Starting server..."
task run
