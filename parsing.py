'''
# Open the log file and output file
with open('/home/emumba/Desktop/Designs/9871/logs/optimization/dummy_logfile.txt', 'r') as log_file, open('/home/emumba/Desktop/9871/qor/fermi.txt', 'w') as output_file:
    for line in log_file:
        # Check if the line contains "stat = value" pattern
        if '=' in line:
            # Split the line by '=' and strip any extra spaces
            stat, value = map(str.strip, line.split('=', 1))
            # Write to output file in the format "stat : value"
            output_file.write(f"{stat} : {value}\n")

print("fermi.txt file has been generated with the desired format.")
'''

import argparse
import os
import shutil

def parse_log_file(log_file_path, output_file_path):
    with open(log_file_path, 'r') as log_file, open(output_file_path, 'w') as output_file:
        for line in log_file:
            # Check if the line contains "stat = value" pattern
            if '=' in line:
                # Split the line by '=' and strip any extra spaces
                stat, value = map(str.strip, line.split('=', 1))
                # Write to output file in the format "stat : value"
                output_file.write(f"{stat} : {value}\n")
    print(f"fermi.txt file has been generated at {output_file_path}.")

def copy_qor_folder(jobid_folder, rsync_directory):
    qor_folder = os.path.join(jobid_folder, 'qor')
    if os.path.exists(qor_folder):
        # Define the destination path to include both jobid folder and qor folder
        destination = os.path.join(rsync_directory, os.path.basename(jobid_folder), 'qor')
        # Copy the qor folder (including the folder itself) to the destination
        shutil.copytree(qor_folder, destination, dirs_exist_ok=True)
        print(f"Copied QOR folder to {destination}.")
    else:
        print(f"QOR folder does not exist in {jobid_folder}.")


def main():
    parser = argparse.ArgumentParser(description="Process log files and manage job directories.")
    parser.add_argument('-l', '--location', required=True, help="Path to the directory containing jobid folders.")
    parser.add_argument('-id', '--jobid', required=True, help="ID of the job (jobid folder name).")
    parser.add_argument('-p', '--parse', action='store_true',required=True, help="Parse the log file and save as fermi.txt in qor folder.")
    parser.add_argument('-r', '--rsync', help="Copy QOR folder to the rsync directory.")

    args = parser.parse_args()

    # Construct paths for the log file and fermi.txt output
    jobid_folder = os.path.join(args.location, args.jobid)
    log_file_path = os.path.join(jobid_folder, 'logs/optimization/dummy_logfile.txt')
    qor_output_folder = os.path.join(jobid_folder, 'qor')
    output_file_path = os.path.join(qor_output_folder, 'fermi.txt')

    # Parse the log file and save fermi.txt if -p is provided
    if args.parse:
        if not os.path.exists(log_file_path):
            print(f"Log file {log_file_path} not found.")
            return
        os.makedirs(qor_output_folder, exist_ok=True)
        parse_log_file(log_file_path, output_file_path)

    # Copy QOR folder to rsync directory if -r is provided
    if args.rsync:
        if not os.path.exists(args.rsync):
            print(f"Rsync directory {args.rsync} not found.")
            return
        copy_qor_folder(jobid_folder, args.rsync)

if __name__ == '__main__':
    main()