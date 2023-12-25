import logging

logging.basicConfig(
    level=logging.INFO,  # 设置日志级别为INFO
    format='%(asctime)s [%(levelname)s] %(message)s',  # 定义日志输出格式
    handlers=[
        logging.FileHandler(f'log/app.log'),  # 将日志写入文件
        logging.StreamHandler()  # 将日志打印到控制台
    ]
)


def print_f(content):
    logger = logging.getLogger()
    logger.info(content)
