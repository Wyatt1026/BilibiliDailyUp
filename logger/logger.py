import logging
from logging.handlers import TimedRotatingFileHandler
import os
from datetime import datetime

class BilibiliLogger:
    def __init__(self, name: str = "app", log_dir: str = "log", level=logging.INFO):
        self.name = name
        self.log_dir = log_dir
        today_str = datetime.now().strftime('%Y-%m-%d')
        self.log_path = os.path.join(log_dir, f"{today_str}.log")
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # 防止重复添加 handler
        if not self.logger.handlers:
            os.makedirs(log_dir, exist_ok=True)

            formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

            # 按天分文件：每天创建一个新的日志文件，保留7天
            file_handler = logging.FileHandler(self.log_path, encoding='utf-8')

            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    # 基础日志封装
    def info(self, msg): self.logger.info(msg)
    def error(self, msg): self.logger.error(msg)
    def debug(self, msg): self.logger.debug(msg)
    def warning(self, msg): self.logger.warning(msg)

    # 标记运行起点
    def start(self):
        self.logger.info(f"=== SCRIPT START [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ===")

    # 标记运行终点
    def end(self):
        self.logger.info(f"=== SCRIPT END   [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ===")

    # 提取本次运行日志段
    def extract_latest_log(self) -> str:
        if not os.path.exists(self.log_path):
            return "⚠️ 日志文件不存在，无法提取日志段。"

        with open(self.log_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        start_idx = None
        end_idx = None

        for i in reversed(range(len(lines))):
            if end_idx is None and "=== SCRIPT END" in lines[i]:
                end_idx = i
            elif end_idx is not None and "=== SCRIPT START" in lines[i]:
                start_idx = i
                break

        if start_idx is not None and end_idx is not None and start_idx < end_idx:
            return ''.join(lines[start_idx:end_idx + 1])
        else:
            return "⚠️ 本次运行日志标记不完整，无法提取日志段落。"
