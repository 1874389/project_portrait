# encoding: utf-8
# !/usr/bin/python3

import traceback

import MySQLdb as mdb

import const as const

# 数据库名
DB_NAME = 'project_portrait'
# 数据库表名
TABLE_NAME_FILE = "file"
TABLE_NAME_RESOURCE = "resource"
TABLE_NAME_REFERENCE = "reference"
TABLE_NAME_TARGET_DATA = "target_data"
TABLE_NAME_TAG = "tag"

# 数据库配置
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '1qaz@WSX',
    'db': DB_NAME,
    'charset': 'utf8'
}

"""
连接数据库
"""


def connect():
    const.dbconnect = mdb.connect(**config)

    # 如果使用事务引擎，可以设置自动提交事务，或者在每次操作完成后手动提交事务conn.commit()
    const.dbconnect.autocommit(True)


"""
断开数据库
"""


def disconnect():
    # 关闭数据库连接
    const.dbconnect.close()


"""
新建数据库
"""


def createDatabases():
    try:
        conn = const.dbconnect
        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        # 因该模块底层其实是调用CAPI的，所以，需要先得到当前指向数据库的指针。
        cursor.execute('DROP DATABASE IF EXISTS %s' % DB_NAME)
        cursor.execute('CREATE DATABASE IF NOT EXISTS %s' % DB_NAME)
    except:
        traceback.print_exc()
        # 发生错误时会滚
        conn.rollback()
    finally:
        # 关闭游标连接
        cursor.close()


"""
新建数据表
"""


def createTables():
    try:
        conn = const.dbconnect
        conn.select_db(DB_NAME)
        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()

        # 创建file表
        cursor.execute('DROP TABLE IF EXISTS %s' % TABLE_NAME_FILE)
        cursor.execute('CREATE TABLE %s('
                       'id bigint unsigned zerofill NOT NULL AUTO_INCREMENT,'
                       'type varchar(255) DEFAULT NULL,'
                       'full_name varchar(255) DEFAULT NULL,'
                       'path varchar(255) DEFAULT NULL,'
                       'name varchar(255) DEFAULT NULL,'
                       'suffix varchar(255) DEFAULT NULL,'
                       'class_full_name varchar(255) DEFAULT NULL,'
                       'line_count bigint DEFAULT NULL,'
                       'size bigint DEFAULT NULL,'
                       'PRIMARY KEY (id)'
                       ') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci'
                       % TABLE_NAME_FILE)

        # 创建resource表
        cursor.execute('DROP TABLE IF EXISTS %s' % TABLE_NAME_RESOURCE)
        cursor.execute('CREATE TABLE %s('
                       'id bigint unsigned zerofill NOT NULL AUTO_INCREMENT,'
                       'resource_type varchar(255) DEFAULT NULL,'
                       'resource_key varchar(255) DEFAULT NULL,'
                       'resource_value varchar(255) DEFAULT NULL,'
                       'file_id varchar(255) DEFAULT NULL, '
                       'file_full_name varchar(255) DEFAULT NULL,'
                       'PRIMARY KEY (id)'
                       ') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci'
                       % TABLE_NAME_RESOURCE)

        # 创建reference表
        cursor.execute('DROP TABLE IF EXISTS %s' % TABLE_NAME_REFERENCE)
        cursor.execute('CREATE TABLE %s('
                       'id bigint unsigned zerofill NOT NULL AUTO_INCREMENT,'
                       'file_id bigint DEFAULT NULL,'
                       'reference_data_id bigint DEFAULT NULL,'
                       'reference_data_type varchar(255) DEFAULT NULL, '
                       'reference_data varchar(255) DEFAULT NULL, '
                       'reference_line bigint DEFAULT NULL,'
                       'PRIMARY KEY (id)'
                       ') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci'
                       % TABLE_NAME_REFERENCE)

        # 创建targetData表
        cursor.execute('DROP TABLE IF EXISTS %s' % TABLE_NAME_TARGET_DATA)
        cursor.execute('CREATE TABLE %s('
                       'id bigint unsigned zerofill NOT NULL AUTO_INCREMENT,'
                       'file_id bigint DEFAULT NULL,'
                       'target_data varchar(255) DEFAULT NULL, '
                       'target_data_line bigint DEFAULT NULL,'
                       'PRIMARY KEY (id)'
                       ') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci'
                       % TABLE_NAME_TARGET_DATA)

        # 创建tag表
        cursor.execute('DROP TABLE IF EXISTS %s' % TABLE_NAME_TAG)
        cursor.execute('CREATE TABLE %s('
                       'id bigint unsigned zerofill NOT NULL AUTO_INCREMENT,'
                       'type varchar(255) DEFAULT NULL, '
                       'value varchar(255) DEFAULT NULL, '
                       'PRIMARY KEY (id)'
                       ') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci'
                       % TABLE_NAME_TAG)
    except:
        traceback.print_exc()
        # 发生错误时会滚
        conn.rollback()
    finally:
        # 关闭游标连接
        cursor.close()
