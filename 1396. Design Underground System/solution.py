class UndergroundSystem:

    def __init__(self):
        self.station_path_avg_distance = {}
        self.station_path_num = {}
        self.checkins = {}  

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin_station, checkin_time = self.checkins[id]
        time_taken = t - checkin_time

        n = self.station_path_num.get((checkin_station, stationName), 0)
        curr_avg = self.station_path_avg_distance.get((checkin_station, stationName), 0)

        self.station_path_num[(checkin_station, stationName)] = 1 + n
        self.station_path_avg_distance[(checkin_station, stationName)] = (n * curr_avg + time_taken) / self.station_path_num[(checkin_station, stationName)]
        del self.checkins[id]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.station_path_avg_distance[(startStation, endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
