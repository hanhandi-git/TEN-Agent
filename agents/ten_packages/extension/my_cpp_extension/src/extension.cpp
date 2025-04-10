#include "include/extension.h"
#include <iostream>

namespace my_cpp_extension {

MyCppExtension::MyCppExtension(const std::string& name) : name_(name) {}

MyCppExtension::~MyCppExtension() {}

void MyCppExtension::OnInit(ten::TenEnv* ten_env) {
    ten_env->LogInfo("MyCppExtension initialized");
    ten_env->OnInitDone();
}

void MyCppExtension::OnStart(ten::TenEnv* ten_env) {
    ten_env->LogInfo("MyCppExtension started");
    
    // 读取配置属性
    std::string greeting;
    ten_env->GetPropertyString("greeting", &greeting);
    ten_env->LogInfo("Greeting property: " + greeting);
    
    // 发送一个示例数据
    ten::Data* output_data = ten::Data::Create("text_data");
    output_data->SetPropertyString("text", greeting);
    output_data->SetPropertyBool("end_of_segment", true);
    ten_env->SendData(output_data);
    
    ten_env->OnStartDone();
}

void MyCppExtension::OnData(ten::TenEnv* ten_env, ten::Data* data) {
    if (data->GetName() == "text_data") {
        std::string text;
        data->GetPropertyString("text", &text);
        ten_env->LogInfo("Received text: " + text);
        
        // 处理文本并回复
        std::string response = "You said: " + text;
        ten::Data* output_data = ten::Data::Create("text_data");
        output_data->SetPropertyString("text", response);
        output_data->SetPropertyBool("end_of_segment", true);
        ten_env->SendData(output_data);
    }
}

void MyCppExtension::OnCmd(ten::TenEnv* ten_env, ten::Cmd* cmd) {
    std::string cmd_name = cmd->GetName();
    ten_env->LogInfo("Received command: " + cmd_name);
    
    if (cmd_name == "hello") {
        ten::CmdResult* cmd_result = ten::CmdResult::Create(ten::StatusCode::OK);
        cmd_result->SetPropertyString("message", "Hello from C++ extension!");
        ten_env->ReturnResult(cmd_result, cmd);
    } else {
        ten::CmdResult* cmd_result = ten::CmdResult::Create(ten::StatusCode::ERROR);
        ten_env->ReturnResult(cmd_result, cmd);
    }
}

void MyCppExtension::OnStop(ten::TenEnv* ten_env) {
    ten_env->LogInfo("MyCppExtension stopped");
    ten_env->OnStopDone();
}

void MyCppExtension::OnDeinit(ten::TenEnv* ten_env) {
    ten_env->LogInfo("MyCppExtension deinitialized");
    ten_env->OnDeinitDone();
}

// 创建扩展实例的工厂函数
extern "C" {
    ten::Extension* CreateExtension(const char* name) {
        return new my_cpp_extension::MyCppExtension(name);
    }
}

} // namespace my_cpp_extension
