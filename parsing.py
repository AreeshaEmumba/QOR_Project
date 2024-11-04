# Open the log file and output file
with open('/home/emumba/Desktop/9871/logs/optimization/dummy_logfile.txt', 'r') as log_file, open('/home/emumba/Desktop/9871/qor/fermi.txt', 'w') as output_file:
    for line in log_file:
        # Check if the line contains "stat = value" pattern
        if '=' in line:
            # Split the line by '=' and strip any extra spaces
            stat, value = map(str.strip, line.split('=', 1))
            # Write to output file in the format "stat : value"
            output_file.write(f"{stat} : {value}\n")

print("fermi.txt file has been generated with the desired format.")