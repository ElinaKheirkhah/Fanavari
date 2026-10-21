#===============================================
#=====================Task 3====================
#===============================================
#======File Management and Analysis Tool========
#===============================================

import os
import math

folder_path = "F:/fanavari/Fanavari/session9-10/project"

if os.path.exists(folder_path):
    print("Folder exists.")
    
    files = os.listdir(folder_path)

    print(files)


    print(f"Total files: {len(files)}")

    total_size = 0
    total_number = len(files)


    largest_file = None
    smallest_file = None

    largest_size = 0
    smallest_size = None

    extension_counts = {}


    for file in files:
        file_path = os.path.isfile(os.path.join(folder_path, file))
        size_bytes = os.path.getsize(file_path)
        size_kb = math.ceil(size_bytes / 1024)
        total_size = total_size + size_kb
        print(f"{file}: {size_kb} KB")
        
        if largest_file is None or size_kb > largest_size:
            largest_file = file
            largest_size = size_kb

        if smallest_file is None or size_kb < smallest_size:
            smallest_file = file
            smallest_size = size_kb
            
            
        name, extension = os.path.splitext(file)

        if extension in extension_counts:
            extension_counts[extension] += 1
        else:
            extension_counts[extension] = 1    

    miangin = total_size / total_number
    print(f"miangin hajm file ha: {miangin}")

        
    print(f"Largest file: {largest_file} ({largest_size} KB)")
    print(f"Smallest file: {smallest_file} ({smallest_size} KB)")    
        
        
    print("File counts by extension:")

    for extension, count in extension_counts.items():
        print(f"{extension}: {count}")   
        
else:
    print("Folder does not exist.")
    





#=====================Challenge=================

reports_path = os.path.join(folder_path, "reports")

os.makedirs(reports_path, exist_ok=True)

report_path = os.path.join(reports_path, "analysis_report.txt")

with open(report_path, "w", encoding="utf-8") as report:

    report.write("========== File Analysis Report ==========\n\n")

    report.write(f"Folder path: {folder_path}\n")
    report.write(f"Total files: {total_number}\n")
    report.write(f"Total size: {total_size} KB\n")
    report.write(f"Average file size: {miangin:.2f} KB\n\n")

    report.write("---------- File Details ----------\n")

    for file in files:
        file_path = os.path.join(folder_path, file)
        size_bytes = os.path.getsize(file_path)
        size_kb = math.ceil(size_bytes / 1024)

        report.write(f"{file}: {size_kb} KB\n")

    report.write("\n---------- Largest File ----------\n")
    report.write(f"{largest_file}: {largest_size} KB\n")

    report.write("\n---------- Smallest File ----------\n")
    report.write(f"{smallest_file}: {smallest_size} KB\n")

    report.write("\n---------- File Counts by Extension ----------\n")

    for extension, count in extension_counts.items():
        report.write(f"{extension}: {count}\n")

print("Report created successfully")

    