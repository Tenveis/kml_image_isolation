
import csv
import os
import sys
import shutil

# /home/vibi/Downloads/personal/DREAM/test/input_data/images

# print("start-> ")
# print("end -> ")


class Isolate_img():
    def __init__(self, ):
        print("start-> __init__")

        # self.make_process_dir()
        # self.open_files()
        # self.read_csv()
        # self.isolate_image()
        # self.close_files()
        print("end -> __init__")
        print("Finished!!!")

    def get_input_data(self, csv_file, img_dir, c1_lat, c1_lon, c2_lat, c2_lon):
        self.csv_file = csv_file
        if not self.csv_file.endswith(".csv"):
            print("It is not a csv file.")
            return "It is not a csv file."

        self.img_dir = img_dir

        if not os.path.exists(self.img_dir):
            return "Image directory does not exist."

        try:
            self.c1_lat = float(c1_lat)
            self.c1_lon = float(c1_lon)
            self.c2_lat = float(c2_lat)
            self.c2_lon = float(c2_lon)
            # 4 cases:
            if((self.c1_lat < self.c2_lat) and (self.c1_lon < self.c2_lon)):
                self.poly_quad = 1
            elif((self.c1_lat > self.c2_lat) and (self.c1_lon < self.c2_lon)):
                self.poly_quad = 2
            elif((self.c1_lat > self.c2_lat) and (self.c1_lon > self.c2_lon)):
                self.poly_quad = 3
            elif((self.c1_lat < self.c2_lat) and (self.c1_lon > self.c2_lon)):
                self.poly_quad = 4

        except Exception as e:
            print("coordinate values are not float",e)
            return "coordinate values are not float"

        return 1

    def get_csv_data(self):
        print("start-> get_csv_data")

        print("end -> get_csv_data")

    def read_csv(self):
        try:
            print("start-> read_csv")
            self.csv_data_list = csv.reader(self.csv_ip_file)
            print("end -> read_csv")
            return 1
        except:
            return "unable to read csv file."

    def open_files(self):
        try:
            print("start-> open_files")
            self.csv_ip_file = open(self.csv_file, "r")
            print("end -> open_files")
            return 1
        except:
            return "unable to open file."

    def close_files(self):
        try:
            print("start-> close_files")
            self.csv_ip_file.close()
            print("end -> close_files")
            return 1
        except:
            return "unable to close file."

    def make_process_dir(self):
        try:
            print("start-> make_process_dir")
            os.mkdir(self.img_dir+"/processed")
            print("end -> make_process_dir")
            return 1
        except:
            return 2

    def isolate_image(self):
        print("start-> isolate_image")
        for lines in self.csv_data_list:
            try:
                p_lat = float(lines[1])
                p_lon = float(lines[2])
                self.img_flag = 0
                if self.poly_quad == 1:
                    if(((p_lat > self.c1_lat) and (p_lat < self.c2_lat)) and ((p_lon > self.c1_lon) and (p_lon < self.c2_lon))):
                        self.img_flag = 1
                elif self.poly_quad == 2:
                    if(((p_lat < self.c1_lat) and (p_lat > self.c2_lat)) and ((p_lon > self.c1_lon) and (p_lon < self.c2_lon))):
                        self.img_flag = 1
                elif self.poly_quad == 3:
                    if(((p_lat < self.c1_lat) and (p_lat > self.c2_lat)) and ((p_lon < self.c1_lon) and (p_lon > self.c2_lon))):
                        self.img_flag = 1
                elif self.poly_quad == 4:
                    if(((p_lat > self.c1_lat) and (p_lat < self.c2_lat)) and ((p_lon < self.c1_lon) and (p_lon > self.c2_lon))):
                        self.img_flag = 1

                if self.img_flag == 1:
                    shutil.copy2(self.img_dir+"/" +
                                 lines[0], self.img_dir+"/processed")
                    print(lines[0])
                # print(lines[1], lines[2])
            except:
                return "coordinates in csv file are not float : [{0}, {1}, {2}]".format(lines[0], lines[1], lines[2])

        print("end -> isolate_image")
        return 1


if __name__ == "__main__":
    csv_file = r"/home/vibi/Downloads/personal/DREAM/test/input_data/csv1.csv"
    img_dir = r"/home/vibi/Downloads/personal/DREAM/test/input_data/images"
    c1_lat, c1_lon = 25.234581, "92.490524"
    c2_lat, c2_lon = 25.235609, 92.487755
    k = Isolate_img()
    k.get_input_data(csv_file, img_dir, c1_lat, c1_lon, c2_lat, c2_lon)
