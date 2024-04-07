# 椭球高转海拔高
from pyproj import CRS, Transformer


def getAltitude(longitude, latitude, ellipsoid_height):
    # 定义WGS 84坐标系（经纬度和椭球高）
    wgs84_geodetic = CRS("EPSG:4326")

    # 定义WGS 84坐标系（经纬度和海拔高）
    wgs84_geoid = CRS("EPSG:4326+5773")

    # 创建一个从椭球高到海拔高的转换器
    transformer = Transformer.from_crs(
        wgs84_geodetic, wgs84_geoid, always_xy=True)

    # 转换到经纬度和海拔高
    longitude, latitude, altitude = transformer.transform(
        longitude, latitude, ellipsoid_height)

    return altitude


d = getAltitude(90.130466887, 44.652654458, 502)
print(d)
