
import csv
import os
import sys
import shutil

# /home/vibi/Downloads/personal/DREAM/test/input_data/images

# print("start-> ")
# print("end -> ")


class Isolate_img():
    def __init__(self, csv_file, img_dir, c1_lat, c1_lon, c2_lat, c2_lon):
        print("start-> __init__")
        self.csv_file = csv_file
        self.img_dir = img_dir
        self.c1_lat = c1_lat
        self.c1_lon = c1_lon
        self.c2_lat = c2_lat
        self.c2_lon = c2_lon

        self.make_process_dir()
        self.open_files()
        self.read_csv()
        self.isolate_image()

        self.close_files()
        print("end -> __init__")
        print("Finished!!!")

    def get_csv_data(self):
        print("start-> get_csv_data")

        print("end -> get_csv_data")

    def read_csv(self):
        print("start-> read_csv")
        self.csv_data_list = csv.reader(self.csv_ip_file)

        print("end -> read_csv")
        pass

    def open_files(self):
        print("start-> open_files")
        self.csv_ip_file = open(self.csv_file, "r")

        print("end -> open_files")
        pass

    def close_files(self):
        print("start-> close_files")
        self.csv_ip_file.close()

        print("end -> close_files")
        pass

    def make_process_dir(self):
        print("start-> make_process_dir")
        try:
            os.mkdir(self.img_dir+"/processed")
        except:
            pass
        print("end -> make_process_dir")

    def isolate_image(self):
        print("start-> isolate_image")
        for lines in self.csv_data_list:
            if((float(lines[1]) > self.c1_lat) and (float(lines[1]) < self.c2_lat) and (float(lines[2]) < self.c1_lon) and ((float(lines[2]) > self.c2_lon))):
                shutil.copy2(self.img_dir+"/" +
                             lines[0], self.img_dir+"/processed")
                print(lines[0])
            print(lines[1], lines[2])

        print("end -> isolate_image")


if __name__ == "__main__":
    csv_file = r"/home/vibi/Downloads/personal/DREAM/test/input_data/csv1.csv"
    img_dir = r"/home/vibi/Downloads/personal/DREAM/test/input_data/images"
    c1_lat, c1_lon = 25.234581, 92.490524
    c2_lat, c2_lon = 25.235609, 92.487755
    k = Isolate_img(csv_file, img_dir, c1_lat, c1_lon, c2_lat, c2_lon)
