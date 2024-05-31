# 略
import math


class GeoPosConv:
    def __init__(self):
        self.m_x_ = 0
        self.m_y_ = 0
        self.m_z_ = 0
        self.m_lat_ = 0
        self.m_lon_ = 0
        self.m_h_ = 0
        self.m_PLato_ = 0
        self.m_PLo_ = 0
        self.x_init_ = 0
        self.y_init_ = 0
        self.z_init_ = 0

    def x(self):
        return self.m_x_

    def y(self):
        return self.m_y_

    def z(self):
        return self.m_z_

    def x_err(self):
        return self.x_init_ - self.m_x_

    def y_err(self):
        return self.y_init_ - self.m_y_

    def z_err(self):
        return self.z_init_ - self.m_z_

    def set_x_init(self, x_init):
        self.x_init_ = x_init

    def set_y_init(self, y_init):
        self.y_init_ = y_init

    def set_z_init(self, z_init):
        self.z_init_ = z_init

    def set_plane(self, lat, lon):
        self.m_PLato_ = lat
        self.m_PLo_ = lon

    def set_plane_by_num(self, num):
        # 这里省略了详细的经纬度映射逻辑...
        # 假设我们已经根据num得到了经纬度
        lon_deg, lon_min, lat_deg, lat_min = self.get_plane_coord_by_num(num)

        # 将经纬度转换为弧度
        self.m_PLo_ = math.pi * (lat_deg + lat_min / 60.0) / 180.0
        self.m_PLato_ = math.pi * (lon_deg + lon_min / 60.0) / 180.0

    def get_plane_coord_by_num(self, num):
        # 这里应该是一个查找表或者逻辑来得到经纬度
        # 以下是示例逻辑
        if num == 0:
            lon_deg = 31
            lon_min = 4.622494026
            lat_deg = 121
            lat_min = 23.43820537
        # ... 其他情况 ...
        return lon_deg, lon_min, lat_deg, lat_min

    def set_llh_nmea_degrees(self, latd, lond, h):
        lad = math.floor(latd / 100.0)
        lat = latd - lad * 100.0
        lod = math.floor(lond / 100.0)
        lon = lond - lod * 100.0

        self.m_lat_ = (lad + lat / 60.0) * math.pi / 180
        self.m_lon_ = (lod + lon / 60.0) * math.pi / 180
        self.m_h_ = h

        self.conv_llh2xyz()

    def llh_to_xyz(self, lat, lon, ele):
        self.m_lat_ = lat * math.pi / 180
        self.m_lon_ = lon * math.pi / 180
        self.m_h_ = ele
        self.conv_llh2xyz()

    def conv_llh2xyz(self):

        # double self.PS;  //
        # double self.PSo; //
        # double self.PDL; //
        # double self.Pt;  //
        # double self.PN;  //
        # double self.PW;  //

        # double self.PB1, self.PB2, self.PB3, self.PB4, self.PB5, self.PB6, self.PB7, self.PB8, self.PB9;
        # double self.PA, self.PB, self.PC, self.PD, self.PE, self.PF, self.PG, self.PH, PI;
        # double self.Pe;  //
        # double self.Pet; //
        # double self.Pnn; //
        # double self.AW, FW, self.Pmo;

        self.Pmo = 0.9999

        # /*WGS84 self.Parameters*/
        self.AW = 6378137.0  # // Semi-major Axis
        self.FW = 1.0 / 298.257222101  # // 298.257223563 //Geometrical flattening

        self.Pe = math.sqrt(2.0 * self.FW - math.pow(self.FW, 2))
        self.Pet = math.sqrt(math.pow(self.Pe, 2) /
                             (1.0 - math.pow(self.Pe, 2)))

        self.PA = 1.0 + 3.0 / 4.0 * math.pow(self.Pe, 2) + 45.0 / 64.0 * math.pow(self.Pe, 4) + 175.0 / 256.0 * math.pow(self.Pe, 6) + 11025.0 / 16384.0 * math.pow(self.Pe, 8) + 43659.0 / 65536.0 * math.pow(
            self.Pe, 10) + 693693.0 / 1048576.0 * math.pow(self.Pe, 12) + 19324305.0 / 29360128.0 * math.pow(self.Pe, 14) + 4927697775.0 / 7516192768.0 * math.pow(self.Pe, 16)

        self.PB = 3.0 / 4.0 * math.pow(self.Pe, 2) + 15.0 / 16.0 * math.pow(self.Pe, 4) + 525.0 / 512.0 * math.pow(self.Pe, 6) + 2205.0 / 2048.0 * math.pow(self.Pe, 8) + 72765.0 / 65536.0 * math.pow(
            self.Pe, 10) + 297297.0 / 262144.0 * math.pow(self.Pe, 12) + 135270135.0 / 117440512.0 * math.pow(self.Pe, 14) + 547521975.0 / 469762048.0 * math.pow(self.Pe, 16)

        self.PC = 15.0 / 64.0 * math.pow(self.Pe, 4) + 105.0 / 256.0 * math.pow(self.Pe, 6) + 2205.0 / 4096.0 * math.pow(self.Pe, 8) + 10395.0 / 16384.0 * math.pow(
            self.Pe, 10) + 1486485.0 / 2097152.0 * math.pow(self.Pe, 12) + 45090045.0 / 58720256.0 * math.pow(self.Pe, 14) + 766530765.0 / 939524096.0 * math.pow(self.Pe, 16)

        self.PD = 35.0 / 512.0 * math.pow(self.Pe, 6) + 315.0 / 2048.0 * math.pow(self.Pe, 8) + 31185.0 / 131072.0 * math.pow(self.Pe, 10) + 165165.0 / \
            524288.0 * math.pow(self.Pe, 12) + 45090045.0 / 117440512.0 * math.pow(
                self.Pe, 14) + 209053845.0 / 469762048.0 * math.pow(self.Pe, 16)

        self.PE = 315.0 / 16384.0 * math.pow(self.Pe, 8) + 3465.0 / 65536.0 * math.pow(self.Pe, 10) + 99099.0 / 1048576.0 * math.pow(
            self.Pe, 12) + 4099095.0 / 29360128.0 * math.pow(self.Pe, 14) + 348423075.0 / 1879048192.0 * math.pow(self.Pe, 16)

        self.PF = 693.0 / 131072.0 * math.pow(self.Pe, 10) + 9009.0 / 524288.0 * math.pow(
            self.Pe, 12) + 4099095.0 / 117440512.0 * math.pow(self.Pe, 14) + 26801775.0 / 469762048.0 * math.pow(self.Pe, 16)

        self.PG = 3003.0 / 2097152.0 * math.pow(self.Pe, 12) + 315315.0 / 58720256.0 * math.pow(
            self.Pe, 14) + 11486475.0 / 939524096.0 * math.pow(self.Pe, 16)

        self.PH = 45045.0 / 117440512.0 * \
            math.pow(self.Pe, 14) + 765765.0 / \
            469762048.0 * math.pow(self.Pe, 16)

        PI = 765765.0 / 7516192768.0 * math.pow(self.Pe, 16)

        self.PB1 = self.AW * (1.0 - math.pow(self.Pe, 2)) * self.PA
        self.PB2 = self.AW * (1.0 - math.pow(self.Pe, 2)) * self.PB / -2.0
        self.PB3 = self.AW * (1.0 - math.pow(self.Pe, 2)) * self.PC / 4.0
        self.PB4 = self.AW * (1.0 - math.pow(self.Pe, 2)) * self.PD / -6.0
        self.PB5 = self.AW * (1.0 - math.pow(self.Pe, 2)) * self.PE / 8.0
        self.PB6 = self.AW * (1.0 - math.pow(self.Pe, 2)) * self.PF / -10.0
        self.PB7 = self.AW * (1.0 - math.pow(self.Pe, 2)) * self.PG / 12.0
        self.PB8 = self.AW * (1.0 - math.pow(self.Pe, 2)) * self.PH / -14.0
        self.PB9 = self.AW * (1.0 - math.pow(self.Pe, 2)) * PI / 16.0

        self.PS = self.PB1 * self.m_lat_ + self.PB2 * math.sin(2.0 * self.m_lat_) + self.PB3 * math.sin(4.0 * self.m_lat_) + self.PB4 * math.sin(6.0 * self.m_lat_) + self.PB5 * math.sin(
            8.0 * self.m_lat_) + self.PB6 * math.sin(10.0 * self.m_lat_) + self.PB7 * math.sin(12.0 * self.m_lat_) + self.PB8 * math.sin(14.0 * self.m_lat_) + self.PB9 * math.sin(16.0 * self.m_lat_)

        self.PSo = self.PB1 * self.m_PLato_ + self.PB2 * math.sin(2.0 * self.m_PLato_) + self.PB3 * math.sin(4.0 * self.m_PLato_) + self.PB4 * math.sin(6.0 * self.m_PLato_) + self.PB5 * math.sin(
            8.0 * self.m_PLato_) + self.PB6 * math.sin(10.0 * self.m_PLato_) + self.PB7 * math.sin(12.0 * self.m_PLato_) + self.PB8 * math.sin(14.0 * self.m_PLato_) + self.PB9 * math.sin(16.0 * self.m_PLato_)

        self.PDL = self.m_lon_ - self.m_PLo_
        self.Pt = math.tan(self.m_lat_)
        self.PW = math.sqrt(1.0 - math.pow(self.Pe, 2)
                            * math.pow(math.sin(self.m_lat_), 2))
        self.PN = self.AW / self.PW
        self.Pnn = math.sqrt(math.pow(self.Pet, 2) *
                             math.pow(math.cos(self.m_lat_), 2))

        self.m_x_ = ((self.PS - self.PSo) + (1.0 / 2.0) * self.PN * math.pow(math.cos(self.m_lat_), 2.0) * self.Pt * math.pow(self.PDL, 2.0) + (1.0 / 24.0) * self.PN * math.pow(math.cos(self.m_lat_), 4) * self.Pt * (5.0 - math.pow(self.Pt, 2) + 9.0 * math.pow(self.Pnn, 2) + 4.0 * math.pow(self.Pnn, 4)) * math.pow(self.PDL, 4) - (1.0 / 720.0) * self.PN * math.pow(math.cos(self.m_lat_), 6) * self.Pt *
                     (-61.0 + 58.0 * math.pow(self.Pt, 2) - math.pow(self.Pt, 4) - 270.0 * math.pow(self.Pnn, 2) + 330.0 * math.pow(self.Pt, 2) * math.pow(self.Pnn, 2)) * math.pow(self.PDL, 6) - (1.0 / 40320.0) * self.PN * math.pow(math.cos(self.m_lat_), 8) * self.Pt * (-1385.0 + 3111 * math.pow(self.Pt, 2) - 543 * math.pow(self.Pt, 4) + math.pow(self.Pt, 6)) * math.pow(self.PDL, 8)) * self.Pmo

        self.m_y_ = (self.PN * math.cos(self.m_lat_) * self.PDL - 1.0 / 6.0 * self.PN * math.pow(math.cos(self.m_lat_), 3) * (-1 + math.pow(self.Pt, 2) - math.pow(self.Pnn, 2)) * math.pow(self.PDL, 3) - 1.0 / 120.0 * self.PN * math.pow(math.cos(self.m_lat_), 5) * (-5.0 + 18.0 * math.pow(self.Pt, 2) - math.pow(self.Pt, 4) -
                     14.0 * math.pow(self.Pnn, 2) + 58.0 * math.pow(self.Pt, 2) * math.pow(self.Pnn, 2)) * math.pow(self.PDL, 5) - 1.0 / 5040.0 * self.PN * math.pow(math.cos(self.m_lat_), 7) * (-61.0 + 479.0 * math.pow(self.Pt, 2) - 179.0 * math.pow(self.Pt, 4) + math.pow(self.Pt, 6)) * math.pow(self.PDL, 7)) * self.Pmo

        self.m_z_ = self.m_h_


geo_ = GeoPosConv()
geo_.set_plane_by_num(0)

latitude_ = 35.104
longitude_ = 117.408
altitude_ = 141.002
geo_.llh_to_xyz(latitude_, longitude_, altitude_)

# std::cout << " x y z " << std::to_string(geo_.x()) << " " << std::to_string(geo_.y()) << " " << std::to_string(geo_.z()) << std::endl;
print(geo_.x())
print(geo_.y())
print(geo_.z())
