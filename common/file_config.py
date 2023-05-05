#!/usr/bin/python3
import os
import platform


class FileConfig:

    def __init__(self):
        # 获取电脑系统平台
        self.computer_sys = platform.system()
        # 项目路径
        self.base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]



    def get_path(self, type="report_path"):
        self.allure_dir = ""
        self.htmlreport_dir = ""
        self.logs_dir = ""
        self.screenshot_dir = ""

        if platform.system() == "Windows":
            # Windows
            if type == "allure_report":
                # Allure报告路径
                self.allure_dir = os.path.join(self.base_dir, "Outputs\\allure_report")
                return self.allure_dir
            elif type == "pytest_report":
                # Pytest报告路径
                self.htmlreport_dir = os.path.join(self.base_dir, "Outputs\\pytest_report")
                return self.htmlreport_dir
            elif type == "logs":
                # Project运行日志路径
                self.logs_dir = os.path.join(self.base_dir, "Outputs\\running_logs")
                return self.logs_dir
            elif type == "screenshots":
                # Project运行截图路径
                self.screenshot_dir = os.path.join(self.base_dir, "Outputs\\running_screenshots")
                return self.screenshot_dir
            elif type == "Outputs":
                self.Outputs_dir = os.path.join(self.base_dir, "Outputs")
                return self.Outputs_dir
            else:
                # 填写设备信息路径
                self.message = "type选择范围：allure_report/pytest_report/logs/screenshots/Outputs"
                return self.message
        else:
            # Mac OR Linux
            if type == "allure_report":
                # Allure报告路径
                self.allure_dir = os.path.join(self.base_dir, "Outputs/allure_report")
                return self.allure_dir
            elif type == "pytest_report":
                # Pytest报告路径
                self.htmlreport_dir = os.path.join(self.base_dir, "Outputs/pytest_report")
                return self.htmlreport_dir
            elif type == "logs":
                # Project运行日志路径
                self.logs_dir = os.path.join(self.base_dir, "Outputs/running_logs")
                return self.logs_dir
            elif type == "screenshots":
                # Project运行截图路径
                self.screenshot_dir = os.path.join(self.base_dir, "Outputs/running_screenshots")
                return self.screenshot_dir
            elif type == "Outputs":
                self.Outputs_dir = os.path.join(self.base_dir, "Outputs")
                return self.Outputs_dir
            else:
                # 填写设备信息路径
                self.message = "type选择范围：allure_report/pytest_report/logs/screenshots/Outputs"
                return self.message


if __name__ == "__main__":
     print(FileConfig().get_path(type="logs"))
