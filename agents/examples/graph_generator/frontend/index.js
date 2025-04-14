// 获取当前页面的主机名和端口
const currentHost = window.location.hostname;
const currentPort = window.location.port;

// 构建API URL
const apiBaseUrl = `http://${currentHost}:${currentPort}`;

// 重定向到正确的前端页面
window.location.href = `${apiBaseUrl}/index.html`; 