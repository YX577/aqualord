"""雨量站数据先从国电数据库中读取,需要对国电数据库里存储的降雨数据有比较清楚的认识,需要核对数据"""
import cx_Oracle

import read_config


def pixel_number_position(center_position_array, pixel_x_length, pixel_y_length, ):
    """Since we have done Guodian Project, data in Guodian Database should be utilized. The position of pixels in
    Guodian database need to be coordinated with the pixel we get from cma in order to utilize other codes,
    such as hydrology model, rain-gauge station position, etc. If the relationship of pixels in cma and guodian is
    one by one, we can store the value into database directly, else we should rescale the data. But the rescaling
    process is very troubling, so it is a better way to change data from database. """
    return


def connect_guodian_db():
    """connect to guodian database"""
    # 连接数据库，下面括号里内容根据自己实际情况填写
    url = read_config.read_radar_data_dir('config.ini', 'guodian-db', 'url')
    username = read_config.read_radar_data_dir('config.ini', 'guodian-db', 'username')
    password = read_config.read_radar_data_dir('config.ini', 'guodian-db', 'password')
    conn = cx_Oracle.connect(username + '/' + password + '@' + url + ':1521/ORCL')
    return conn


if __name__ == "__main__":
    connect_guodian_db()
